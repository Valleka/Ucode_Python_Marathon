import mysql.connector
import yaml
import sys


def to_connect():
    res = dict()
    with open("cfg.yaml", 'r') as f:
        try:
            line = yaml.safe_load(f)['settings']
            res['host'] = line['host']
            res['user'] = line['user']
            res['password'] = line['password']
            if 'database' in line:
                res['database'] = line['database']
            else:
                res['database'] = None
        except yaml.YAMLError as e:
            print(e)
    return res


if __name__ == '__main__':
    db = sys.argv
    res = to_connect()
    try:
        conn = mysql.connector.connect(host=res['host'], user=res['user'], password=res['password'],
                                       database=res['database'])
        print(f"Connected to MySQL server (version {conn.get_server_info()}), database {res['database']}.")
        if len(db) == 2:
            cursor = conn.cursor()
            if db[1] == "databases":
                cursor.execute('show databases')
                print("Database list:")
                for d in cursor:
                    print(f"- {d[0]}")
                conn.close()
                print("MySQL connection is closed")
            elif db[1] == "tables":
                if res['database']:
                    cursor.execute(f"use {res['database']}")
                    cursor.execute("show tables")
                    if not cursor:
                        print("No tables")
                    else:
                        print("Table list:")
                        for d in cursor:
                            print(f"- {d[0]}")
                else:
                    print("Error: not connected to a database.")
                conn.close()
                print("MySQL connection is closed")
        elif db[1] == 'create':
            try:
                cursor = conn.cursor()
                cursor.execute(f"create database {db[2]}")
                print(f"Database '{db[2]}' is created.")
                conn.close()
                print("MySQL connection is closed")
            except mysql.connector.Error as err:
                print("MySQL connection Error: {}".format(err))
        elif db[1] == 'drop':
            cursor = conn.cursor()
            cursor.execute(f'drop database {db[2]}')
            print(f"Database '{db[2]}' is dropped.")
            conn.close()
            print('MySQL connection is closed.')
        else:
            print("Error: command-line arguments are invalid")
    except mysql.connector.Error as err:
        print("MySQL connection Error: {}".format(err))
        conn.close()
        print('MySQL connection is closed.')