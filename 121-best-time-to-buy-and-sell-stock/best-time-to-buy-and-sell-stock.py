class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        # min_price = float('inf')
        # max_profit = 0
        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)
        # return max_profit
# Memoization
        n = len(prices)
        dp = [[-1] * 2 for i in range(n)]
    
        def f(i, canBuy):
            if i == n:
                return 0
            if dp[i][canBuy] != -1:
                return dp[i][canBuy]
        
            if canBuy:
                dp[i][canBuy] = max(-prices[i] + f(i+1, 0), f(i+1, 1))
            else:
                dp[i][canBuy] = max(prices[i], f(i+1, 0))
        
            return dp[i][canBuy]
    
        return f(0, 1)   # start at day 0, we can buy



        #1.
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if(prices[j]>prices[i]):
        #             profit=max(profit,prices[j]-prices[i])
        #         else:
        #             j+=1
        # return profit

        #2.
        # i=0
        # profit=0
        # for j in range(1,len(prices)):
        #     if prices[i]<prices[j]:
        #         curr=prices[j]-prices[i]
        #         profit=max(profit,curr)
        #     else:
        #         i=j
        # return profit



# \U0001f4dd Problem Recap

# You’re given an array prices[] where prices[i] = price of a stock on day i.
# You want to maximize profit by buying on one day and selling on a later day.

# \U0001f511 Key Idea

# At any day i, you have two choices:

# Buy the stock (if you haven’t already bought).

# Sell the stock (if you already bought).

# But since this problem allows only one transaction (1 buy + 1 sell), the state is simpler than the full "Stock Buy & Sell" DP (with multiple transactions).

# 1️⃣ Recursive Thinking

# Let’s define a function:

# f(i, canBuy)


# i = current day index.

# canBuy = boolean (1 if you can buy, 0 if you must sell).

# Transitions:

# If canBuy == 1:

# Either buy at day i → profit = -prices[i] + f(i+1, 0)

# Or skip buying → profit = f(i+1, 1)

# Take max of both.

# If canBuy == 0:

# Either sell at day i → profit = prices[i] + f(i+1, 1)

# Or skip selling → profit = f(i+1, 0)

# Take max of both.

# Base Case:

# If i == len(prices), return 0 (no days left).

# Recursive Formula:
# f(i, 1) = max(-prices[i] + f(i+1, 0), f(i+1, 1))   # can buy
# f(i, 0) = max(prices[i] + f(i+1, 1), f(i+1, 0))    # must sell


# This is the recursion.

# 2️⃣ Memoization (Top-Down DP)

# Since many states repeat, store results in a dp[i][canBuy].

# def maxProfit(prices):
#     n = len(prices)
#     dp = [[-1] * 2 for _ in range(n)]
    
#     def f(i, canBuy):
#         if i == n:
#             return 0
#         if dp[i][canBuy] != -1:
#             return dp[i][canBuy]
        
#         if canBuy:
#             dp[i][canBuy] = max(-prices[i] + f(i+1, 0), f(i+1, 1))
#         else:
#             dp[i][canBuy] = max(prices[i] + f(i+1, 1), f(i+1, 0))
        
#         return dp[i][canBuy]
    
#     return f(0, 1)   # start at day 0, we can buy

# 3️⃣ Tabulation (Bottom-Up DP)

# We build dp[i][canBuy] from the end backwards.

# def maxProfit(prices):
#     n = len(prices)
#     dp = [[0] * 2 for _ in range(n+1)]  # extra row for base case
    
#     for i in range(n-1, -1, -1):   # from last day to first
#         dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
#         dp[i][0] = max(prices[i] + dp[i+1][1], dp[i+1][0])
    
#     return dp[0][1]

# 4️⃣ Space Optimized

# Since only i+1 is needed, we can reduce to 2 variables:

# def maxProfit(prices):
#     n = len(prices)
#     ahead = [0, 0]  # dp for i+1
#     curr = [0, 0]   # dp for i
    
#     for i in range(n-1, -1, -1):
#         curr[1] = max(-prices[i] + ahead[0], ahead[1])  # can buy
#         curr[0] = max(prices[i] + ahead[1], ahead[0])   # must sell
#         ahead = curr[:]
    
#     return ahead[1]

# 5️⃣ Simplified Formula for LeetCode 121

# Since only one buy and one sell is allowed, we can simplify:

# Keep track of the minimum price seen so far.

# At each day, calculate profit = price[i] - minPriceSoFar.

# Take the max profit.

# def maxProfit(prices):
#     min_price = float('inf')
#     max_profit = 0
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
#     return max_profit


# ✅ This last one is the optimized greedy solution (O(n), O(1)) which is easier.
# But the recursion → memoization → tabulation steps are how we derive the DP formula logically.

            

        