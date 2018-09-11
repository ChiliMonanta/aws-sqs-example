provider "aws" {
  region  = "eu-west-1"
  profile = "my-aws"
}

resource "aws_sqs_queue" "terraform_queue" {
  name                        = "terraform-example-queue.fifo"
  fifo_queue                  = true
  content_based_deduplication = true
  visibility_timeout_seconds  = 10

  tags {
    Environment = "example-fifo"
  }
}

resource "local_file" "queue_uri" {
  content  = "${aws_sqs_queue.terraform_queue.id}"
  filename = "${path.module}/uri.txt"
}

output "uri" {
  description = "The URL for the created Amazon SQS queue"
  value       = "${aws_sqs_queue.terraform_queue.id}"
}
