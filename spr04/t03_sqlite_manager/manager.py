import sqlite3

connections = dict()
if __name__ == '__main__':
    i = True
    while i:
        command = input(f'Enter command: ')
        if command == 'help':
            print('Available commands:')
            print('- help')
            print('- connect [database]')
            print('- close [database]')
            print('- execute [database] "[SQL statement]"')
            print('- show')
            print('- exit')
        elif command == "show":
            if connections:
                print('Connected to:')
                print(list(connections))
            else:
                print("No connections.")
        elif 'connect' in command:
            spl = command.split(' ')
            if len(spl) == 2: #проверяем состоит ли команда из 2 аргументов
                if spl[1] in connections: #проверяем, есть ли подключение к этой базе
                    print(f'Already connected to database "{spl[1]}".') # если есть, выводим сообщение
                else: # если коннекта нет, создаем новое подключение к бд
                    try:
                        db = sqlite3.connect(spl[1])
                        connections[spl[1]] = db #записали бд в наш словарь
                    except Exception as e:
                        print(e)
                    print(f'Created connection to database "{spl[1]}".')
            else:
                print('Invalid command. Try "help" to see available commands.')
        elif command == 'exit':
            for c in connections:
                connections[c].close()
                print(f'Closed connection to database "{c}".')
            i = False
        elif 'close' in command:
            spl = command.split(' ')
            if len(spl) == 2:
                if spl[1] in connections:
                    connections[spl[1]].close()
                    connections.pop(spl[1])
                    print(f'Closed connection to database "{spl[1]}".')
                else:
                    print(f'Cannot close connection to "{spl[1]}". Not connected.')
            else:
                print('Invalid command. Try "help" to see available commands.')
        elif 'execute' in command:
            try:
                db1 = command.split('"')[0]
                db = db1.split(" ")[1]
                sql_comnd = command.split('"')[1]  # команда прилетает корректная, проверено
                sql_connect = connections[db]
                cursor = sql_connect.cursor()
                cursor.execute(sql_comnd)
                sql_connect.commit()
                print(f'Executed SQL statement.')
            except Exception as e:
                print(e)
        else:
            print('Invalid command. Try "help" to see available commands.')