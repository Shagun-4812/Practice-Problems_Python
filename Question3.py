def coinChange(coins, amount):
    """
    Calculates the minimum number of coins needed to make up the given amount.
    
    Args:
        coins: List of available coin denominations
        amount: Target amount to make
        
    Returns:
        Minimum number of coins needed, or -1 if not possible
    """
    # Initialize DP array with infinity (impossible values)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([], 7, -1),
        ([1, 3, 4], 6, 2),
        ([2, 5, 10], 13, 4),
        ([1, 2, 5], 100, 20),
        ([1, 2, 2, 5], 11, 3),  # Duplicate coins
        ([3, 7], 9, 3),
        ([186, 419, 83, 408], 6249, 20)  # Large amount case
    ]
    
    for coins, amount, expected in test_cases:
        result = coinChange(coins, amount)
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"Expected: {expected}, Result: {result}")
        print(f"Test {'Passed' if result == expected else 'Failed'}\n")