def coin_change_brute_force(coins, amount):
    """
    Brute Force Approach: Try all possible combinations with repetitions
    Time Complexity: O(k^(amount/min(coins))) where k is number of coin types
    Practical complexity: O(amount^k) in worst case
    Space Complexity: O(1)
    """
    if amount == 0:
        return 0
    
    min_coins = float('inf')
    
    # Generate all possible combinations using bit manipulation
    for mask in range(1, 1 << len(coins)):
        total = 0
        coin_count = 0
        
        for i in range(len(coins)):
            if mask & (1 << i):
                # Try using this coin type multiple times
                max_use = amount // coins[i]
                for use_count in range(1, max_use + 1):
                    if total + coins[i] * use_count <= amount:
                        total += coins[i] * use_count
                        coin_count += use_count
                        break
        
        if total == amount:
            min_coins = min(min_coins, coin_count)
    
    return min_coins if min_coins != float('inf') else -1


def coin_change_divide_conquer(coins, amount):
    """
    Divide and Conquer with Memoization (Dynamic Programming)
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    if amount == 0:
        return 0
    
    # Use iterative DP to avoid recursion
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_greedy(coins, amount):
    """
    Greedy Approach: Always use the largest coin possible
    Time Complexity: O(k + amount/min(coins)) where k is number of coin types
    Practical complexity: O(amount) in worst case (when only using smallest coin)
    Space Complexity: O(1)
    
    Note: This only works optimally for certain coin systems (like US coins)
    """
    if amount == 0:
        return 0
    
    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    coin_count = 0
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            coin_count += count
            amount -= coin * count
    
    return coin_count if amount == 0 else -1


# Test the algorithms
def test_algorithms():
    coins = [1, 5, 10, 25]
    test_amounts = [30, 43, 67, 99]
    
    print("Coin denominations:", coins)
    print("=" * 60)
    
    for amount in test_amounts:
        print(f"\nTarget amount: {amount}")
        print("-" * 30)
        
        # Brute Force
        result_bf = coin_change_brute_force(coins, amount)
        print(f"Brute Force:      {result_bf} coins")
        
        # Divide and Conquer (DP)
        result_dc = coin_change_divide_conquer(coins, amount)
        print(f"Divide & Conquer: {result_dc} coins")
        
        # Greedy
        result_greedy = coin_change_greedy(coins, amount)
        print(f"Greedy:           {result_greedy} coins")


# Performance comparison
def performance_comparison():
    import time
    
    coins = [1, 5, 10, 25]
    amount = 67
    
    print(f"\nPerformance Comparison (amount = {amount}):")
    print("=" * 50)
    
    # Brute Force timing
    start = time.time()
    result_bf = coin_change_brute_force(coins, amount)
    time_bf = time.time() - start
    print(f"Brute Force:      {result_bf} coins, {time_bf:.6f}s")
    
    # Divide and Conquer timing
    start = time.time()
    result_dc = coin_change_divide_conquer(coins, amount)
    time_dc = time.time() - start
    print(f"Divide & Conquer: {result_dc} coins, {time_dc:.6f}s")
    
    # Greedy timing
    start = time.time()
    result_greedy = coin_change_greedy(coins, amount)
    time_greedy = time.time() - start
    print(f"Greedy:           {result_greedy} coins, {time_greedy:.6f}s")


# Complexity Analysis and Examples
def analyze_complexities():
    """
    Detailed complexity analysis for coin change with repetitions:
    
    Given:
    - k = number of coin types
    - n = target amount
    - min_coin = smallest coin denomination
    
    1. BRUTE FORCE:
       - Time: O(k^(n/min_coin))
       - Explanation: For each position up to n/min_coin, we have k choices
       - Example: coins=[1,5,10], amount=30 → 3^30 ≈ 2×10^14 operations
    
    2. DIVIDE & CONQUER (Dynamic Programming):
       - Time: O(n × k)
       - Space: O(n)
       - Explanation: Fill DP table of size n, checking k coins for each entry
       - Example: coins=[1,5,10], amount=30 → 30×3 = 90 operations
    
    3. GREEDY:
       - Time: O(k + n/min_coin)
       - Space: O(1)
       - Explanation: Sort k coins once, then at most n/min_coin iterations
       - Example: coins=[1,5,10], amount=30 → 3 + 30/1 = 33 operations
    """
    
    print("COMPLEXITY ANALYSIS FOR COIN CHANGE WITH REPETITIONS")
    print("=" * 55)
    
    examples = [
        {"coins": [1, 5, 10], "amount": 30},
        {"coins": [1, 2, 5], "amount": 50},
        {"coins": [1, 3, 4], "amount": 100}
    ]
    
    for ex in examples:
        coins, amount = ex["coins"], ex["amount"]
        k = len(coins)
        min_coin = min(coins)
        
        print(f"\nExample: coins={coins}, amount={amount}")
        print(f"k={k}, min_coin={min_coin}")
        print("-" * 40)
        
        # Brute Force complexity
        bf_ops = k ** (amount // min_coin)
        print(f"Brute Force: O({k}^{amount//min_coin}) ≈ {bf_ops:,} operations")
        
        # DP complexity
        dp_ops = amount * k
        print(f"Dynamic Programming: O({amount}×{k}) = {dp_ops:,} operations")
        
        # Greedy complexity
        greedy_ops = k + (amount // min_coin)
        print(f"Greedy: O({k}+{amount//min_coin}) = {greedy_ops:,} operations")
        
        # Speedup ratios
        print(f"DP vs Brute Force speedup: {bf_ops/dp_ops:,.0f}x")
        print(f"Greedy vs Brute Force speedup: {bf_ops/greedy_ops:,.0f}x")


if __name__ == "__main__":
    test_algorithms()
    performance_comparison()
    print("\n" + "="*60)
    analyze_complexities()
