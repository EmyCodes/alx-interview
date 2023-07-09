#!/usr/bin/python3
def canUnlockAll(boxes):
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
