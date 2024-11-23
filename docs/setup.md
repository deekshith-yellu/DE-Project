# Project Setup Guide

## Prerequisites
1. AWS Account
2. Python 3.11
3. AWS CLI
4. Git

## Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/deekshith-yellu/DE-Project.git
cd DE-Project
```

### 2. Python Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. AWS Configuration
#### IAM User Setup
1. Create IAM User
2. Enable MFA
3. Configure AWS CLI
```bash
aws configure
```

#### S3 Buckets
1. Create raw data bucket:
   - Name: dev-ecommerce-raw-data-us-east-2
   - Region: us-east-2

2. Create processed data bucket:
   - Name: dev-ecommerce-processed-data-us-east-2
   - Region: us-east-2

### 4. Lambda Function Setup
1. Create Lambda function:
   - Name: dev-ecommerce-data-generator
   - Runtime: Python 3.11
   - Handler: generator.lambda_handler

2. Add Layers:
   - AWS SDK Pandas Layer

3. Configure IAM Roles:
   - S3 access
   - CloudWatch logs
   - Basic Lambda execution

## Testing
1. Test Lambda Function:
   - Use test event
   - Verify S3 uploads
   - Check CloudWatch logs

## Monitoring Setup
1. CloudWatch:
   - Enable detailed monitoring
   - Set up log groups
   - Configure metrics

## Troubleshooting
Common issues and solutions will be added as encountered.