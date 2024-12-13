#!/usr/bin/python3


def is_winner(x, nums):
    """
    Determines the winner of each game round and the overall winner.

    Parameters:
        x (int): The number of rounds.
        nums (list): List of integers representing the max number in each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if tied.
    """
    if x < 1 or not nums:
        return None

    # Determine the maximum number to calculate primes up to
    max_n = max(nums)

    # Step 1: Use Sieve of Eratosthenes to find all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the cumulative number of primes up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Step 2: Simulate each game round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the total number of primes up to n
        total_primes = prime_counts[n]

        # Maria wins if the total number of primes is odd, Ben wins if even
        if total_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None

# Example usage
if __name__ == "__main__":
    print("Winner:", is_winner(5, [2, 5, 1, 4, 3]))
