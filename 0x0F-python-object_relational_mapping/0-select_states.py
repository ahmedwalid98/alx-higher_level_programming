#!/usr/bin/python3
"""
    a script to list states from database
"""
import sys
import MySQLdb


if __name__ == '__main__':


    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor = db.cursor()
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
