import json
import boto3
from io import BytesIO
from PIL import Image

client = boto3.client('s3')
#source_bucket = "media-app-initial-image"
destination_bucket = "media-app-resized-image"
exclude_keys = {'cover/', 'post/', 'profile/'}

# Custom Image Size
image_sizes = {
    'cover': (820, 360),
    'profile': (170, 170),
    'post': (1080, 1080)
}

def resizer(img, key):
    image_type = key.split("/")[0]
    if image_type in image_sizes:
        resized_image = img.resize(image_sizes[image_type])
        temp_buffer = BytesIO()
        resized_image.save(temp_buffer,format=img.format)
        resized_bytes = temp_buffer.getvalue()
        client.put_object(Body=resized_bytes, Bucket=destination_bucket, Key=key)

def download_image(bucket_name, key):
    response = client.get_object(Bucket=bucket_name, Key=key)
    return response['Body'].read()

def lambda_handler(event, context):
    print(event)
    try:
        
        for item in event['Records']:
            
            s3_event = json.loads(item['body'])
            
            if 'Event' in s3_event and s3_event['Event'] == 's3:TestEvent':
                print("Test Event")
                
            else:
                for item in s3_event['Records']:
                    source_bucket = item['s3']['bucket']['name']
                    key = item['s3']['object']['key']
                    print(key)
                    
                    if key not in exclude_keys:
                        image_content = download_image(source_bucket, key)
                        with Image.open(BytesIO(image_content)) as img:
                            img.format
                            resizer(img, key)
                        
    except Exception as exception:
        print(exception)
