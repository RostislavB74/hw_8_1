from mongoengine import connect
from mongoengine import Document, StringField, ListField, CASCADE, ReferenceField, DateTimeField

connect(
    host=f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/proverka", ssl=True)


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField(max_length=50)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quota = StringField()


# class TextQuotes(Quotes):
#     content = StringField()


# class ImageQuotes(Quotes):
#     image_path = StringField()


# class LinkQuotes(Quotes):
#     link_url = StringField()


def models_db(name_db):
    connect(
        host=f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}", ssl=True)
    """uri = f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}?retryWrites=true&w=majority"

        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client[name_db]"""


if __name__ == '__main__':
    models_db()
