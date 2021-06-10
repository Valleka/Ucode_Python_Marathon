import mysql.connector

def get_param():
    d = dict()
    with open("cfg.yaml", 'r') as f:
        i = 0
        for line in f:
            if i > 0:
                if i == 1:
                    host = line.split(": ")[1]
                    d['host'] = host
                if i == 2:
                    user = line.split(": ")[1]
                    d['user'] = user
                if i == 3:
                    try:
                        password = line.split(": ")[1]
                        d['password'] = password
                    except Exception as e:
                        d['password'] = ''
            i +=1
        return d


if __name__ == '__main__':
    dic = get_param()
    try:
        mydb = mysql.connector.connect(host=dic['host'],
                                   user=dic['user'],
                                   password=dic['password'])
        print(f"Connected to MySQL server (version {mydb.get_server_info()}).")
        mydb.close()
        print("MySQL connection is closed")
    except mysql.connector.Error as e:
        print("MySQL connection Error: {}".format(e))