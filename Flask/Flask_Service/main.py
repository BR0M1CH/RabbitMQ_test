from flask import Flask, request
import pika
import time
app = Flask(__name__)



time.sleep(10)
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('guest', 'guest'))
    )
channel = connection.channel()
channel.queue_declare(queue='testqueue', durable=True)


@app.route('/test')
def test():
    channel.basic_publish(
    exchange='',
    routing_key='testqueue',
    body='test message',
    properties=pika.BasicProperties(
        delivery_mode=2,  # Для сохранения сообщений даже при перезапуске брокера
        )
    )
    return('Sended: test message')

@app.route('/')
def page():
    return('Hello, world!')

if __name__ == '__main__':
    print('START FLASK')
    app.run(debug=True, host='0.0.0.0', port=5000)