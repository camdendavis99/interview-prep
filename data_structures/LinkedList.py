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

    def add(self, val):
        node = LinkedListNode(val=val)
        self + node

    def last(self):
        for node in self:
            if not node.next:
                return node


class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return hex(id(self))

    def __add__(self, other):
        if isinstance(other, LinkedListNode):
            self.next = other
        elif isinstance(other, LinkedList):
            self.next = other.head
        else:
            raise TypeError


class LinkedListIterator:
    def __init__(self, node):
        if isinstance(node, LinkedListNode):
            self.node = node
        elif isinstance(node, LinkedList):
            self.node = node.head
        else:
            raise TypeError

    def __next__(self):
        if self.node:
            cur_node = self.node
            self.node = self.node.next
            return cur_node
        raise StopIteration
