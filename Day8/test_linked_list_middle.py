from pytest import fixture

from Day8.linked_list_middle import Solution


@fixture
def create_list():
    test_list = Solution.LinkedList()
    return test_list


def test_middle_node():
    assert False


def test_append_node(create_list):
    test_list = create_list
    test_list.append_node(4)
    test_list.append_node(5)
    test_list.append_node(6)
    assert test_list.head.val == 4
    assert test_list.head.next.val == 5
    assert test_list.tail.val == 6
