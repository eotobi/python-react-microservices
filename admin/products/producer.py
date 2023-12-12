import pika, json

params = pika.URLParameters("amqps://yvdukkkv:Iu6peDrSD_02NMekO89uLtK5KBNH7s3p@shrimp.rmq.cloudamqp.com/yvdukkkv")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
