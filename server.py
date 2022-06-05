from flask import Flask
import pika


app = Flask(__name__)


@app.route('/')
def hello():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    i = 100
    while i > 90:
        channel.basic_publish(exchange='', routing_key='hello', body=f'Hello a new message here RabbitMQ! {i}')
        i -= 1

    print(" [x] Sent 'Hello a new message here RabbitMQ!'")

    connection.close()
    return "Hello from publisher values published"