import json
import boto3
import random
from datetime import datetime, timedelta
import pandas as pd
import io

def generate_customer_data(num_records=100):
    """Generate sample customer data"""
    customers = []
    for i in range(num_records):
        customer = {
            'customer_id': f'CUST_{str(random.randint(1000, 9999))}',
            'name': f'Customer {i}',
            'email': f'customer{i}@example.com',
            'registration_date': (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
        }
        customers.append(customer)
    return customers

def generate_product_data(num_products=50):
    """Generate sample product data"""
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
    products = []
    for i in range(num_products):
        product = {
            'product_id': f'PROD_{str(random.randint(1000, 9999))}',
            'name': f'Product {i}',
            'category': random.choice(categories),
            'price': round(random.uniform(10, 1000), 2),
            'stock': random.randint(0, 1000)
        }
        products.append(product)
    return products

def generate_transaction_data(customers, products, num_transactions=200):
    """Generate sample transaction data"""
    transactions = []
    for i in range(num_transactions):
        customer = random.choice(customers)
        product = random.choice(products)
        transaction = {
            'transaction_id': f'TXN_{str(random.randint(10000, 99999))}',
            'customer_id': customer['customer_id'],
            'product_id': product['product_id'],
            'quantity': random.randint(1, 5),
            'amount': round(random.randint(1, 5), 2),
            'transaction_date': (datetime.now() - timedelta(hours=random.randint(1, 24))).isoformat()
        }
        transactions.append(transaction)
    return transactions

def upload_to_s3(data, bucket, folder, timestamp):
    """Upload data to S3"""
    s3 = boto3.client('s3')
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Convert to CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    # Upload to S3
    s3.put_object(
        Bucket=bucket,
        Key=f'{folder}/data_{timestamp}.csv',
        Body=csv_buffer.getvalue()
    )

def lambda_handler(event, context):
    try:
        # Generate timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Set bucket name
        bucket_name = 'dev-ecommerce-raw-data-us-east-2'
        
        # Generate data
        customers = generate_customer_data()
        products = generate_product_data()
        transactions = generate_transaction_data(customers, products)
        
        # Upload each dataset to S3
        upload_to_s3(customers, bucket_name, 'customers', timestamp)
        upload_to_s3(products, bucket_name, 'products', timestamp)
        upload_to_s3(transactions, bucket_name, 'transactions', timestamp)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully generated and uploaded data. Timestamp: {timestamp}')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error generating data: {str(e)}')
        }