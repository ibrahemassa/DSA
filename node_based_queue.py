class Node:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, val) -> None:
        node = Node(val)

        if not self.head:
            self.head = node
            self.tail = node
        
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
        self.size += 1
    
    def dequeue(self):
        if len(self) == 0:
            print("The queue is empty!")
            return

        data = self.head.val
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None

        self.size -= 1

        return data

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "The queue is empty!"
        cur = self.head
        temp = ''
        while cur.next:
            temp += f'{cur.val}->'
            cur = cur.next
        return temp + str(cur.val)
