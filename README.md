# Data Engineering Project (E-commerce Analytics)

## Architecture Overview
This project implements a six-layer data engineering architecture:
1. SOURCE-HUB (Data Sources)
2. INGEST-ENGINE (Data Ingestion)
3. DATA-FACTORY (Processing)
4. DATA-VAULT (Storage)
5. INSIGHT-HUB (Analytics)
6. WATCH-TOWER (Monitoring)

## Current Status
- ✅ Project Setup
- ✅ AWS IAM Configuration
- ✅ S3 Buckets Creation
- ✅ Lambda Function Implementation
- 🔄 EventBridge Setup (In Progress)

## Resources Created
### AWS Resources
- S3 Buckets:
  - dev-ecommerce-raw-data-us-east-2
  - dev-ecommerce-processed-data-us-east-2
- Lambda Function: dev-ecommerce-data-generator
- Lambda Layer: AWS SDK Pandas Layer

## Setup Instructions
Detailed setup instructions can be found in [docs/setup.md](docs/setup.md)

## Progress Tracking
Current implementation progress is documented in [docs/progress.md](docs/progress.md)

## Next Steps
1. Complete EventBridge setup
2. Implement CloudWatch monitoring
3. Begin data processing pipeline