from mongoengine import Document
from mongoengine import StringField, ListField, ReferenceField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quotes = StringField()
