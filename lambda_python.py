import boto3
import json

def lambda_handler(event, context):
    
    # Create an SQS client
    sqs = boto3.client('sqs')
    
    # Get the URL of the SQS queue
    queue_url = sqs.get_queue_url(QueueName='CustomerOrders')['QueueUrl']
    
    # Receive a message from the SQS queue
    response = sqs.receive_message(QueueUrl=queue_url, AttributeNames=['All'], MaxNumberOfMessages=1)
    
    # Check if there are any messages
    if 'Messages' not in response:
        return {
            'statusCode': 200,
            'body': 'No messages in the queue'
        }
    
    # Get the message
    message = response['Messages'][0]
    
    # Convert the message body from a string to a dictionary
    message_body = message['Body']
    message_dict = json.loads(message_body)
    
    # Send a message to the SNS topic
    sns = boto3.client('sns')
    
    # Create an SNS topic if it doesn't exist
    topic_name = 'Orders'
    topics = sns.list_topics()['Topics']
    topic_arn = None
    for t in topics:
        if t['TopicArn'].endswith(':' + topic_name):
            topic_arn = t['TopicArn']
            break
    if topic_arn is None:
        topic_arn = sns.create_topic(Name=topic_name)['TopicArn']
    
    sns.publish(TopicArn=topic_arn, Message=json.dumps(message_dict))
    
    # Delete the message from the SQS queue
    receipt_handle = message['ReceiptHandle']
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    
    return {
        'statusCode': 200,
        'body': 'Successfully submitted a customer order to fufillment'
    }
