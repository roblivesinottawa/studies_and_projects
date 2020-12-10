import sqlite3

# creating a connection
connected = sqlite3.connect('connect.db')

# create a table
cursor = connected.cursor()


# many_customers = [
#     ('John', 'Doe', 'john@icloud.com'),
#     ('Jane', 'Doe', 'jane@icloud.com'),
#     ('Mary', 'Brown', 'mary@icloud.com'),
# ]

# # populate table
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# update records
# cursor.execute("""
# UPDATE customers SET first_name = 'John'
# WHERE rowid = 4


# """)

# # delete records
# cursor.execute("DELETE from customers WHERE last_name = 'Doe' ")

# drop table
cursor.execute("DROP TABLE customers")

connected.commit()
# query database - order by
cursor.execute("SELECT * FROM customers")

items = cursor.fetchall()

for item in items:
    print(item)


print("command executed successfully...")


# COMMIT TO A DATABASE
connected.commit()

# close connection
connected.close()