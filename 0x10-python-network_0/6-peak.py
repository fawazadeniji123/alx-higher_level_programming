#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    
    def binary_peak_search(start, end):
        mid = (start + end) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and (
            mid == len(list_of_integers) - 1
            or list_of_integers[mid] >= list_of_integers[mid + 1]
        ):
            return list_of_integers[mid]

        # If left neighbor is greater, search left
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return binary_peak_search(start, mid - 1)

        # If right neighbor is greater, search right
        return binary_peak_search(mid + 1, end)

    if not list_of_integers:
        return None

    return binary_peak_search(0, len(list_of_integers) - 1)
