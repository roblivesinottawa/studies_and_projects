import database


# database.create_table()

database.add_one("Luke", "Skywalker")


stuff = [
    ('Anakin', 'Skywalker'),
    ('Padme', 'Amidala'),
    ('Obiwan', 'Kanobi'),
]
database.add_many(stuff)

# database.delete_one('1')

database.show_all()