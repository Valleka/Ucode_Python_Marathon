import mysql.connector
import yaml


def get_params(database):
    res = dict()
    with open("cfg.yaml", 'r') as f:
        try:
            line = yaml.safe_load(f)['settings']
            res['host'] = line['host']
            res['user'] = line['user']
            res['password'] = line['password']
            res['database'] = database
        except yaml.YAMLError as e:
            print(e)
    return res


def to_connect(res):
    try:
        conn = mysql.connector.connect(host=res['host'], user=res['user'], password=res['password'])
        cursor = conn.cursor()
        cursor.execute(f"create database if not exists {res['database']}")
        cursor.execute(f"use {res['database']}")
        return conn
    except mysql.connector.Error as e:
        print(e)


def update_zoo(data: dict):
    db = data['database']
    table = data['table']
    res = get_params(db)
    conn = to_connect(res)
    cursor = conn.cursor()
    try:
        cursor.execute(f"create table if not exists {table}(species text, name text, age integer)")
        for d in data['news']:
            if d['event'] == 'born':
                if len(d) == 3:
                    cursor.execute(f'INSERT INTO {table} (species, name, age) VALUES ("{d["species"]}","{d["name"]}",0)')
                    conn.commit()
                else:
                    for dt in d:
                        if dt != "name" and dt != "species" and dt != "age" and dt != 'event':
                            cursor.execute(f"alter table {table} add {dt} text after age")
                            conn.commit()
    except mysql.connector.Error as e:
        print(e)


data = {
    "database": "zoo",
    "table": "animals",
    "news": [
        {
            "species": "Bear",
            "name": "Angela",
            "event": "born"
        },
        {
            "species": "Bear",
            "name": "Walter",
            "event": "born",
            "weight": 15,
            "area": "A2"
        },
        {
            "species": "Penguin",
            "name": "Daisy",
            "event": "birthday",
            "area": "A2"
        },
        {
            "species": "Hyena",
            "name": "Jay",
            "event": "moved in",
            "age": 10,
            "area": "A2"
        },
        {
            "species": "Horse",
            "name": "Jack",
            "event": "moved in",
            "age": 6
        },
        {
            "species": "Bat",
            "name": "Alex",
            "event": "birthday",
            "endangered": False
        },
        {
            "species": "Giraffe",
            "name": "Lisa",
            "event": "moved in",
            "age": 5
        },
        {
            "species": "Koala",
            "name": "Max",
            "event": "moved in",
            "age": 4,
            "area": "A1"
        },
        {
            "species": "Panda",
            "name": "Rocky",
            "event": "moved in",
            "age": 10,
            "endangered": True
        },
        {
            "species": "Penguin",
            "name": "Ollie",
            "event": "born",
            "area": "A2",
            "endangered": False
        },
        {
            "species": "Panda",
            "name": "Micky",
            "event": "birthday",
            "area": "A2"
        },
        {
            "species": "Bat",
            "name": "Red",
            "event": "born",
            "area": "A1"
        },
        {
            "species": "Wolf",
            "name": "Max",
            "event": "moved in",
            "age": 10
        },
        {
            "species": "Bear",
            "name": "Luke",
            "event": "born",
            "endangered": False
        },
        {
            "species": "Bear",
            "name": "Rocky",
            "event": "born",
            "weight": 20
        },
        {
            "species": "Wolf",
            "name": "Walter",
            "event": "birthday",
            "endangered": True
        },
        {
            "species": "Puma",
            "name": "Micky",
            "event": "birthday",
            "area": "A1",
            "weight": 90
        },
        {
            "species": "Gorilla",
            "name": "Oscar",
            "event": "born",
            "area": "A1"
        },
        {
            "species": "Lion",
            "name": "Ollie",
            "event": "moved in",
            "age": 10,
            "weight": 105,
            "endangered": False
        },
        {
            "species": "Giraffe",
            "name": "Jay",
            "event": "moved in",
            "age": 2,
            "endangered": False,
            "weight": 90
        },
        {
            "species": "Hyena",
            "name": "Oscar",
            "event": "born"
        },
        {
            "species": "Penguin",
            "name": "Ollie",
            "event": "born"
        },
        {
            "species": "Tortoise",
            "name": "Walter",
            "event": "birthday"
        },
        {
            "species": "Bear",
            "name": "Tina",
            "event": "birthday",
            "weight": 23
        },
        {
            "species": "Giraffe",
            "name": "Jay",
            "event": "moved in",
            "age": 25,
            "area": "A2"
        },
        {
            "species": "Tortoise",
            "name": "Ozzy",
            "event": "moved in",
            "age": 80
        },
        {
            "species": "Horse",
            "name": "Lisa",
            "event": "moved in",
            "age": 8
        },
        {
            "species": "Lion",
            "name": "Ruby",
            "event": "birthday",
            "weight": 81
        },
        {
            "species": "Bear",
            "name": "Max",
            "event": "born"
        },
        {
            "species": "Giraffe",
            "name": "Luke",
            "event": "moved in",
            "age": 12
        }
    ]
}


#update_zoo(data)
