class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, task):
        node = Node(task)
        node.next = self.head
        self.head = node

    def to_list(self):
        curr, res = self.head, []
        while curr:
            res.append(curr.task)
            curr = curr.next
        return res
