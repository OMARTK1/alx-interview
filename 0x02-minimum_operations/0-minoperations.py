#!/usr/bin/python3
"""
Module that find the minimum number of operations
and result in exactly n H characters into file
"""


def minOperations(n):
    """
    Function that calculates the fewest number of operations needed
    and result in exactly n H characters in the file

    :args n: The target number of H characters to be displayed
    :return: The minimum number of operations or 0 if impossible
    """
    if n <= 1:
        return 0

    opers = 0
    divs = 2

    while n > 1:
        while n % divs == 0:
            opers += divs
            n //= divs
        divs += 1

    return opers
