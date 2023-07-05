import pika
from models import User
from connection import connect
from mongoengine import ObjectIdField
def main():
    cred =pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection\
        (pika.ConnectionParameters(host='localhost', port =5672, credentials=cred))
    channel = connection.channel()

    channel.queue_declare(queue='return_true')

    def callback(ch, method, properties, body):
        id = body.decode()
        user =User.objects(id = id).first()
        def send_email(user):
            email = user.email
            print(f'I sent email to {email}')
        send_email(user)
        user.update(get_email = True)


    channel.basic_consume(queue = 'hello_world', on_message_callback= callback,  auto_ack= True)

    channel.start_consuming()


if __name__ == '__main__':
    main()