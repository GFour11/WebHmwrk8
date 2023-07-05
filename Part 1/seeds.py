import json
import mongoengine
from models import Author, Quotes
from connection import connect


with open('authors.json', "r", encoding='utf-8') as fh:
    unpacked = json.load(fh)
    for author in unpacked:
        Author(fullname=author['fullname'], born_date=author['born_date'], born_location=author['born_location'],
               description=author['description']).save()


with open('qoutes.json', "r", encoding='utf-8') as fh:
    unpacked = json.load(fh)
    for res in unpacked:
        for author in Author.objects():
            if author.fullname == res['author']:
                Quotes(tags=res['tags'], author=author, quotes=res['quote']).save()
