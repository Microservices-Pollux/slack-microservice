# publish.py
import pika
import os
from dotenv import load_dotenv
load_dotenv()


def publish():
    url = os.environ['CLOUDAMQP_URL']
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='hello', durable=True)  # Declare a queue
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello CloudAMQP!')

    print(" [x] Sent 'Hello World!'")
    connection.close()
