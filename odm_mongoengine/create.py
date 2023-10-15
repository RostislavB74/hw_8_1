from models import Authors, Quotes

if __name__ == '__main__':
    # writer1 = Authors(fullname='Alex Pushkin', born_date='June 6, 1799',
    #                   born_location='St.Petesburg', description='poet').save()

    # writer2 = Authors(fullname='Petrov', born_date='June 6, 1899',
    #                   born_location='Kyiv', description='art').save()
    links3 = Quotes(tags=['test6', 'test7'], author=Authors(id='652c27039fc5538277d326b5'),
                    quota='проверка').save()
