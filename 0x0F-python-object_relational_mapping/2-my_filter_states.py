#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Check if correct number of arguments is provided """
    if len(sys.argv) != 5:
        print("""
        Usage: ./2-filter_states.py <mysql_username> <mysql_passsword>
                <database_name> <state_name_searched>
        """)
        sys.exit(1)

        """ Get MySQL connection parameters from command line arguments """
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name_searched = sys.argv[4]

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
        query = ("SELECT * FROM states WHERE name = %s ORDER BY id ASC")
        cur.execute(query, (state_name_searched,))

        """ Fetch all rows from the result set """
        query_rows = cur.fetchall()

        """ Display the results """
        for row in query_rows:
            print(row)

        """ Close the cursor and database connection """
        cur.close()
        db.close()
