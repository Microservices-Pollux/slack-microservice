from app import app
import awsgi

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})