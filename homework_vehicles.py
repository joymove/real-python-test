import sqlite3


with sqlite3.connect("cars.db") as conn:
    cursor = conn.cursor()
    vehicles = [('Ford', 'a1', 2),('Ford', 'a2', 3),('Ford','a3',4),('Hondas','b1',2),('Hondas', 'b2', 3)]
    cursor.executemany("INSERT INTO inventory(Make, Model, Quantity) values (?,?,?)", vehicles)

    cursor.execute("UPDATE inventory set quantity=3 WHERE model='a1'")    
    cursor.execute("UPDATE inventory set quantity=5 WHERE model='b2'")    
    
# Output all the records from the table
    cursor.execute("SELECT * FROM inventory")
    records = cursor.fetchall()
    for row in records:
        print row[0],row[1], row[2]

    print "\noutput only ford vehicles\n"
# Output only ford vehicles
    cursor.execute("SELECT * FROM inventory WHERE Make='Ford'")
    records = cursor.fetchall()
    for row in records:
        print row[0],row[1], row[2]


