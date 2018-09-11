provider "aws" {
  region  = "eu-west-1"
  profile = "my-aws"
}

resource "aws_sqs_queue" "terraform_queue_deadletter" {
  name                      = "terraform-example-deadletter-queue"
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10

  tags {
    Environment = "example-deadletter"
  }
}

resource "aws_sqs_queue" "terraform_queue" {
  name                      = "terraform-example-queue"
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  redrive_policy            = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.terraform_queue_deadletter.arn}\",\"maxReceiveCount\":2}"

  tags {
    Environment = "example-deadletter"
  }
}

resource "local_file" "queue_uri" {
  content  = "${aws_sqs_queue.terraform_queue.id}"
  filename = "${path.module}/uri.txt"
}

output "uri_queue" {
  description = "The URL for the created Amazon SQS queue"
  value       = "${aws_sqs_queue.terraform_queue.id}"
}

resource "local_file" "deadletter_uri" {
  content  = "${aws_sqs_queue.terraform_queue_deadletter.id}"
  filename = "${path.module}/uri_deadletter.txt"
}

output "uri_deadletter" {
  description = "The URL for the created Amazon SQS queue"
  value       = "${aws_sqs_queue.terraform_queue_deadletter.id}"
}