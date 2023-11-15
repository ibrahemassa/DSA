class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert_at_beg(self, val):
        node = Node(val=val, next=self.head)
        self.head = node
    
    def append(self, val):
        node = Node(val=val, next=None)
        if self.head == None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node
    
    def __str__(self):
        if self.head == None:
            return 'The list is empty!'

        cur = self.head
        the_list = ''
        while cur:
            the_list += f'{cur.val}->'
            cur = cur.next
        the_list += 'None'
        return the_list

    def insert_values(self, values):
        for v in values:
            self.append(v)
    
    def __len__(self):
        c = 0
        cur = self.head
        while cur:
            c += 1
            cur = cur.next
        return c

    def remove(self, index):
        if index > len(self) - 1 or index < 0:
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
        if index == len(self) - 1:
            self.tail = cur

    
    def insert_at(self, index, val):
        if index > len(self) - 1 or index < 0:
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
        if index == len(self) - 1:
            self.tail = temp


# my_list = LinkedList()

# for i in range(2, 7):
#     my_list.append(i**2)

# my_list.insert_values(['a', 'b'])

# print(my_list)

# print(f'Length: {len(my_list)}')

# my_list.remove(0)

# print(my_list)

# print(f'Length: {len(my_list)}')

# my_list.insert_at(3, 'yes')

# print(my_list)

