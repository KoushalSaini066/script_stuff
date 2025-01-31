import boto3
import json
import os
from botocore.exceptions import ClientError

# Editable variables
BUCKET_NAME = "bucketname"
FOLDER_NAME = "foldername"
REGION = "ap-south-X"
STAGE_NAME = "prod"

def export_apis_to_s3(region, bucket_name, folder_name, stage_name='prod'):
    try:
        # Initialize clients
        apigateway_client = boto3.client('apigateway', region_name=region)
        s3_client = boto3.client('s3', region_name=region)

        # Fetch all APIs
        apis = apigateway_client.get_rest_apis()

        for api in apis.get('items', []):
            api_id = api['id']
            api_name = api['name']

            print(f"Exporting API: {api_name} (ID: {api_id})")

            # Export the API
            export_response = apigateway_client.get_export(
                restApiId=api_id,
                stageName=stage_name,
                exportType='swagger',
                accepts='application/json',
                parameters={
                    'extensions': 'integrations'
                }
            )

            # Generate file path
            file_name = f"{folder_name}/{api_name}_{api_id}.json"
            temp_file_path = f"/tmp/{api_name}_{api_id}.json"

            # Save export to a temporary file
            with open(temp_file_path, 'wb') as f:
                f.write(export_response['body'].read())

            # Upload to S3
            s3_client.upload_file(temp_file_path, bucket_name, file_name)

            print(f"Uploaded {api_name} to s3://{bucket_name}/{file_name}")

            # Clean up temporary file
            os.remove(temp_file_path)

    except ClientError as e:
        print(f"AWS ClientError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    export_apis_to_s3(REGION, BUCKET_NAME, FOLDER_NAME, STAGE_NAME)
