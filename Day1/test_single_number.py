from pytest import mark

from Day1.single_number import Solution


@mark.parametrize('nums, expected', [([1], 1), ([1, 1, 2], 2), ([1, 2, 1], 2), ([2, 1, 1], 2),
                                     ([1, 1, 2, 3, 2, 3, 2, 4], 4)])
def test_single_number(nums, expected):
    assert Solution.single_number(nums) == expected
