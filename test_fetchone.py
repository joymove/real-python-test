import sqlite3


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT avg(population) FROM population")
    result = c.fetchone()
    print result
