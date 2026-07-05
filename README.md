# AWS-Elastic-Kubernetes-Service-Infrastructure-Deployment-and-fully-automated-with-Terraform
This project demonstrates the deployment of a production-ready Kubernetes infrastructure on AWS using Amazon Elastic Kubernetes Service (EKS) and Terraform. 

# EKS Infrastructure Deployment with Terraform
# Project Overview

This project demonstrates the deployment of a production-ready Kubernetes infrastructure on AWS using Amazon Elastic Kubernetes Service (EKS) and Terraform. The infrastructure was designed for the Oshawa Public Library (OPL) digital transformation initiative to host a containerized application consisting of a frontend, backend API, and cloud storage integration.

The project follows Infrastructure as Code (IaC) principles to provision and manage AWS resources while implementing Kubernetes best practices for security, scalability, high availability, fault tolerance, and workload isolation.

# Objective

## Design and deploy an intermediate-level cloud-native Kubernetes platform that:

Automates infrastructure provisioning using Terraform
Deploys a managed Kubernetes cluster with Amazon EKS
Implements secure networking using a custom VPC
Runs containerized workloads on scalable worker nodes
Integrates Amazon ECR for container images
Provides secure access to Amazon S3 storage
Demonstrates Kubernetes deployment, scaling, and networking concepts
Implements high availability and fault-tolerant architecture across multiple Availability Zones

# Architecture

                     Internet
                         │
                 AWS Load Balancer
                         │
          ─────────────────────────────────
                  Amazon EKS Cluster
          (Managed Kubernetes Control Plane)
          ─────────────────────────────────
                 │                  │
      Worker Node Group      Worker Node Group
      (Private Subnet)       (Private Subnet)
         AZ-A                    AZ-B
           │                        │
     Kubernetes Pods         Kubernetes Pods
           │                        │
           └────────────┬───────────┘
                        │
                Amazon S3 Storage
                        │
                  Amazon ECR Images

                  
# AWS Services Used| Service                      | Purpose                                      |
| ---------------------------- | -------------------------------------------- |
| **Amazon EKS**               | Managed Kubernetes cluster                   |
| **Amazon EC2**               | Kubernetes worker nodes                      |
| **Amazon VPC**               | Network isolation                            |
| **Public & Private Subnets** | Segmentation of public and private resources |
| **Internet Gateway**         | Public internet access                       |
| **NAT Gateway**              | Secure outbound internet for private nodes   |
| **Amazon ECR**               | Container image registry                     |
| **Amazon S3**                | Object storage for application assets        |
| **IAM**                      | Identity and access management               |
| **Security Groups**          | Network security                             |
| **Elastic Load Balancer**    | Exposes Kubernetes services                  |
| **Terraform**                | Infrastructure as Code automation            |


# Key Cloud Features Implemented
## Infrastructure as Code (Terraform)
    Provisioned the complete AWS infrastructure using Terraform
    Modular infrastructure design
    Version-controlled infrastructure
    Repeatable and consistent deployments
    Simplified infrastructure updates and maintenance



# Amazon EKS Implementation

## Implemented a fully managed Kubernetes cluster using Amazon EKS.
### Features
    Managed Kubernetes control plane
    AWS-managed API Server
    Kubernetes Scheduler
    etcd management by AWS
    IAM authentication
    Native AWS integration
    Multi-AZ control plane
    
### Benefits
    Reduced operational overhead
    Automatic Kubernetes control plane management
    High availability by default
    Secure cluster authentication

# Kubernetes Node Groups

## Implemented managed node groups running on Amazon EC2.

### Features
    Managed worker nodes
    Auto Scaling enabled
    Private subnet deployment
    IAM roles attached to worker nodes
    Container workload execution

### Scaling Configuration  
| Parameter     | Value     |
| ------------- | --------- |
| Instance Type | t3.medium |
| Minimum Nodes | 1         |
| Desired Nodes | 3         |
| Maximum Nodes | 5         |


# Kubernetes Workload Deployment

Successfully deployed a containerized Python API to the EKS cluster.

Implementation included:

  Docker container creation
  Image push to Amazon ECR
  Kubernetes Deployment
  Kubernetes Service
  External LoadBalancer
  Pod scheduling across worker nodes


# Networking Implementation

A secure custom VPC architecture was deployed.

## VPC Design
    Custom VPC (192.168.0.0/16)
    2 Public Subnets
    2 Private Subnets
    Internet Gateway
    NAT Gateway
    Route Tables
    
## Kubernetes Networking
    Worker nodes deployed only in private subnets
    LoadBalancer Service exposes the application
    Internal cluster communication secured
    Controlled outbound internet access through NAT Gateway

## Security Implementation

Security was designed following AWS and Kubernetes best practices.

    IAM Security
    Separate IAM role for EKS Cluster
    Separate IAM role for Worker Nodes
    Least Privilege Principle
    Custom IAM policy for Amazon S3 access
### Network Security

Implemented Security Groups to restrict traffic.

### Control Plane
  HTTPS (443) only
  Restricted communication
### Worker Nodes
  Private subnet isolation
  Limited SSH access
  Trusted source restrictions
### Storage Security
  IAM-based S3 access
  No public S3 permissions
  Node-specific storage permissions

# Designed to follow AWS Well Architceture framework

## High Availability

The infrastructure was designed for continuous availability.

Implemented:

    Multi-AZ deployment
    Highly available EKS control plane
    Worker nodes distributed across two Availability Zones
    Elastic Load Balancer
    Private subnet redundancy
    AWS managed Kubernetes control plane

## Fault Tolerance

Several mechanisms improve resilience against failures.

Implemented
    Multi-AZ worker nodes
    Kubernetes pod rescheduling
    Managed Kubernetes control plane
    Load balancing across healthy nodes
    Auto recovery through Kubernetes scheduling

If a worker node becomes unavailable, Kubernetes automatically schedules workloads on healthy nodes.

## Scalability

The platform dynamically scales based on workload demand.

Kubernetes Features
Managed Node Groups
Cluster scaling
Dynamic pod scheduling
Load-balanced application traffic
AWS Features
EC2 Auto Scaling
Elastic Load Balancer
Managed EKS control plane

## Redundancy

Redundancy was implemented across multiple infrastructure layers.

Multi-AZ deployment
Multiple worker nodes
Redundant networking
Highly available control plane
Amazon S3 durability
Elastic Load Balancer distribution

This minimizes service disruption during infrastructure failures.


# Container Workflow

The application deployment pipeline followed standard Kubernetes practices.

Docker Build
      │
      ▼
Amazon ECR
      │
      ▼
Amazon EKS
      │
      ▼
Kubernetes Deployment
      │
      ▼
Pods
      │
      ▼
LoadBalancer Service
      │
      ▼
Public Application


Testing & Validation

# The deployed infrastructure was validated by deploying a Dockerized Python API.

## Validation Steps
  Built Docker image
  Pushed image to Amazon ECR
  Created Kubernetes Deployment
  Created Kubernetes Service
  Exposed service through AWS LoadBalancer
  Verified pod scheduling
  Verified image retrieval from Amazon ECR
  Tested Amazon S3 connectivity
  Issue Resolved

An IAM permission issue initially prevented the application from accessing Amazon S3. The problem was resolved by attaching a custom IAM policy to the EKS worker node role, restoring secure access to storage.

# Kubernetes Concepts Demonstrated

  Managed Kubernetes (Amazon EKS)
  Kubernetes Deployments
  Kubernetes Services
  LoadBalancer Service
  Pod Scheduling
  Managed Node Groups
  Cluster Networking
  Worker Nodes
  Container Orchestration
  Declarative Infrastructure
  Infrastructure as Code
  Container Image Management
  Cloud-native Application Deployment

# Results and outcomes

  Successfully deployed an intermediate-level cloud-native Kubernetes platform that provides:
  
  Automated AWS infrastructure provisioning with Terraform
  Managed Kubernetes cluster using Amazon EKS
  Secure container deployment with Amazon ECR
  Private networking using Amazon VPC
  Secure object storage integration with Amazon S3
  Auto-scaling Kubernetes worker nodes
  Multi-AZ high availability architecture
  Fault-tolerant workload scheduling
  Secure IAM-based access control
  Public application exposure using AWS LoadBalancer
  
  The project demonstrates practical experience with deploying and managing Kubernetes workloads on AWS while applying cloud architecture principles such as security, scalability, redundancy, high availability, and Infrastructure as Code.


# Future Improvements

  Implement CI/CD with GitHub Actions
  Deploy applications using Helm charts
  Integrate Amazon RDS for PostgreSQL
  Configure AWS Load Balancer Controller or NGINX Ingress
  Install Metrics Server
  Deploy Prometheus and Grafana for monitoring
  Enable Horizontal Pod Autoscaler (HPA)
  Add centralized logging with Fluent Bit and CloudWatch
  Implement IRSA (IAM Roles for Service Accounts) for fine-grained pod-level permissions

# Skills Demonstrated

  Amazon EKS
  Kubernetes
  Terraform
  Docker
  Amazon EC2
  Amazon VPC
  Amazon ECR
  Amazon S3
  IAM
  Security Groups
  Elastic Load Balancing
  Infrastructure as Code (IaC)
  Cloud Networking
  High Availability Architecture
  Fault Tolerance
  Auto Scaling
  Container Orchestration
  Cloud Security Best Practices

  
