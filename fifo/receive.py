import json
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Get uri from terraform
with open('uri.txt') as f:
    queue_url = f.readline()

def receive_message():
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=1,
        VisibilityTimeout=10,
        WaitTimeSeconds=10
    )

    message = response['Messages'][0]

    print("Received Message:")
    print(json.dumps(message, indent=4, sort_keys=True))
    return message['ReceiptHandle']

def delete_message(receipt_handle):
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

msg1 = receive_message()    # MessageGroupId 1
msg2 = receive_message()    # MessageGroupId 2
delete_message(msg1)
delete_message(msg2)
msg3 = receive_message()    # MessageGroupId 1
delete_message(msg3)
