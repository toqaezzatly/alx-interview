# Making Change

This project implements a solution to the coin change problem using dynamic programming. The goal is to find the minimum number of coins needed to make up a given total amount.

## Problem Description

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
- `coins`: A list of integers representing coin denominations
- `total`: The target amount to make change for

### Returns
- Fewest number of coins needed to meet the total
- Returns 0 if total is 0 or less
- Returns -1 if total cannot be met by any number of coins

### Constraints
- The value of a coin will always be an integer greater than 0
- You have an infinite number of each denomination of coin

## Algorithm Explanation

The solution uses a dynamic programming approach:

1. **Base Cases**:
   - If total ≤ 0, return 0
   - Initialize an array `dp` of size total + 1 with infinity
   - Set dp[0] = 0 (it takes 0 coins to make amount 0)

2. **Dynamic Programming Process**:
   - For each amount from 1 to total:
     - For each coin denomination:
       - If the coin value is less than or equal to current amount
       - Update dp[amount] with minimum of:
         - Current value of dp[amount]
         - 1 + dp[amount - coin]

3. **Final Result**:
   - If dp[total] is still infinity, return -1 (impossible to make change)
   - Otherwise, return dp[total]

  ## Algorithm Flowchart

  This flowchart illustrates the dynamic programming approach
  used in the solution. It starts by checking if the total is
  less than or equal to 0. If it is, the function returns 0.
  Otherwise, the function initializes an array dp of size
  total + 1 with infinity and sets dp[0] = 0.
  Then, for each amount from 1 to total, it iterates through
  each coin denomination. If the coin value is less than or
  equal to the current amount, it updates dp[current amount]
  with the minimum of its current value and 1 + dp[current
  amount - coin].
  After iterating through all amounts, it checks if dp[total]
  is still infinity. If it is, the function returns -1
  (impossible to make change). Otherwise, it returns dp[total].

## Algorithm Flowchart

```mermaid
flowchart TD
    A[Start] --> B{Is total <= 0?}
    B -->|Yes| C[Return 0]
    B -->|No| D[Initialize dp array of size total + 1 with infinity]
    D --> E[Set dp[0] = 0]
    E --> F[For each amount i from 1 to total]
    F --> G[For each coin in coins]
    G --> H{Is coin <= current amount i?}
    H -->|No| G
    H -->|Yes| I[Update dp[i] = min(dp[i], dp[i-coin] + 1)]
    I --> G
    G --> |Done with all coins| F
    F --> |Done with all amounts| J{Is dp[total] infinite?}
    J -->|Yes| K[Return -1]
    J -->|No| L[Return dp[total]]
    K --> M[End]
    L --> M
    C --> M
```

## Time and Space Complexity

- Time Complexity: O(total * len(coins))
  - We iterate through each amount from 1 to total
  - For each amount, we consider each coin denomination
- Space Complexity: O(total)
  - We use a dp array of size total + 1

## Example

```python
coins = [1, 2, 25]
total = 37

Result: 7 (25 + 2 + 2 + 2 + 2 + 2 + 2 = 37)
```

The algorithm determines that 7 coins is the minimum number needed to make 37 (one 25-cent coin and six 2-cent coins).