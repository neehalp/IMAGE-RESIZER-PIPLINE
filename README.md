#  Image Resizer Pipeline
## Building an Event-Driven Image Resizer Using AWS S3, SQS and Lambda : 

![image](https://user-images.githubusercontent.com/19708705/228999047-c28dfcb6-8832-4c36-82c9-0dfe0162fd0e.png)

## For step-by-step guidelines read the following article:
This project implements how to build an event-driven image processing pipeline using AWS services like S3, SQS, Lambda, and CloudWatch. It provides a step-by-step guide for creating S3 buckets, an SQS queue, configuring access policies, creating IAM policies, setting up a Lambda execution role, configuring a Lambda function, and testing the image resizing process.

Facts

📂 Step 1: Create Two S3 Buckets: Create two S3 Buckets named "media-app-initial-image" and "media-app-resized-image" with specific folder structure.

📥 Step 2: Create an SQS queue: Create an SQS queue named "media-app-queue" and edit its access policy to allow the S3 bucket to publish events to the queue.

⚙️ Step 3: SQS queue - Access Policy: Add an access policy to the SQS queue that allows the S3 bucket to publish events to the queue.

📂 Step 4: S3 Bucket (media-app-initial-image): Configure event notifications to publish events to the SQS queue when images are uploaded to the bucket.

🔒 Step 5: IAM Policies: Create three IAM policies to grant necessary permissions to the Lambda function for writing logs to CloudWatch, accessing S3 buckets, and reading the SQS queue.

🤝 Step 6: Lambda Execution Role: Create a Lambda execution role and attach the previously created IAM policies to it.

⚙️ Step 7: Configure Lambda: Create a Lambda function with the provided code and necessary configurations, including the deployment of the code and specifying the execution role.

⚡ Step 8: Test: Upload images to the initial S3 bucket and check if they are resized and saved to the resized S3 bucket. Monitor CloudWatch logs for any unexpected results.

Blog Link: https://towardsaws.com/building-an-event-driven-image-resizer-using-aws-s3-sqs-and-lambda-894ff455e12
