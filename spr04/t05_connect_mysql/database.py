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