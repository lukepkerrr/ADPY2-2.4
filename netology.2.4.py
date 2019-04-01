import csv
import re

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
        reader = csv.reader(csvfile)
        csv_list = list(reader)
        csv_list.pop(0)
        for line in csv_list:
            data.append({
                'artist': line[0],
                'price': int(line[1]),
                'place': line[2],
                'date': line[3]
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

    regex = re.compile('.*{}.*'.format(name))

    concerts_by_name = db.concerts.find({'artist': regex}).sort('price', 1)
    for concert in concerts_by_name:
        print(concert)


if __name__ == '__main__':
    # read_data('artists.csv', concerts_db)
    # find_cheapest(concerts_db)
    find_by_name('ов', concerts_db)