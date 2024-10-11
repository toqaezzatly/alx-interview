#!/usr/bin/env python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    :param boxes: List of lists where each list contains keys for other boxes.
    :return: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]  # Start with the keys from the first box

    # Keep track of the boxes we can unlock
    for key in keys:
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])  # Add the keys from the newly unlocked box

    return all(unlocked)


# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False
