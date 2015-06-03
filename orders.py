import csv
import sqlite3


with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()
    entries = csv.reader(open("order_csv", "rU"))
    c.execute("CREATE TABLE orders(Make TEXT, Model TEXT, order_date datetime)")
    c.executemany("INSERT INTO orders values (?,?,?)", entries)
