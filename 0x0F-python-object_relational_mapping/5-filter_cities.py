#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa (SQL injection free!).


Usage: ./5-my_filter_states.py <mysql_username> <mysql_password>
        <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Check if correct number of arguments is provided """
    if len(sys.argv) != 5:
        print("""
        Usage: ./5-filter_states.py <mysql_username> <mysql_passsword>
                <database_name <state_name>
        """)
        sys.exit(1)

        """ Get MySQL connection parameters from command line arguments """
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        """ Create a cursor object to interact with the database """
        cur = db.cursor()

        """ Execute the safe SQL query to select states """
        query = """
                SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE statesname = %s
                ORDER BY cities.id ASC
                """
        cur.execute(query, (state_name,))

        """ Fetch all rows from the result set """
        result = cur.fetchone()[0]

        """ Display the results """
        if result:
            print(result)
        else:
            print("No cities found for the specified state")

        """ Close the cursor and database connection """
        cur.close()
        db.close()
