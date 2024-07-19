class LinkedList:
    def __init__(self):
        self.head = None

    def pop_back(self):
        # removes end item and returns its value
        pass

    def front(self):
        # get the value of the front item
        pass

    def back(self):
        # get the value of the end item
        pass

    def insert(self, index, value):
        # insert value at index, so the current item at that index is pointed to by the new item at the index
        pass

    def erase(self, index):
        # removes node at given index
        pass

    def value_n_from_end(self, n):
        # returns the value of the node at the nth position from the end of the list
        pass

    def reverse(self):
        # reverses the list
        pass

    def remove_value(self, value):
        # removes the first item in the list with this value
        pass

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # No need to implement, as described in the search results

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        # adds value to the top of the stack
        pass

    def pop(self):
        # removes top item and returns its value
        pass

    def peek(self):
        # returns the value of the top item
        pass

class Queue:
    def __init__(self):
        self.items = []
        self.tail = None

    def enqueue(self, value):
        # adds value at a position at the tail
        pass

    def dequeue(self):
        # removes front item and returns its value
        pass

    def peek(self):
        # returns the value of the front item
        pass
