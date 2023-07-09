#!/usr/bin/python3
""" Defines lockboxes """


def canUnlockAll(boxes):
    """Determines whether all boxes can be unlocked or not.

    Args:
        boxes (list): A list of lists
        representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]
    for key in keys:
        for val in boxes[key]:
            if val not in keys:
                keys.append(val)
    if len(keys) == len(boxes):
        return True
    return False
