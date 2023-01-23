import boto3
import os
from decouple import config

bucket = config('AWS_STORAGE_BUCKET_NAME')
s3 = boto3.resource('s3')

client = boto3.client('s3',
                    aws_access_key_id=config('AWS_S3_ACCESS_KEY_ID'),
                    aws_secret_access_key=config('AWS_S3_SECRET_ACCESS_KEY'))

class S3Utils:
    def get_video(self, videoPath):
        key = videoPath
        file_byte_string = client.get_object(Bucket=bucket, Key=str(key))['Body'].read()
        video = file_byte_string
        
        return video
