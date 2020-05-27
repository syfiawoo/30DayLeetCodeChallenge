class Solution:
    @staticmethod
    def product_except_self(nums):
        """
        My strategy for solving this problem is to treat lists that contain zeroes differently.
        If the list contains no zeroes, I find the product of numbers in the list, and divide
        the product by each number in the list. For handling zeroes, if there are multiple zeroes,
        then all products will be zero. With just one zero, there is only one product which isn't
        zero, and that's the product of the rest of the numbers. I kind of brute-forced this as
        it was indicated not to use division. Will update when I think of another solution.
        :param nums: list of numbers
        :return: a list containing product of elements in the list with the exception of number at
        that index
        :rtype: list
        """
        prod = 1
        prod_list = []
        # check if there is a zero
        if 0 in nums:
            zeroes = [i for i in range(len(nums)) if nums[i] == 0]  # get indexes of zeroes
            prod_list = [0 for num in nums]  # create a product array of zeroes
            # If there is only 1 zero
            if len(zeroes) == 1:
                for num in nums:
                    # find product of rest of list without the zero
                    if num != 0:
                        prod *= num
                prod_list[zeroes[0]] = prod  # replace index with the zero with the product
        else:
            # find product of all elements
            for num in nums:
                prod *= num
            # divide product with each number and append result to list
            for num in nums:
                prod_list.append(prod // num)

        return prod_list
