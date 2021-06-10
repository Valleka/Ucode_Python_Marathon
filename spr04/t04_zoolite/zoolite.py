import sqlite3
def update_zoo(data: dict):
    try:
        db = sqlite3.connect(data['database'])
        table = data['table']
        news = data['news']
        coursor = db.cursor()
        coursor.execute(f"create table if not exists {table}(species text, name text, age integer)")
        try:
          coursor.execute(f"CREATE UNIQUE INDEX USER ON {table}(species, name)")
          db.commit()
        except Exception as e:
          s = e
        i = 0
        count = coursor.execute(f"SELECT * from {table}")
        print(f"*** BEFORE: {len(coursor.fetchall())} animals in the zoo.")
        for n in news:
          #age = 0
          if n["event"] == "born":
            try:
              comand = f'insert into {data["table"]} (species, name, age) values ("{n["species"]}", "{n["name"]}", 0)'
              c = coursor.execute(comand)
              if c is not None:
                print(f"Inserted {n['species']} {n['name']} in table {table} of {data['database']}.")
              db.commit()
            except Exception as e:
              print(f"Failed to process event: {n}. Error: {e}")
            i += 1
          elif n['event'] == "died":
            coursor.execute(f'DELETE FROM {table}  WHERE species = "{n["species"]}" and name = "{n["name"]}"')
            db.commit()
            print(f"Deleted {n['species']} {n['name']} in table {table} of {data['database']}.")
          elif n['event'] == "birthday":
            coursor.execute(f'SELECT age FROM animals WHERE species = "{n["species"]}" and name = "{n["name"]}"')
            age = coursor.fetchone()
            if age:
                coursor.execute(f'UPDATE {table} SET age = {age[0] + 1} WHERE species = "{n["species"]}" and name = "{n["name"]}"')
                db.commit()
                print(f"Updated {n['species']} {n['name']} in table {table} of {data['database']}.")
        count = coursor.execute(f"SELECT * from {table}")
        print(f"*** AFTER: {len(coursor.fetchall())} animals in the zoo.")
    except Exception as e:
        print(e)