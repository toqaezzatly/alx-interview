#!/usr/bin/python3


def isWinner(x, nums):
    def sieve(n):
        """ Returns a list of primes up to n using the Sieve of Eratosthenes. """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulates the game for a given n and returns the winner. """
        if n < 2:
            return "Ben"  # If n < 2, Maria cannot make a move
        
        primes = sieve(n)
        prime_count = len(primes)
        
        # If the count of primes is odd, Maria wins; if even, Ben wins
        return "Maria" if prime_count % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
    