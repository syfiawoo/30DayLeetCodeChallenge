# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, item: int):
        # create the new node to be added to end of list
        new_node = ListNode(item)
        # check to see if list is empty
        # head should become the new_node
        if not self.head:
            self.head = new_node
        else:
            #
            self.tail.next = new_node
        self.tail = new_node


class Solution:
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
