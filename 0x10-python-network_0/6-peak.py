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
    low = 0
    r = len(list_of_integers)
    mid = low + (r - low) / 2
    mid = int(mid)
    if r == 1:
        return list_of_integers[0]
    if r == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid + 1] \
            and list_of_integers[mid] >= list_of_integers[mid - 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])

    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid - 1])
