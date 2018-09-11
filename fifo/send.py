import time
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Get uri from terraform
with open('uri.txt') as f:
    queue_url = f.readline()

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageGroupId='1',
    MessageDeduplicationId=str(int(time.time())+1),
    MessageBody=(
        '#1 This is MessageGroupId 1'
    )
)

print(response['MessageId'])

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageGroupId='1',
    MessageDeduplicationId=str(int(time.time())+2),
    MessageBody=(
        '#2 This is MessageGroupId 1'
    )
)

print(response['MessageId'])

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageGroupId='2',
    MessageDeduplicationId=str(int(time.time())+3),
    MessageBody=(
        '#3 This is MessageGroupId 2'
    )
)

print(response['MessageId'])