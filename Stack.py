class Stack:
    def __init__(self, stack = []):
        self.stack = stack

    def pop(self):
        try:
            return self.stack.pop()
        except:
            print('Stack is empty!')

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        try:
            return self.stack[-1]
        except:
            print('Stack is empty!')

    def is_empty(self):
        return len(self.stack) == 0
    
    def search(self, item):
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[len(self.stack)-i-1] == item:
                return i
        return -1
