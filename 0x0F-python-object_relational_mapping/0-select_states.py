#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Check if correct number of arguments is provided """
if len(sys.argv) != 4:
    print("""
    Usage: ./0-select_states.py <mysql_username> <mysql_password>
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

    """ Execute the  SQL query to select all states and order by id """
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fecth all rows from the result set """
    query_rows = cur.fetchall()

    """ Display the results """
    for row in query_rows:
        print(row)

    """ Close the cursor and database connection """
    cur.close()
    db.close()
