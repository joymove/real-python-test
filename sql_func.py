import sqlite3


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    # Create a dictionary of sql queries
    sql = {'average': "SELECT avg(population) FROM population",
            'maximum': "SELECT max(population) FROM population",
            'minimum': "SELECT min(population) FROM population",
            'sum': "SELECT count(city) FROM population",
            'count': "SELECT count(city) FROM population"
            }
    # Run each sql query item in the dictionary
    for keys, values in sql.iteritems():
        # Run sql
        c.execute(values)
        # Fetchone() retrieves one record from the query
        result = c.fetchone()
        # Output the result to screen
        print keys + ":", result[0]
