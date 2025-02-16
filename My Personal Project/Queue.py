class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def my_bag(self):
        print(self.items)




food = Queue()
food.enqueue('Eyram')
food.enqueue('Edem')
food.enqueue('Elikem')
food.enqueue('Dzifa')
food.my_bag()

food.dequeue()
food.my_bag()


