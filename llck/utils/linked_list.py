class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def get(self):
      return self.data

    def __repr__(self):
        return self.get()

    def __str__(self):
        return self.get()

    def __eq__(self, other):
        return self.get() == other

    def __len__(self):
        return len(self.data)

    def __call__(self):
        return self.get()


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = nodes.pop(0)
            self.head = node
            for elem in nodes:
                node.next = elem
                node.previous = node
                node = node.next

    def add_last(self, elem):
        if not self.head:
            self.head = elem
            return
        for current_node in self:
            pass
        current_node.next = elem

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, item): 
        node = self.head
        count = 0
        while node is not None:
            if count == item: 
                return node
            else:
                count += 1
                node = node.next
        
    def __str__(self):
        return str(list(self))
