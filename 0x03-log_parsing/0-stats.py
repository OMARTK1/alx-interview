#!/usr/bin/python3

"""A script reading stdin line by line and computes metrics"""

import sys


def Imprimer(dict, size):
    """ This prints the input info provided """
    print("File size: {:d}".format(size))
    for i in sorted(dict.keys()):
        if dict[i] != 0:
            print("{}: {:d}".format(i, dict[i]))


psc = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

compte = 0
size = 0

try:
    for line in sys.stdin:
        if compte != 0 and compte % 10 == 0:
            Imprimer(psc, size)

        psclist = line.split()
        compte += 1

        try:
            size += int(psclist[-1])
        except:
            pass

        try:
            if psclist[-2] in psc:
                psc[psclist[-2]] += 1
        except:
            pass
    Imprimer(psc, size)


except KeyboardInterrupt:
    Imprimer(psc, size)
    raise
