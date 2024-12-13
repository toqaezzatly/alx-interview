# Prime Game

## Overview

The Prime Game is a two-player game where players take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including `n`. The player who cannot make a move loses the game. Maria always goes first, and both players play optimally.

## Problem Statement

Given `x` rounds of the game, where `n` may differ for each round, the task is to determine the player who wins the most rounds. If the winner cannot be determined, the function should return `None`.

## Solution

The solution is implemented in the `isWinner` function, which takes two parameters:

- `x`: The number of rounds.
- `nums`: An array of integers representing the upper limit (`n`) for each round.

### Key Functions

1. **sieve(n)**: 
   - This function generates a list of prime numbers up to `n` using the Sieve of Eratosthenes algorithm.
   - It returns a list of prime numbers.

2. **play_game(n)**:
   - This function simulates the game for a given `n`.
   - It determines the winner based on the count of prime numbers:
     - If the count of primes is odd, Maria wins.
     - If the count is even, Ben wins.

3. **isWinner(x, nums)**:
   - This is the main function that iterates through the list of `nums`, counts the wins for Maria and Ben, and returns the name of the player with the most wins.

### Example

```python
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))