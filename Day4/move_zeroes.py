class Solution:
    @staticmethod
    def move_zeroes(nums) -> None:
        """
        My strategy for solving this finding consecutive number of zeroes, and
        swapping them with numbers that come after the last zero encountered
        There is a case where we might have more zeroes than numbers to be swapped;
        in this we always pick the lesser of last index to be copied and length of list
        :param nums: a list containing numbers
        :return: None, list is modified in place
        """
        i = 0
        zero_count = 0
        while i < len(nums):
            if nums[i] == 0:
                zero_count += 1
            else:
                # check if we've encountered any zeroes so far
                if zero_count > 0:
                    end = zero_count + i  #
                    nm_copy = zero_count  # number of elements to be substituted with zeroes
                    # make sure the end index does not go out of bounds
                    if end > len(nums):
                        end = len(nums)
                        nm_copy = end - i  # the number of elements that need to be switched
                    for k in range(nm_copy):
                        # swap any the zeros we've encountered so far with the numbers after last encountered zero
                        nums[i - zero_count + k] = nums[i + k]
                    # set the numbers we copied over to zero
                    for j in range(zero_count):
                        if i + j < len(nums):
                            nums[i + j] = 0
                    i -= zero_count  # go back a few indexes since we might have copied some zeroes over
                zero_count = 0  # reset the number of zeros encountered
            i += 1
