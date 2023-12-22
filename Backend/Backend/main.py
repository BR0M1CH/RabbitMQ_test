import pika
import time

print('start COSUMENTO')
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('guest', 'guest'))
    )
channel = connection.channel()
channel.queue_declare(queue='testqueue', durable=True)

def process_order(ch, method, properties, body):
    # Здесь происходит обработка заказа
    with open('log.txt', 'a', encoding='utf-8') as log:
        log.write(str(body))
    # Подтверждение обработки заказа
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='testqueue', on_message_callback=process_order)

if __name__ == '__main__':
    print('START CONSUME')
    channel.start_consuming()
    connection.close()