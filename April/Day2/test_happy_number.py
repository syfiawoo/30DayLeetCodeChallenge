from pytest import mark

from April.Day2.happy_number import Solution


@mark.parametrize('num, expected', [(2, False),
                                    (10, True),
                                    (19, True),
                                    (101, False),
                                    (91, True),
                                    (23, True)
                                    ])
def test_is_happy(num, expected):
    assert Solution.is_happy(num) == expected
