class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beg(self, val):
        node = Node(val=val, next=self.head)
        self.head = node
    
    def append(self, val):
        node = Node(val=val, next=None)
        if self.head == None:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    
    def print_list(self):
        if self.head == None:
            print('The list is empty!')
            return

        cur = self.head
        the_list = ''
        while cur:
            the_list += f'{cur.val}->'
            cur = cur.next
        the_list += 'None'
        print(the_list)

    def insert_values(self, values):
        for v in values:
            self.append(v)
    
    def length(self):
        c = 0
        cur = self.head
        while cur:
            c += 1
            cur = cur.next
        return c

    def remove(self, index):
        if index >= self.length() - 1 or index < 0:
            print("Out of index!")
            return

        if index == 0:
            self.head = self.head.next
            return

        cur = self.head
        cur_index = 0
        while cur_index < index-1:
            cur = cur.next
            cur_index += 1
        cur.next = cur.next.next
    
    def insert_at(self, index, val):
        if index >= self.length() - 1 or index < 0:
            print("Out of index!")
            return
        if index == 0:
            old_head = self.head
            temp = Node(val=val, next=old_head)
            self.head = temp
            return

        cur = self.head
        cur_index = 0
        temp = Node(val=val)
        while cur_index < index-1:
            cur = cur.next
            cur_index += 1
        temp.next = cur.next
        cur.next = temp


my_list = LinkedList()

for i in range(2, 7):
    my_list.append(i**2)

my_list.insert_values(['a', 'b'])

my_list.print_list()

print(f'Length: {my_list.length()}')

my_list.remove(0)

my_list.print_list()

print(f'Length: {my_list.length()}')

my_list.insert_at(3, 'yes')

my_list.print_list()

