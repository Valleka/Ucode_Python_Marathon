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


def update_db(data: dict):
    db = data['database']
    table = data['table']
    res = get_params(db)
    conn = to_connect(res)
    cursor = conn.cursor()
    try:
        cursor.execute(f"create table if not exists {table}(id integer, method_r text, url text, params text, body text, status integer)")
        for d in data['news']:
            #if d['event'] == 'born':
                #if len(d) == 3:
            cursor.execute(f'INSERT INTO {table} (id, method_r, url, params, body, status) VALUES ("{d["id"]}","{d["method_r"]}","{d["url"]}","{d["params"]}","{d["body"]}","{d["status"]}",0)')
            conn.commit()
                # else:
                #     for dt in d:
                #         if dt != "name" and dt != "species" and dt != "age" and dt != 'event':
                #             cursor.execute(f"alter table {table} add {dt} text after age")
                #             conn.commit()
    except mysql.connector.Error as e:
        print(e)