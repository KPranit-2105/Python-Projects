# AWS SDK Wrapper Integration with Product Backend

## Overview
This project integrates an AWS SDK Wrapper with a product backend using Python, Flask, AWS, and Boto3. The Flask application allows interaction with AWS services such as S3, DynamoDB, and Lambda.

## Features
- Upload files to AWS S3
- Retrieve items from DynamoDB
- Invoke AWS Lambda functions

## Prerequisites
- Python 3.8+
- AWS CLI configured with credentials
- Flask & Boto3 installed

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/aws-sdk-wrapper.git
   cd aws-sdk-wrapper
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Ensure AWS credentials are configured:
```bash
aws configure
```
Alternatively, add credentials to `~/.aws/credentials`:
```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = YOUR_AWS_REGION
```

## Running the Application
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Upload File to S3
**Endpoint:** `/upload`  
**Method:** `POST`
**Request:**
```json
{
  "file": "<file>",
  "bucket_name": "your-bucket"
}
```
**Response:**
```json
{
  "message": "File uploaded successfully!"
}
```

### Retrieve Item from DynamoDB
**Endpoint:** `/get-item`  
**Method:** `GET`
**Request:**
```json
{
  "table_name": "your-table",
  "id": "item-id"
}
```
**Response:**
```json
{
  "id": "item-id",
  "name": "Item Name"
}
```

### Invoke AWS Lambda
**Endpoint:** `/invoke-lambda`  
**Method:** `POST`
**Request:**
```json
{
  "function_name": "your-lambda-function",
  "payload": "{}"
}
```
**Response:**
```json
{
  "result": "Lambda response"
}
```

## Deployment (Optional)
You can deploy this Flask app on AWS Lambda, EC2, or Fargate for production use.

## License
MIT License

## Author 
Pranit P. Kolamkar

