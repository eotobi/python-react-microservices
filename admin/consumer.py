import pika

params = pika.URLParameters(
    "amqps://yvdukkkv:Iu6peDrSD_02NMekO89uLtK5KBNH7s3p@shrimp.rmq.cloudamqp.com/yvdukkkv"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received a message")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
