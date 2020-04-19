from pytest import fixture, mark

from Day8.linked_list_middle import Solution


@fixture
def create_list():
    test_list = Solution.LinkedList()
    return test_list


@fixture
def add_to_list(create_list, nums):
    for num in nums:
        create_list.append_node(num)
    return create_list


@mark.parametrize('nums', [range(1), range(2), range(100), range(105)])
def test_middle_node(add_to_list, nums):
    result_list = add_to_list
    assert Solution.middle_node(result_list.head).val == nums[len(nums) // 2]


def test_append_node(create_list):
    create_list.append_node(4)
    create_list.append_node(5)
    create_list.append_node(6)
    assert create_list.head.val == 4
    assert create_list.head.next.val == 5
    assert create_list.tail.val == 6
