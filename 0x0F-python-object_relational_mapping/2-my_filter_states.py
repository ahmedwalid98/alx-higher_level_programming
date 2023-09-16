#!/usr/bin/python3
"""script that takes argument and display state based on the arg"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name='{}'".format(sys.argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
