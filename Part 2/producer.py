import pika
from models import User
from faker import Faker

fake = Faker('uk-UA')


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='return_true')

    def seed():
        for i in range(5):
            create = User(fullname=fake.name(), email=fake.email()).save()

    def send_user_id():
        users = User.objects()
        for user in users:
            id = user.id
            channel.basic_publish(exchange='', routing_key='hello_world', body=f'{id}'.encode())
    seed()
    send_user_id()
    print('END')
    connection.close()


if __name__ == '__main__':
    main()