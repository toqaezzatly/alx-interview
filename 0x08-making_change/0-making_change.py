#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    Args:
        coins: list of coin values
        total: target amount
    Returns:
        Fewest number of coins needed to meet total,
        0 if total is 0 or less,
        -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    # Initialize dp array with float('inf')
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # For each amount from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
