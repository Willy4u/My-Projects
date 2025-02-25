class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr.next =Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next !=None):
            n = n.next
        return n.data

    def print_list(self):
        n = self.head
        while n !=None:
            print(n.data, end = ' =>')
            n = n.next
        print()



