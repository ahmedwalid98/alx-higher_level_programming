#!/usr/bin/python3
"""script to list all states start with a letter N"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)

    cursor = db.cursor()
    query = """SELECT * FROM states WHERE states.name LIKE 'N%'
    ORDER BY states.id ASC"""
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
