class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return hex(id(self))

    def __add__(self, other):
        if isinstance(other, LinkedListNode):
            self.next = other
            return self
        else:
            raise TypeError
