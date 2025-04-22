import pika
import os
import json
from slack_sdk import WebClient
from dotenv import load_dotenv
load_dotenv()

bot_token = os.environ["BOT_TOKEN"]
client = WebClient(token=bot_token)


def consume():
    url = os.environ['CLOUDAMQP_URL']
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='slack_msg', durable=True)  # Declare a queue

    def callback(ch, method, properties, body):
        body = json.loads(body.decode())
        slackChannel = body["slackChannel"]
        text = body["text"]
        blocks = body["blocks"]
        client.chat_postMessage(
            channel=slackChannel,
            text=text,
            blocks=[blocks]
        )

    channel.basic_consume('slack_msg',
                          callback,
                          auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
    connection.close()


consume()
