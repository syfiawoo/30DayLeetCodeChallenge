class Solution:
    @staticmethod
    def max_profit(prices) -> int:
        """
        My strategy for solving this finding difference between current
        and previous, and adding it to profit if positive
        :param prices: a list containing stock prices on consecutive days
        :return: int:  maximum profit to be made
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
