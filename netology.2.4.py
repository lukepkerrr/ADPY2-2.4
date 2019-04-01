import csv
import re

from pymongo import MongoClient

client = MongoClient
concerts_db = client.concerts_db



def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        print(reader)
        print(db)



def find_cheapest(db):
    """
    Найти самые дешевые билеты
    Документация: https://docs.mongodb.com/manual/reference/operator/aggregation/sort/
    """


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и выведите их по возрастанию цены
    """

    regex = re.compile('укажите регулярное выражение для поиска')


if __name__ == '__main__':
    read_data('artists.csv', concerts_db)