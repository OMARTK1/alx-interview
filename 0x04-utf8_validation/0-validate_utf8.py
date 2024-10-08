#!/usr/bin/python3
"""UTF-8 Fonction Validation"""


def validUTF8(data):
    """Determines if the given data set
    represents a valid utf-8 encoding

     Args:
        data: List of integers that representing bytes

    Returns:
        True if the arg data is a valid UTF-8 encoding, else False
    """
    numb_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if numb_bytes == 0:

            while mask_byte & i:
                numb_bytes += 1
                mask_byte = mask_byte >> 1

            if numb_bytes == 0:
                continue

            if numb_bytes == 1 or numb_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        numb_bytes -= 1

    if numb_bytes == 0:
        return True

    return False
