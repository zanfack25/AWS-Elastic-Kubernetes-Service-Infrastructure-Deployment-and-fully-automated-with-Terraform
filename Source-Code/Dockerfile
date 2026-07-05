

FROM python:3.10-slim

LABEL authors="David-Roland-Gnimpieba Z."

WORKDIR /app

COPY app.py .

RUN pip install fastapi uvicorn boto3 pandas openpyxl python-dateutil

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
