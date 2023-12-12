import pika, json
from main import Product,db


params = pika.URLParameters(
    "amqps://yvdukkkv:Iu6peDrSD_02NMekO89uLtK5KBNH7s3p@shrimp.rmq.cloudamqp.com/yvdukkkv"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("Received a message in main")
    data = json.dumps(body)
    print(data)

    if properties.content_type == "product created":
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print("Product Created")

    elif properties.content_type == "product updated":
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print("Product Updated")

    elif properties.content_type == "product deteted":
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("Product Deleted")

channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
