#!/usr/bin/env python3
def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked or not.

    Args:
        boxes (list): A list of lists representing the boxes and their corresponding keys.
            Each inner list represents a box, and the indices of the outer list represent
            the box numbers. Each inner list contains the keys that can unlock other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

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
