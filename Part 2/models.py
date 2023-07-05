from mongoengine import Document, StringField, BooleanField
from connection import connect


class User(Document):
    fullname = StringField()
    email = StringField()
    get_email = BooleanField(default=False)


