#!/usr/bin
def no_c(my_string):
    print(my_string.translate(str.maketrans("", "", "cC")))
