'''
	You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 < prices.length <= 5 * 104
0 < prices[i], fee < 5 * 104
   Hide Hint #1  
Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.




'''

class Solution:
    def maxProfit(self, B, fee):
        if len(B) == 1: return 0
        n = len(B)
        
        dp, sp = [-float(inf)]*n, [0]*n

        for i in range(n-1):
            dp[i] = B[i+1] - B[i] + max(dp[i-1], sp[i-2] - fee)
            sp[i] = max(sp[i-1], dp[i])
             
        return sp[-2] 