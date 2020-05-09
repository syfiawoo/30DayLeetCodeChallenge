class MinStack:
    """
    For my MinStack, the head always contains the node
    having the smallest value on the stack
    """

    class Node:
        def __init__(self, x, ptr):
            self.val = x
            self.next = ptr
            self.min = self

    def __init__(self):
        """
        initialize our MinStack
        """
        self.head = None

    def push(self, x: int) -> None:
        new_node = self.Node(x, self.head)
        # check if an item exists and if new node's
        # value is greater than our min mode's value
        if self.head and x > self.head.min.val:
            new_node.min = self.head.min
        self.head = new_node

    def pop(self) -> None:
        # make sure there is an item
        if self.head:
            self.head = self.head.next

    def top(self) -> int:
        if self.head:
            return self.head.val

    def get_min(self) -> int:
        return self.head.min.val
