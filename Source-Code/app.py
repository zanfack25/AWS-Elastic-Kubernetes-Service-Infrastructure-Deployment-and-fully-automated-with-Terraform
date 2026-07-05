from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import boto3
import io
import datetime
from dateutil.relativedelta import relativedelta
from urllib.parse import urlparse

app = FastAPI()

INPUT_PATH = "s3://maintenance-operations-bucket/INPUT-MaintenanceOperationsData/maintenance_Operations_Input_Data.xlsx"
OUTPUT_PREFIX = "s3://maintenance-operations-bucket/OUTPUT-MaintenanceOperationsResults/"

def generate_schedule(df, budget_df, interval_label, interval_months):
    today = pd.to_datetime(datetime.date.today())
    due_date = df['Effective_Last_Maintenance'] + pd.to_timedelta(interval_months * 30, unit='D')
    filtered = df[
        (df['Recommended_Interval'].str.lower() == interval_label.lower()) &
        (due_date <= today + pd.DateOffset(months=interval_months))
    ]
    merged = pd.merge(filtered, budget_df, on='Department', how='left')
    merged['Estimated_Cost'] = 1000
    merged = merged[merged['Remaining_Budget'] >= merged['Estimated_Cost']]
    result = merged.sort_values(by=['Criticality_Level', 'Risk_Impact'], ascending=[False, False])
    return result

@app.get("/generate-maintenance-plan")
def generate_plan():
    try:
        parsed_url = urlparse(INPUT_PATH)
        bucket_name = parsed_url.netloc
        key = parsed_url.path.lstrip('/')
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = response['Body'].read()
        excel_io = io.BytesIO(file_content)

        equipment_df = pd.read_excel(excel_io, sheet_name='Equipment_List', engine='openpyxl')
        excel_io.seek(0)
        maintenance_logs_df = pd.read_excel(excel_io, sheet_name='Maintenance_Logs', engine='openpyxl')
        excel_io.seek(0)
        maintenance_priorities_df = pd.read_excel(excel_io, sheet_name='Maintenance_Priorities', engine='openpyxl')
        excel_io.seek(0)
        budget_df = pd.read_excel(excel_io, sheet_name='Budget_Allocation', engine='openpyxl')

        equipment_priority_df = pd.merge(equipment_df, maintenance_priorities_df, on='Equipment_ID', how='left')
        latest_log = maintenance_logs_df.groupby('Equipment_ID')['Date'].max().reset_index()
        latest_log.columns = ['Equipment_ID', 'Last_Log_Date']
        equipment_priority_df = pd.merge(equipment_priority_df, latest_log, on='Equipment_ID', how='left')
        equipment_priority_df['Effective_Last_Maintenance'] = equipment_priority_df['Last_Maintenance_Date'].fillna(
            equipment_priority_df['Last_Log_Date']
        )

        plans = {
            '3_month': generate_schedule(equipment_priority_df, budget_df, '3 months', 3),
            'quarterly': generate_schedule(equipment_priority_df, budget_df, 'Quarterly', 3),
            '6_month': generate_schedule(equipment_priority_df, budget_df, '6 Months', 6),
            'annual': generate_schedule(equipment_priority_df, budget_df, 'Annual', 12),
            'biannual': generate_schedule(equipment_priority_df, budget_df, 'Biannual', 24)
        }

        for plan_name, df in plans.items():
            if df.empty:
                continue
            output_key = f'{OUTPUT_PREFIX}{plan_name}_maintenance_plan.xlsx'.replace("s3://", "").split("/", 1)[1]
            with io.BytesIO() as buffer:
                df.to_excel(buffer, index=False)
                buffer.seek(0)
                s3_client.put_object(Bucket=bucket_name, Key=output_key, Body=buffer.getvalue())

        global_plan = pd.concat(plans.values(), ignore_index=True).drop_duplicates()
        if not global_plan.empty:
            global_key = f'{OUTPUT_PREFIX}global_maintenance_plan.xlsx'.replace("s3://", "").split("/", 1)[1]
            with io.BytesIO() as buffer:
                global_plan.to_excel(buffer, index=False)
                buffer.seek(0)
                s3_client.put_object(Bucket=bucket_name, Key=global_key, Body=buffer.getvalue())

        return {"status": "success", "message": "Maintenance plans generated and uploaded."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
