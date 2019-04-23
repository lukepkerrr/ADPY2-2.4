import csv
import re
import datetime

from pymongo import MongoClient

client = MongoClient()
concerts_db = client.concerts_db


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        data = []
        reader = csv.DictReader(csvfile)
        for line in reader:
            date = line['Дата'].split('.')
            data.append({
                'artist': line['Исполнитель'],
                'price': int(line['Цена']),
                'place': line['Место'],
                'date': datetime.datetime(year=2019, month=int(date[1]), day=int(date[0]))
            })
        db.concerts.insert_many(data)



def find_cheapest(db):
    """
    Найти самые дешевые билеты
    Документация: https://docs.mongodb.com/manual/reference/operator/aggregation/sort/
    """
    concerts_by_price = db.concerts.find().sort('price', 1)
    for concert in concerts_by_price:
        print(concert)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и выведите их по возрастанию цены
    """

    regex = re.compile('.*{}.*'.format(re.escape(name)))

    concerts_by_name = db.concerts.find({'artist': regex}).sort('price', 1)
    for concert in concerts_by_name:
        print(concert)


def find_by_date(start, end, db):
    start_date = start.split('.')
    end_date = end.split('.')

    concerts_by_date = db.concerts.find({'$and': [
        {'date': {'$gte': datetime.datetime(year=2019, month=int(start_date[1]), day=int(start_date[0]))}},
        {'date': {'$lte': datetime.datetime(year=2019, month=int(end_date[1]), day=int(end_date[0]))}}
    ]})
    for concert in concerts_by_date:
        print(concert)


if __name__ == '__main__':

    # read_data('artists.csv', concerts_db)
    # find_cheapest(concerts_db)
    find_by_name('ов', concerts_db)
    #find_by_date('01.07', '30.07', concerts_db)