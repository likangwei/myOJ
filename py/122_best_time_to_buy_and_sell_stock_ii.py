__author__ = 'lxzMac'
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max = 0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                max = max + prices[i+1]-prices[i]
        return max