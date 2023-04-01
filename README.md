# Mastering_Serverless_architecture

How to Chain Lambda Functions in AWS for High-Performance Applications using SNS, SQS, DynamoDB &amp; two Lambda additional Lambda functions.

<img width="674" alt="Screenshot 2023-04-01 at 20 13 06" src="https://user-images.githubusercontent.com/67044030/229309939-509250ec-a7ab-4713-87ef-7a1d50c298a7.png">

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

Step 1: Creating our Lambda Function

Per our use-case, our Lambda will need to be triggered by the creation of an SQS queue message. We already set up that SQS queue in our previous article therefore, we will not go in-depth here on how to set up an SQS queue.

This Lambda will then need to publish the received SQS message to an SNS topic, which should notify our in-house fulfillment of a new customer order for processing.

From our Lambda console, we click, “Create Function”. We give our function a name, select Python 3.9, the default architecture, and click “Create Function”.

<img width="1249" alt="Screenshot 2023-04-01 at 19 13 39" src="https://user-images.githubusercontent.com/67044030/229309991-830ac584-6fd8-4e37-b5ca-25d28ebae4f6.png">

<img width="1240" alt="Screenshot 2023-04-01 at 19 14 25" src="https://user-images.githubusercontent.com/67044030/229310028-fc649b51-7e7d-455c-8353-ae1537df92be.png">

Next, we need to edit the permissions of our Lambda so that it can access both the SQS queue and write to our SNS topic. Within our function dashboard, we click the “Configuration” sub-menu, “Permissions”, and click our “Execution Role” to be re-directed to IAM to add the needed policies to our function.

The permission policies we will need for our use-case are “SNSFullAccess” and “SQSFullAccess”.

Now we head back to our Lambda console and copy our python script above into our code and click “Deploy”.

Next, we need to configure our test event to ensure our lambda is working properly. Below is a JSON of our test event that mimics an SQS event to trigger our Lambda function:

Again, from our Lambda function dashboard, we click, “Configure test event”.

We give our test event a name. For our use-case, we will make it private and paste in our JSON test event from above. Click “Save”.

Now with our Lambda function coded, configured with the proper permissions, and our test event ready, we click “Test” to test our Lambda.

We recieve a “200” success status code and a message informing us that our customer order has been sent to an SNS topic for fufillment.

We can verify that our Lambda processed the message in our SQS queue and submitted the information via a message to our SNS topic by visiting our SNS dashboard

Our fulfillment team has a subscription to messages that are sent to our “Order” topic in SNS and are notified via email when a new message is posted.

We can check our company email to ensure that our SNS topic was configured correctly by Lambda by checking an email that was subscribed to the SNS topic:

Step 2: Create A Lambda that Time Stamps SNS Messages and Stores it in a DynamoDB Table
Once again, we head to the Lambda dashboard to create our function


As in our previous Lambdas, we need to give our function the correct permissions to pull messages from our SNS topic and to create DynamoDB tables

We need to configure our test event. Below is a JSON for our test event


We configure the event in the same way with our previous Lambda

This Lambda function is triggered by an SNS topic and extracts relevant information from the SNS message, which is then stored in a DynamoDB table.

The function generates a unique identifier for each record, adds a timestamp to indicate when the message was posted, and converts the timestamp from epoch time to human-readable format.

We can paste our code into our Lambda function, click “Deploy” and run our test event:

We receive a successful result:


We can then verify the results by visiting our DynamoDB Dashboard


Step 4: Test and Verify our Entire Serverless Application
Starting in the API gateway, we once again test our API to see our application run from start all the way through. We run one more test in our API


And confirm that an SQS queue was created


And confirm that our SNS is triggering by seeing if we received an email


Finally, we check our DynamoDB Table one last time to see the timestamp and log of our orders


