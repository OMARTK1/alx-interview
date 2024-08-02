#!/usr/bin/python3
"""Script that unlock list of lists"""


def canUnlockAll(boxes):
    """Function that takes list of lists and the hey in it
       will unlock next lists
    """
    if not boxes:
        return False

    box_checked = set()
    F1_box = [0]

    while F1_box:
        curnt_box = F1_box.pop()
        if curnt_box not in box_checked:
            box_checked.add(curnt_box)
            for key in boxes[curnt_box]:
                if key < len(boxes):
                    F1_box.append(key)

    return len(box_checked) == len(boxes)
