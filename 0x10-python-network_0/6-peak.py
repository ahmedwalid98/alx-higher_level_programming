#!/usr/bin/python3
"""
    finds the peak element
"""


def find_peak(list_of_integers):
    """
    finds the peak element
    """
    if not list_of_integers:
        return None
    peak_list = []
    for i in range(0, len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] >= list_of_integers[i + 1]:
                peak_list.append(list_of_integers[i])
            else:
                continue
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] >= list_of_integers[i - 1]:
                peak_list.append(list_of_integers[i])
            else:
                continue
        elif list_of_integers[i] >= list_of_integers[i + 1] \
                and list_of_integers[i] >= list_of_integers[i - 1]:
            peak_list.append(list_of_integers[i])

    return max(peak_list)
