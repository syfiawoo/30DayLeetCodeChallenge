class Solution:
    @staticmethod
    def single_number(nums) -> int:
        """
        My strategy for solving this problem is checking for
        consecutive numbers in a sorted list
        :param nums: list of numbers
        :return: number which appears only once in the list
        """
        nums = sorted(nums)
        single = nums[0]  # assume the first number appears only once
        is_single = False
        count = 1  # number of occurrences of assumed single
        i = 1
        # so far as we haven't identified a single
        # and not reached end of list
        while not is_single and i < len(nums):
            # comparing assumed single to adjacent number
            if single != nums[i]:
                # how many times has the number appeared so far
                if count == 1:
                    # number appears only once
                    is_single = True
                else:
                    count = 1  # reset count
                    single = nums[i]
            else:
                single = nums[i]
                count += 1
            i += 1  # advance to the next number
        return single
