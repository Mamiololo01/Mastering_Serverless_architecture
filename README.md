# Mastering_Serverless_architecture

How to Chain Lambda Functions in AWS for High-Performance Applications using SNS, SQS, DynamoDB &amp; two Lambda additional Lambda functions.

In a previous article, I showed you how to create a serverlesss architecture using an API, Lambda Python function, and an SQS messaging queue. This combination of AWS was created with this business case in mind:

Suppose your company is running a high-traffic e-commerce website that receives a large number of orders each day. To process these orders efficiently, the company can set up an API Gateway to receive incoming order requests from the website’s front-end. The API Gateway can then trigger a Lambda function, which can use the information from the order requests to create a new SQS queue.

The SQS queue can act as a buffer between the website’s front-end and the back-end processing system, allowing the company to process orders in batches and avoid overwhelming the back-end system. The Lambda function can also be configured to send notifications to relevant stakeholders when a new queue is created or when new orders are added to the queue.

Our previous architecture ended with our SQS queue, but suppose we wanted to extend this further. Suppose we wanted to keep our customers informed of the process of their order.

This is where the power of serverless architectures come into play. We can continue to build out additional functions and services to provide better efficiency in our operations and customer service for our consumers with the help of additional DevOps automation.

To keep stakeholders informed of the order processing progress, our SQS queue can be monitored by a separate Lambda function, which can be configured to trigger an SNS topic to notify stakeholders when there are updates to the order processing status.

When the SNS topic is triggered, it can call another Lambda function, which can extract the relevant information from the SNS message and store it in a DynamoDB table. The Lambda function can add a timestamp to the record to indicate when the message was posted and generate a unique identifier for each record to facilitate easy search and retrieval.

This data can be used by the company to analyze the order processing performance and identify areas for improvement.

In this article, we are going to continue to build our a more robust serverless architecture using SNS, SQS, DynamoDB & two Lambda additional Lambda functions.

Let’s jump right in!

Prerequisites
Understanding of AWS services, especially API Gateway, Lambda, SQS, SNS, and DynamoDB
Experience with coding in Python
Familiarity with event-driven architectures
Knowledge of NoSQL databases
Understanding of serverless architecture principles
