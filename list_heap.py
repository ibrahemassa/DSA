class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float_node(self, n):
        while n // 2 > 0:
            if self.heap[n] < self.heap[n // 2]:
                self.heap[n], self.heap[n // 2] = self.heap[n // 2], self.heap[n]
            n //= 2

    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.float_node(self.size)

    def min_index(self, n):
        if n * 2 + 1 > self.size:
            return n * 2
        elif self.heap[n*2+1] > self.heap[n*2]:
            return n * 2
        else:
            return n * 2 + 1

    def sink(self, n):
        while n*2 <= self.size:
            mindex = self.min_index(n)
            if self.heap[mindex] < self.heap[n]:
                self.heap[n], self.heap[mindex] = self.heap[mindex], self.heap[n]
            n = mindex

    def pop(self):
        data = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.sink(1)
        return data

