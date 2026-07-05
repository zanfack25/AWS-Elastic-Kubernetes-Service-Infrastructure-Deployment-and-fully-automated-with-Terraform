# AWS-Elastic-Kubernetes-Service-Infrastructure-Deployment-and-fully-automated-with-Terraform
This project demonstrates the deployment of a production-ready Kubernetes infrastructure on AWS using Amazon Elastic Kubernetes Service (EKS) and Terraform. 

# EKS Infrastructure Deployment with Terraform
# Project Overview

This project demonstrates the deployment of a production-ready Kubernetes infrastructure on AWS using Amazon Elastic Kubernetes Service (EKS) and Terraform. The infrastructure was designed for the Oshawa Public Library (OPL) digital transformation initiative to host a containerized application consisting of a frontend, backend API, and cloud storage integration.

The project follows Infrastructure as Code (IaC) principles to provision and manage AWS resources while implementing Kubernetes best practices for security, scalability, high availability, fault tolerance, and workload isolation.

# Objective

## Business Objective

  The Oshawa Public Library (OPL) is undergoing a digital transformation to improve public
  access to its services. The library application consists of a front-end for public access and a
  back-end API connected to a PostgreSQL database and an S3 image storage bucket.
  To support this application, we deployed a fully managed Kubernetes cluster on AWS using
  EKS and Terraform. This infrastructure enables scalability, high availability, and security, all
  managed as Infrastructure as Code (IaC).

## Technical Objective: Design and deploy an intermediate-level cloud-native Kubernetes platform that:

Automates infrastructure provisioning using Terraform
Deploys a managed Kubernetes cluster with Amazon EKS
Implements secure networking using a custom VPC
Runs containerized workloads on scalable worker nodes
Integrates Amazon ECR for container images
Provides secure access to Amazon S3 storage
Demonstrates Kubernetes deployment, scaling, and networking concepts
Implements high availability and fault-tolerant architecture across multiple Availability Zones

# Why chosing EKS 

<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/275b0058-01f9-442b-bd6e-f060c733d22e" />


Amazon EKS was chosen as the core orchestration platform due to its managed control plane,
which simplifies Kubernetes operations while ensuring high availability. The cluster integrates
seamlessly with AWS Identity and Access Management (IAM) for secure authentication and is
deployed within a custom Virtual Private Cloud (VPC) to allow fine-grained control over
networking and access.

## Key Features:
●​ AWS-managed control plane (highly available)​
●​ Integrated with IAM for secure authentication​
●​ Deploys into custom VPC for fine-grained networking

## EKS (Elastic Kubernetes Service) Cluster
  -​ A managed Kubernetes control plane on AWS.
  - It handles the orchestration of containerized applications
  - Control Plane: AWS manages the Kubernetes master components (API server, etcd,
scheduler, controller).​
  -​ VPC Integration: The cluster is deployed into a custom Virtual Private Cloud (VPC) with
secure networking (private/public subnets).​
  -​ API Endpoint Access: You can control whether the Kubernetes API is publicly
accessible or only from within the VPC.

## Node Groups
  EKS Node Groups consist of EC2 instances that serve as the compute layer for running
  application pods. These nodes are configured to auto-scale based on workload demand and are
  deployed in private subnets to minimize exposure to external threats. IAM roles are assigned to
  these nodes to enforce secure access to AWS resources such as S3 and ECR.

Key Features:
  ●​ Auto-scaling worker nodes​
  ●​ Secure IAM roles for workload permissions​
  ●​ Deployed in private subnets to limit exposure
  ●​ Node Group is a set of EC2 instances (worker nodes) that run your containerized
  applications in the EKS cluster.
  ●​ Autoscaling: Node groups can scale automatically based on workload demand (min,
  max, desired size).​
  ●​ IAM Role: Each node group has a role that allows it to interact with the EKS control
  plane and AWS services like ECR or S3.
  ●​ Runs Workloads: Pods are scheduled on these nodes, and they handle the actual
  application processing.

# EKS Infrastructure automation with Terraform

Terraform was used to automate the provisioning of all infrastructure components. Its
declarative syntax and modular design enabled the creation of reusable and version-controlled
configurations for the VPC, EKS cluster, node groups, IAM roles, and networking components.
This ensured consistency across environments and simplified future updates.

Key Features:
●​ Infrastructure as Code (IaC)​
●​ Modular and version-controlled​
●​ Used to provision VPC, EKS, Node Groups, IAM, and networking



​

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


# Infrastructure Layers and Design Justification


<img width="2048" height="707" alt="image" src="https://github.com/user-attachments/assets/81120000-64ac-4405-82d1-86813e1a52dd" />



                  
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
  - Provisioned the complete AWS infrastructure using Terraform
  - Modular infrastructure design
  - Version-controlled infrastructure
  - Repeatable and consistent deployments
  - Simplified infrastructure updates and maintenance



# Amazon EKS Implementation

## Implemented a fully managed Kubernetes cluster using Amazon EKS.
### Features
   - Managed Kubernetes control plane
   - AWS-managed API Server
   - Kubernetes Scheduler
   - etcd management by AWS
   - IAM authentication
   - Native AWS integration
   - Multi-AZ control plane
    
### Benefits
   - Reduced operational overhead
   - Automatic Kubernetes control plane management
   - High availability by default
   - Secure cluster authentication


<img width="1776" height="789" alt="image" src="https://github.com/user-attachments/assets/72633e74-a617-43a7-b4b9-5a879971dfe6" />




# Kubernetes Node Groups

## Implemented managed node groups running on Amazon EC2.

### Features
   - Managed worker nodes
   - Auto Scaling enabled
   - Private subnet deployment
   - IAM roles attached to worker nodes
   - Container workload execution

### Scaling Configuration  
| Parameter     | Value     |
| ------------- | --------- |
| Instance Type | t3.medium |
| Minimum Nodes | 1         |
| Desired Nodes | 3         |
| Maximum Nodes | 5         |


<img width="1788" height="715" alt="image" src="https://github.com/user-attachments/assets/fc6c8001-ef37-41b6-a425-83839ee7b289" />

<img width="1387" height="214" alt="image" src="https://github.com/user-attachments/assets/ee6f3b61-34cc-4ffa-9802-db48ac776cca" />




# Kubernetes Workload Deployment

Successfully deployed a containerized Python API to the EKS cluster.

Implementation included:

  Docker container creation
  Image push to Amazon ECR
  Kubernetes Deployment
  Kubernetes Service
  External LoadBalancer
  Pod scheduling across worker nodes

Provisioning EKS with Terraform-Pods

<img width="1765" height="802" alt="image" src="https://github.com/user-attachments/assets/33ce80ad-ea57-4db7-9a27-dabd39825b3b" />






# Networking Implementation


A secure custom VPC architecture was deployed.

A custom VPC with CIDR block 192.168.0.0/16 was created to isolate and manage network
traffic. It includes two public subnets for load balancers and NAT gateways, and two private
subnets for EKS nodes. Internet and NAT gateways were configured to control external access,
and subnets were distributed across two availability zones to ensure high availability.

●​ Create a custom VPC (192.168.0.0/16) with:​
    2 Public Subnets (for load balancer / NAT)​
    2 Private Subnets (for EKS nodes)
    Internet Gateway & NAT Gateway
    Private subnets for workload isolation
    NAT for secure outbound internet access​
●​ Configured Internet Gateway and NAT Gateway for controlled external access​
●​ Subnets spread across 2 Availability Zones for high availability

## VPC Design
  - Custom VPC (192.168.0.0/16)
  - 2 Public Subnets
  - 2 Private Subnets
  - Internet Gateway
  - NAT Gateway
  - Route Tables

  -   
## Kubernetes Networking
  - Worker nodes deployed only in private subnets
  - LoadBalancer Service exposes the application
  - Internal cluster communication secured
  - Controlled outbound internet access through NAT Gateway



    
<img width="1759" height="711" alt="image" src="https://github.com/user-attachments/assets/2ff161a5-c106-48e9-999d-f4be439d1d07" />

<img width="1780" height="804" alt="image" src="https://github.com/user-attachments/assets/a6f80db6-793c-4874-ac7f-d4e06fc03ee6" />

Public Route Table

  <img width="1324" height="784" alt="image" src="https://github.com/user-attachments/assets/fc47d49c-6250-4b1c-8c5a-b73f7437eb82" />

Private Route Table 

<img width="1264" height="649" alt="image" src="https://github.com/user-attachments/assets/c8e7b447-92e4-4d2b-b507-6638c6278011" />




## Security Implementation

Security was designed following AWS and Kubernetes best practices.

   - IAM Security
   - Separate IAM role for EKS Cluster
   - Separate IAM role for Worker Nodes
   - Least Privilege Principle
   - Custom IAM policy for Amazon S3 access

Security was enforced using IAM roles that follow the principle of least privilege. Separate roles
were created for the EKS cluster and node groups, with tightly scoped permissions. Inbound
access to the control plane was restricted to port 443 within the VPC, and SSH access to nodes
was limited to trusted IP sources. S3 access was granted only to nodes that required it.

●​ Used IAM roles with least privilege principle for:​
  ○​ Cluster (eks_cluster_role)​
  ○​ Node Group (eks_node_role)​
●​ Limited inbound access on control plane (port 443 only within VPC)​
●​ Limited SSH access to nodes (port 22 only from trusted sources)​
●​ Applied S3 access policy only to nodes that need it
●​ IAM: Cluster and Node roles with minimal privileges​
●​ SGs:​
  ○​ Control plane allows only internal communication (port 443)​
  ○​ Worker nodes limited SSH (port 22)​
●​ Private subnets: for worker node isolation​
●​ S3 Bucket Access: Policy granted only to node IAM role

### Network Security

Implemented Security Groups to restrict traffic.

### Control Plane
  HTTPS (443) only
  Restricted communication
### Worker Nodes
 - Private subnet isolation
 - Limited SSH access
 - Trusted source restrictions
### Storage Security
 - IAM-based S3 access
 - No public S3 permissions
 - Node-specific storage permissions

Node security bgroup 

<img width="1462" height="748" alt="image" src="https://github.com/user-attachments/assets/0cdaa384-90ef-45ac-b377-27fd82204229" />

<img width="1482" height="739" alt="image" src="https://github.com/user-attachments/assets/fe077ae7-b54b-427b-b9fc-fe32817dd608" />

Master security group 

<img width="1486" height="796" alt="image" src="https://github.com/user-attachments/assets/519d67eb-1d63-427b-ba43-4b3dffc76b72" />


# Designed to follow AWS Well Architceture framework

The infrastructure was designed for resilience and scalability. Multi-AZ deployment across
ca-central-1a and ca-central-1b ensures redundancy. The LoadBalancer service securely
exposes the public API, and node auto-scaling allows the system to adapt to varying workloads.
The EKS control plane, managed by AWS, guarantees high availability and operational stability.

●​ Multi-AZ deployment (ca-central-1a, ca-central-1b)(2 AZs for subnets)​
●​ LoadBalancer service exposes public API securely​
●​ Node auto-scaling ensures workload flexibility​
●​ EKS control plane is managed and highly available by AWS
●​ Autoscaling through Node Group
●​ Load Balancer via Kubernetes Service for front-end
●​ S3 is Highly available by design​

## High Availability

The infrastructure was designed for continuous availability.

Implemented:

   - Multi-AZ deployment
   - Highly available EKS control plane
   - Worker nodes distributed across two Availability Zones
   - Elastic Load Balancer
   - Private subnet redundancy
   - AWS managed Kubernetes control plane

## Fault Tolerance

Several mechanisms improve resilience against failures.

Implemented
  -  Multi-AZ worker nodes
  -  Kubernetes pod rescheduling
  -  Managed Kubernetes control plane
  -  Load balancing across healthy nodes
  -  Auto recovery through Kubernetes scheduling

If a worker node becomes unavailable, Kubernetes automatically schedules workloads on healthy nodes.


<img width="1759" height="711" alt="image" src="https://github.com/user-attachments/assets/8bd9ca61-a0ef-43a6-937e-a849f07e73d7" />


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

- Multi-AZ deployment
- Multiple worker nodes
- Redundant networking
- Highly available control plane
- Amazon S3 durability
- Elastic Load Balancer distribution

This minimizes service disruption during infrastructure failures.

# Storage Layer

Container images were stored in Amazon Elastic Container Registry (ECR), while application
media assets were managed in Amazon S3. To enable secure access to S3, a custom IAM
policy was attached to the node group role. The PostgreSQL database is planned for future
deployment, either via Amazon RDS or as an in-cluster service using Helm.

●​ Docker images stored in Amazon Elastic Container Registry (ECR)​
●​ Application uses Amazon S3 for storing images and media assets​
●​ IAM policy attached to Node Group Role to enable secure S3 access​
●​ PostgreSQL database will be provisioned separately (RDS or in-cluster for now)
●​ Docker images stored in Amazon Elastic Container Registry (ECR)​
●​ The PostgreSQL database via Amazon RDS
●​ S3 used for storing asset images (e.g., book covers, documents)​
●​ EKS node IAM role updated with S3 access policy​



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
 -  Built Docker image
 -  Pushed image to Amazon ECR
 -  Created Kubernetes Deployment
 -  Created Kubernetes Service
 -  Exposed service through AWS LoadBalancer
 - Verified pod scheduling
 - Verified image retrieval from Amazon ECR
 - Tested Amazon S3 connectivity
 - Issue Resolved

An IAM permission issue initially prevented the application from accessing Amazon S3. The problem was resolved by attaching a custom IAM policy to the EKS worker node role, restoring secure access to storage.

To validate the infrastructure, a Python-based API was containerized using Docker and pushed
to Amazon ECR. Kubernetes manifests were applied to deploy the application to the EKS
cluster, and a LoadBalancer was provisioned to expose the service externally. Initial deployment
encountered an issue with S3 access due to missing IAM permissions. This was resolved by
attaching a custom policy to the eks_node_role, after which the application was successfully
accessed via the public LoadBalancer endpoint.


1.​ Build and Push Docker Image:​
○​ Image built locally​
○​ Tagged and pushed to ECR


<img width="1831" height="772" alt="image" src="https://github.com/user-attachments/assets/519b4d2f-e280-4921-a96c-617009a8fe4b" />


2. Pushed the container to ECR

<img width="1810" height="787" alt="image" src="https://github.com/user-attachments/assets/f0f15ef8-5103-42d4-bf81-1343df4b3ef9" />

3. Deploy to EKS:​
  ○​ Kubernetes deployment and service manifests applied​
  ○​ LoadBalancer assigned an external IP


<img width="1816" height="820" alt="image" src="https://github.com/user-attachments/assets/d4cb01b8-360b-4eca-a32f-782c91bcad3e" />

<img width="1704" height="430" alt="image" src="https://github.com/user-attachments/assets/d69e9991-fc0e-480d-825d-b501e163085c" />

4.Verified that the image is deployed and is available in ECR 

<img width="1696" height="400" alt="image" src="https://github.com/user-attachments/assets/6630309d-4ec0-4983-9398-55bceae8c546" />

5. Verified that Pods pull the image from ECR and are running successfully


<img width="1710" height="807" alt="image" src="https://github.com/user-attachments/assets/497c8dad-b0ba-4eb1-a747-96d29086d2c1" />




<img width="1648" height="787" alt="image" src="https://github.com/user-attachments/assets/63277883-ed65-4f04-b620-be9670620aeb" />





# Kubernetes Concepts Demonstrated

 -  Managed Kubernetes (Amazon EKS)
 -  Kubernetes Deployments
 -  Kubernetes Services
 -  LoadBalancer Service
 -  Pod Scheduling
 -  Managed Node Groups
 -  Cluster Networking
 -  Worker Nodes
 - Container Orchestration
 - Declarative Infrastructure
 - Infrastructure as Code
 - Container Image Management
 - Cloud-native Application Deployment

# Results and outcomes

The deployed infrastructure provides a secure, scalable, and highly available foundation for the
Oshawa Public Library’s digital services. Key achievements include the use of Terraform for
Infrastructure as Code, a robust Kubernetes environment on AWS, efficient container workflows
with ECR, and successful real-world testing of a Dockerized API. The architecture is
well-positioned to support future enhancements and production workloads.

●​Infrastructure as Code with Terraform​
●​Secure and scalable Kubernetes on AWS​
●​Efficient container deployment workflow with ECR​
●​High availability and multi-AZ design​
●​Real-world testing with Dockerized AP

  Successfully deployed an intermediate-level cloud-native Kubernetes platform that provides:
  
 - Automated AWS infrastructure provisioning with Terraform
 - Managed Kubernetes cluster using Amazon EKS
 - Secure container deployment with Amazon ECR
 - Private networking using Amazon VPC
 - Secure object storage integration with Amazon S3
 - Auto-scaling Kubernetes worker nodes
 - Multi-AZ high availability architecture
 - Fault-tolerant workload scheduling
 - Secure IAM-based access control
 - Public application exposure using AWS LoadBalancer
  
  The project demonstrates practical experience with deploying and managing Kubernetes workloads on AWS while applying cloud architecture principles such as security, scalability, redundancy, high availability, and Infrastructure as Code.


# Future Improvements

 - Implement CI/CD with GitHub Actions
 - Deploy applications using Helm charts
 - Integrate Amazon RDS for PostgreSQL
 - Configure AWS Load Balancer Controller or NGINX Ingress
 - Install Metrics Server
 - Deploy Prometheus and Grafana for monitoring
 - Enable Horizontal Pod Autoscaler (HPA)
 - Add centralized logging with Fluent Bit and CloudWatch
 - Implement IRSA (IAM Roles for Service Accounts) for fine-grained pod-level permissions

# Skills Demonstrated

 - Amazon EKS
 - Kubernetes
 - Terraform
 - Docker
 - Amazon EC2
 - Amazon VPC
 - Amazon ECR
 - Amazon S3
 - IAM
 - Security Groups
 - Elastic Load Balancing
 - Infrastructure as Code (IaC)
 - Cloud Networking
 - High Availability Architecture
 - Fault Tolerance
 - Auto Scaling
 - Container Orchestration
 - Cloud Security Best Practices

  
