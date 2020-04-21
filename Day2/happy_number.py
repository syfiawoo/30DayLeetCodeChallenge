class Solution:
    @staticmethod
    def is_happy(self, n: int) -> bool:
        tot = n
        same = False
        calc = [n]
        while tot != 1 and not same:
            sum_sq = 0
            while tot > 0:
                sum_sq += (tot % 10) ** 2
                tot //= 10
            same = sum_sq in calc
            tot = sum_sq
            calc.append(tot)
        return tot == 1
