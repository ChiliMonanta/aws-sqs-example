SQS Examples
============

A Small example of Amazon SQS

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.

Some highlights from documentation...

Standard queue
--------------

Standard queues support a nearly unlimited number of transactions per second (TPS) per action. Standard queues support at-least-once message delivery. It's possible that more than one copy of a message might be delivered out of order

FIFO queue
----------

By default, FIFO queues support up to 3,000 messages per second with batching. To request a limit increase, file a support request.
FIFO queues support up to 300 messages per second (300 send, receive, or delete operations per second) without batching. To avoid that the same message is sent twice there is something called Message Deduplication ID (sqs has a minimum deduplication interval of 5 minutes).

Within a fifo queue you can use message groups. When messages that belong to a particular message group ID are invisible, no other consumer can process messages with the same message group ID.

Delay queue
-----------
Delay queues let you postpone the delivery of new messages to a queue for a number of seconds (max 15 minutes). 

Dead-Letter queue
-----------------
Amazon SQS supports dead-letter queues, which other queues (source queues) can target for messages that can't be processed (consumed) successfully. 

Pricing
-------

Standard Queue $0.40 per 1 Million Requests ($0.00000040 per request)

FIFO Queue $0.50 per 1 Million Requests ($0.00000050 per request)

Every Amazon SQS action counts as a request.
Some additional pricing exists, see [pricing](https://aws.amazon.com/sqs/pricing/).

To organize and identify your Amazon SQS queues for cost allocation, you can add metadata tags that identify a queue's purpose, owner, or environment.

Long polling helps reduce the cost of using Amazon SQS by eliminating the number of empty responses (when there are no messages available for a ReceiveMessage request) and false empty responses (when messages are available but aren't included in a response).

To reduce costs or manipulate up to 10 messages with a single batch command.

Requirements
------------

	sudo apt install python3 python3-venv python3-pip

Setup Environment for each example

	python3 -m venv env
	source env/bin/activate
	pip3 install -r requirement.txt
	terraform init
	terraform plan
	terraform output -json > outputs.json

Run

	python3 send.py
	python3 receive.py


Links
-----

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
https://www.terraform.io/docs/providers/aws/r/sqs_queue.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html
