import json
# from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

name_db = 'hw8'
uri = f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.hw8
# client = MongoClient('localhost', 27017)
# db = client['test']
collection_authors = db['test']

with open('input\\authors.json') as f:
    file_data = json.load(f)

    # if pymongo < 3.0, use insert()
    # collection_authors.insert(file_data)
    # if pymongo >= 3.0 use insert_one() for inserting one document
    # collection_authors.insert_one(file_data)
    # if pymongo >= 3.0 use insert_many() for inserting many documents
    collection_authors.insert_many(file_data)

    client.close()
