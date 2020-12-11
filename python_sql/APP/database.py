import sqlite3


def create_table():
    connector = sqlite3.connect('starwars.db')
    conn = connector.cursor()

    conn.execute("CREATE TABLE starwars (first_name TEXT, last_name TEXT)")

    connector.commit()
    connector.close()


def show_all():
    connector = sqlite3.connect('starwars.db')
    conn = connector.cursor()

    conn.execute("SELECT * FROM starwars")
    items = connector.fetchone()

    for item in items:
        print(item)

    connector.commit()
    connector.close()



def add_one(first, last):
    connector = sqlite3.connect('starwars.db')
    conn = connector.cursor()
    conn.execute("INSERT INTO starwars VALUES (?,?)", (first, last))

    connector.commit()
    connector.close()



def add_many(list):
    connector = sqlite3.connect('starwars.db')
    conn = connector.cursor()
    conn.executemany("INSERT INTO starwars VALUES (?,?)", (list))

    connector.commit()
    connector.close()



def delete_one(id):
    connector = sqlite3.connect('starwars.db')
    conn = connector.cursor()
    conn.execute("DELETE FROM starwars WHERE rowid = (?)", id)

    connector.commit()
    connector.close()
