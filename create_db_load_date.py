import json
import os
import shutil
from pymongo import MongoClient
from pymongo.server_api import ServerApi

input_directory = 'input'
arch_directory = 'arch'


def create_db_load_date(name_db):
    # name_db = 'hw8'

    uri = f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}?retryWrites=true&w=majority"

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[name_db]

    for file in os.listdir(input_directory):
        if file.endswith(".json"):
            collection_name = file.split('.')[0]
            collection = db[collection_name]

            with open(os.path.join(input_directory, file)) as f:
                file_data = json.load(f)
                collection.insert_many(file_data)
                print(file)
            shutil.move(f'input/{file}', f'arch/{file}')

    client.close()
    return 'OK'


if __name__ == '__main__':
    create_db_load_date("")
