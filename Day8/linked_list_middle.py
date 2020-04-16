# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''

    '''

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def insert_node(self, item: int):
            pass

    @staticmethod
    def middle_node(head: ListNode) -> ListNode:
        """
        :param head:
        :return: middle node
        """
        curr = head  # start from the first item
        m_list = []  # an empty list to which nodes would be appended
        # add all elements in linked list to our list
        while curr:
            m_list.append(curr)  # add current node to list
            curr = curr.next  # advance current node to next
        mid = len(m_list) // 2  # find middle of list
        return m_list[mid]
