import data_structures.LinkedList as LinkedList
import data_structures.LinkedListNode as LinkedListNode


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
