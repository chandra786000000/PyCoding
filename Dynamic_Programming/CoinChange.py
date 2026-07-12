class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # type: ignore
        if amount == 0:
            return 0
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        coins.sort()
        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
                else:
                    break
        if dp[amount] !=float('inf'):
            return dp[amount]
        else:
            return -1



# What does dp[i] represent ->
# dp[i] = how many min coins it takes so that total amount is i


# dp[i] = dp[i-coin] + 1 if coin is in coins
# for coin in coins:
#       dp[i] = min(dp[i],dp[i-coin]+1)