class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, data) -> None:
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    def pop(self):
        if self.empty():
            raise Exception("The stack is empty!")
        if len(self) == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
        else:
            temp = self.head.data
            self.head = self.head.next
        self.size -= 1
        return temp
    
    def peek(self):
        return self.head.data
    
    def empty(self) -> bool:
        return len(self) == 0
    
    def search(self, target) -> bool:
        if self.empty():
            return False
        cur = self.head
        while cur:
            if cur.data == target:
                return True
            cur = cur.next
        return False
    
    def __str__(self) -> str:
        if self.empty():
            return 'None'
        cur = self.head
        temp = ''
        while cur.next:
            temp += f'{cur.data}->'
            cur = cur.next
        return temp + str(cur.data)

    def __len__(self) -> int:
        return self.size


#Testing

stack = Stack()
for i in range(5):
    stack.push(i)

print(f'Popped: {stack.pop()}')

print(stack)

print(stack.search(22))

print(stack.empty())

print(f'The length: {len(stack)}')