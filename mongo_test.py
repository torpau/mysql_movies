from pymongo import MongoClient


def main():
    client = MongoClient('mongodb://root:s3cr37@localhost:27027')
    db = client.person_db
    persons_collection = db.persons

    p1 = {
        'first_name': 'Lisa',
        'last_name': 'Andersson',
        'age': 25,
        'likes': ['Candles', 'Walks', 'Dogs']
    }
    p2 = {
        'first_name': 'Pelle',
        'last_name': 'Svensson',
        'age': 29,
        'fav-music': 'Punk'
    }

    p1_id = persons_collection.insert_one(p1).inserted_id
    p2_id = persons_collection.insert_one(p2).inserted_id


if __name__ == '__main__':
    main()
