import json

from models import Authors, Quotes


if __name__ == '__main__':
    with open("arch/authors.json", "r", encoding="utf-8") as af:
        authors_date = json.load(af)

    with open("arch/quotes.json", "r", encoding="utf-8") as qf:
        quotes_date = json.load(qf)

    for author_date in authors_date:
        author = Authors(**author_date)
        author.save()

    for quote_date in quotes_date:
        author_fullname = quote_date['author']
        author = Authors.objects(fullname=author_fullname).first()

        del quote_date['author']

        quote = Quotes(**quote_date, author=author)
        quote.save()
