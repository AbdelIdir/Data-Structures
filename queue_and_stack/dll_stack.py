import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        newNode = DoublyLinkedList(value)

        if not self.first:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            self.first = newNode
            self.first.next = temp

        return self.size + 1

    def pop(self):
        pass

    def len(self):
        pass


stack = Stack()

stack.push(30)
