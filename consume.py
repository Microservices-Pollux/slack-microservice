import pika
import os
from dotenv import load_dotenv
load_dotenv()


def consume():
    url = os.environ['CLOUDAMQP_URL']
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()  # start a channel
    channel.queue_declare(queue='hello')  # Declare a queue

    def callback(ch, method, properties, body):
        print(" [x] Received " + str(body))
    channel.basic_consume('hello',
                          callback,
                          auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
    connection.close()
