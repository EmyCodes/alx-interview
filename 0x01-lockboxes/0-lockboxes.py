#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines whether all boxes can be unlocked or not.

    Args:
        boxes (list): A list of lists
        representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # keys = [0]
    # for key in keys:
    #     for val in boxes[key]:
    #         if val not in keys:
    #             keys.append(val)
    # if len(keys) == len(boxes):
    #     return True
    # return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        key = keys.pop(0)
        if key < num_boxes and not visited[key]:
            visited[key] = True
            keys.extend(boxes[key])

    return all(visited)
