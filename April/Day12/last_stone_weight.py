class Solution:
    @staticmethod
    def last_stone_weight(stones: object) -> int:
        """
        My strategy for solving this problem is to first sort (asc) the list of stones,
        remove the last two stones, find and push the positive difference back onto the list
        :param stones:
        :return:
        :rtype: int
        """
        # we need at least 2 stones to cancel out each other
        while len(stones) > 1:
            stones = (sorted(stones))
            # get the last 2 stones
            stone1 = stones.pop()
            stone2 = stones.pop()
            result_stone = abs(stone1 - stone2)  # find the difference
            # check if resulting stone is positive
            if result_stone > 0:
                stones.append(result_stone)  # add to list
        resultant = 0
        if len(stones):
            resultant = stones.pop()
        return resultant
