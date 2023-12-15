#!/usr/bin/python3
"""Script to connect to MySQL using MySQLdb"""

import MySQLdb

# Connect to MySQL
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
        cur = conn.cursor()

        # Execute SQL query
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()

        # Print query results
        for row in query_rows:
                print(row)

                # Close connections
                cur.close()
                conn.close()
