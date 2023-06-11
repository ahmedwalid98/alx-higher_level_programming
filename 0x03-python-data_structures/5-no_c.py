#!/usr/bin/python3
def no_c(my_string):
    x = ""
    y = ""
    z = "cC"
    table = str.maketrans(x, y, z)
    return my_string.translate(table)
