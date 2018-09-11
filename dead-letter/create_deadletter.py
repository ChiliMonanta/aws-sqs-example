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
        VisibilityTimeout=1,
        WaitTimeSeconds=1
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        print("Received Message: ", message['MessageId'])
        print("ApproximateReceiveCount", message['Attributes']['ApproximateReceiveCount'])

def delete_message(receipt_handle):
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        'Bad message'
    )
)
print("Sent: ", response['MessageId'])

# Trigger deadletter
receive_message()
receive_message()
receive_message()