import mongoengine
from models import Quotes
from connection import connect
from pprint import pprint

def search_tag(tag):
    db_result = Quotes.objects()
    result_list = []
    for db_res in db_result:
        if tag in db_res.tags:
            result_list.append((db_res.quotes))
    for i in result_list:
        pprint(i)

def search_tags(tags):
    db_result = Quotes.objects()
    result_list = []
    for tag in tags:
        for db_res in db_result:
            if tag in db_res.tags:
                result_list.append((db_res.quotes))
    for i in result_list:
        pprint(i)


def search_author(name):
    db_result = Quotes.objects()
    result =[]
    for db_res in db_result:
        if name == db_res.author.fullname:
            result.append(db_res.quotes)
    for i in result:
        pprint(i)

def main():
    while True:
        user_search = input('>>> ')
        if user_search.startswith('name'):
            user_search = user_search.replace('name:', '')
            user_search = user_search.lstrip(' ')
            search_author(user_search)
        elif user_search.startswith('tags'):
            user_search = user_search.replace('tags:', '')
            user_search = user_search.split(',')
            print(user_search)
            search_tags(user_search)
        elif user_search.startswith('tag'):
            user_search = user_search.replace('tag:', '')
            user_search = user_search.lstrip(' ')
            search_tag(user_search)
        elif user_search.startswith('exit'):
            break
        else:
            print("Unknown command")

if __name__ == '__main__':
    main()

