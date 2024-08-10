class Solution(object):
    def maxProfit(self, prices):
        # Initialize variables
        min_price = float('inf')  # Start with a very high minimum price
        max_profit = 0  # Start with zero profit

        # Iterate over the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            else:
                # Calculate the potential profit and update max_profit if it's higher
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
