class Node:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        node = Node(val=data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
    
    def delete(self, data):
        cur = self.head
        deleted = False
        if not cur:
            deleted = False
        elif cur.val == data:
            self.head = self.head.next
            self.head.prev = None
            deleted = True
        elif self.tail.val == data:
            self.tail = self.tail.prev
            self.tail.next = None
            deleted = True
        else:
            while cur:
                if cur.val == data:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    deleted = True
                    break
                cur = cur.next
        if deleted:
            self.size -= 1
        return deleted

    def insert_at_index(self, index, data):
        if index > len(self) or index < 0:
            raise IndexError("Index is out of range")

        node = Node(val=data)
        if index == 0:
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if not self.tail:
                self.tail = node
        elif index == len(self):
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            node.prev = cur.prev
            node.next = cur
            cur.prev.next = node
            cur.prev = node

        self.size += 1

    def search(self, data):
        return data in self.iter()

    def iter(self):
        cur = self.head
        while cur:
            temp = cur.val
            cur = cur.next
            yield temp
    
    def __len__(self):
        return self.size

    def __str__(self):
        the_list = '['
        cur = self.head
        while cur:
            the_list += f'{cur.val}, '
            cur = cur.next
        the_list = the_list[:-2] + ']'
        return the_list
    
    def __getitem__(self, index):
        if index > len(self)-1 or index < 0:
            raise IndexError("Index is out of range")

        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
