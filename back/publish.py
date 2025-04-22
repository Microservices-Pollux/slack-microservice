# publish.py
import pika
import os
import json
from dotenv import load_dotenv
load_dotenv()

body = {
    "slackChannel": "#test",
    "text": "Hello World!",
    "blocks": {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Hello World!*"
        }
    }
}

def publish():
    url = os.environ['CLOUDAMQP_URL']
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='slack_msg', durable=True)  # Declare a queue
    channel.basic_publish(exchange='',
                          routing_key='slack_msg',
                          body=json.dumps(body).encode()),

    print(" [x] Sent 'Hello World!'")
    connection.close()

publish()