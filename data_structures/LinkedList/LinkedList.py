from data_structures.iterators import LinkedListIterator
from data_structures import LinkedListNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        val_list = [str(node.val) for node in self]
        return f'LinkedList {hex(id(self))}\n' + ' -> '.join(val_list)

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        return LinkedListIterator(self)

    def __add__(self, other):
        last = self.last()
        if isinstance(other, LinkedListNode):
            last.next = other
        elif isinstance(other, LinkedList):
            last.next = other.head
        else:
            raise TypeError

    def add(self, n):
        try:
            self.__add__(n)
        except TypeError:
            self.__add__(LinkedListNode(val=n))

    def last(self):
        for node in self:
            if not node.next:
                return node
