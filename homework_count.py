import sqlite3


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("SELECT COUNT(order_date) FROM orders WHERE Make='Ford'")
    results = c.fetchone()
    print results,results[0]
    c.execute("SELECT COUNT(order_date) FROM orders WHERE Make='Hondas'")
    results = c.fetchone()
    print results,results[0]
