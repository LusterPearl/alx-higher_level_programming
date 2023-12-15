#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Check if correct number of arguments is provided """
    if len(sys.argv) != 4:
        print("""
        Usage: ./1-filter_states.py <mysql_username> <mysql_passsword>
                <database_name>
        """)
        sys.exit(1)

        """ Get MySQL connection parameters from command line arguments """
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        """ Create a cursor object to interact with the database """
        cur = db.cursor()

        """ Execute the SQL query to select states starting with 'N' """
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
                    )

        """ Fetch all rows from the result set """
        query_rows = cur.fetchall()

        print("Fetched rows:", query_rows)

        """ display the results """
        for row in query_rows:
            print(row)

        print("Script executed successfully")
        print()

        """ Close the cursor and database connection """
        cur.close()
        db.close()
