from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/hw81?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi("1"))

db = client.hw_8_1

if __name__ == "__main__":
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")

        results = db.author.find()
        for r in results:
            print(r)
    except Exception as e:
        print(e)
