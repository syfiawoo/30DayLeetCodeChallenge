class Solution:
    @staticmethod
    def is_happy(n: int) -> bool:
        """
        My strategy for solving this problem is maintaining a list of numbers that have
        already been encountered to prevent an indefinite amount of calculations
        :param n: a counting number
        :return: boolean indicating if number is happy
        """
        num = n
        same = False  # track if we have already encountered num
        calc = [n]
        while num != 1 and not same:
            sum_square = 0
            # get individual digits and perform calculation
            while num > 0:
                sum_square += (num % 10) ** 2
                num //= 10
            # have we already encountered this number
            same = sum_square in calc
            num = sum_square
            calc.append(num)
        return num == 1
