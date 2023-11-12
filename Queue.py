class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def offer(self, item):
        self.queue.append(item)
        return True
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        print('The queue is empty!')
    
    def is_empty(self):
        return len(self.queue) == 0

    def poll(self):
        if not self.is_empty():
            return self.queue.pop(0)
        print('The queue is empty!')

    def contains(self, target):
        return target in self.queue
    
    def length(self):
        return len(self.queue)
    
    def __str__(self):
        if self.is_empty():
            return "The queue is empty!"
        else:
            return '->'.join(map(str, self.queue)) + '->None'


# Testing the Queue class:


# q = Queue()

# q.offer(34)
# q.offer(3)
# q.offer('n')
# q.offer('hi')

# print(q.offer('queue'))

# q.poll()

# print(q)

# print(q.length())