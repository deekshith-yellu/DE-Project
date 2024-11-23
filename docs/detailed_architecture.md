# E-commerce Analytics Platform - Detailed Architecture

## Architecture Diagram

```mermaid
flowchart TB
    subgraph Layer1["1. SOURCE-HUB"]
        SFTP["SFTP Server"]
        MySQL[(MySQL DB)]
        MongoDB[(MongoDB)]
        APIs[REST APIs]
    end

    subgraph Layer2["2. INGEST-ENGINE"]
        ELB["Elastic Load Balancer"]
        CF["CloudFront"]
        Lambda["AWS Lambda"]
        ECS["ECS Containers"]
    end

    subgraph Layer3["3. DATA-FACTORY"]
        subgraph ETL["ETL Processing"]
            Glue["AWS Glue"]
            Info["Informatica"]
            Step["Step Functions"]
        end
        
        subgraph BigData["Big Data"]
            EMR["EMR Cluster"]
            Hadoop["Hadoop"]
            Hive["Hive"]
            Pig["Pig"]
        end
        
        subgraph SparkProcess["Spark Processing"]
            PySpark["PySpark"]
            SparkRDD["Spark RDD"]
            Databricks["Databricks"]
        end
    end

    subgraph Layer4["4. DATA-VAULT"]
        S3["S3 Data Lake"]
        Lake["Lake Formation"]
        
        subgraph DataWH["Data Warehouses"]
            Snow[(Snowflake)]
            Redshift[(Redshift)]
        end
        
        DDB[(DynamoDB)]
    end

    subgraph Layer5["5. INSIGHT-HUB"]
        QS["QuickSight"]
        PBI["Power BI"]
        MPL["Matplotlib"]
    end

    subgraph Layer6["6. WATCH-TOWER"]
        CW["CloudWatch"]
        CFM["CloudFormation"]
        EC2M["EC2 Monitoring"]
    end

    Layer1 --> Layer2
    Layer2 --> Layer3
    Layer3 --> Layer4
    Layer4 --> Layer5
    Layer6 -.-> Layer2
    Layer6 -.-> Layer3
    Layer6 -.-> Layer4
```

## Layer Details

### 1. SOURCE-HUB (Data Sources)
- Purpose: Data ingestion from multiple sources
- Components:
  - SFTP Server: File transfers
  - MySQL DB: Transactional data
  - MongoDB: NoSQL data
  - REST APIs: Real-time data

### 2. INGEST-ENGINE (Data Ingestion)
- Purpose: Data collection and initial processing
- Components:
  - Elastic Load Balancer: Traffic distribution
  - CloudFront: Content delivery
  - AWS Lambda: Serverless processing
  - ECS Containers: Containerized services

[Continue with detailed descriptions of other layers...]