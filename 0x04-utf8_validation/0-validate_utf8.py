#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): List of integers representing bytes    
    Returns:
        bool: True if valid UTF-8 encoding, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7
    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits
        num = num & 255

        # If this is the start of a new character
        if n_bytes == 0:
            # Count number of 1s in the beginning of the byte
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False

        # If this byte is part of an existing character
        else:
            # Check if the byte starts with 10
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    # Check if all characters were completed
    return n_bytes == 0
