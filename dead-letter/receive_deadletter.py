import json
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Get uri from terraform
with open('uri_deadletter.txt') as f:
    queue_url = f.readline()

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'All'
    ],
    MaxNumberOfMessages=1,
    VisibilityTimeout=1,
    WaitTimeSeconds=1
)

msg = response['Messages'][0]

print("Received Message:")
print(json.dumps(msg, indent=4, sort_keys=True))

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=msg['ReceiptHandle']
)
