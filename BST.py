from collections import deque

class Node:
    def __init__(self, data=None, left_child=None, right_child=None) -> None:
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return
        parent = None
        current = self.root
        while True:
            parent = current
            if current.data > data:
                current = current.left_child
                if current == None:
                    parent.left_child = node
                    return
            else:
                current = current.right_child
                if current == None:
                    parent.right_child = node
                    return
    
    def get_parent(self, data):
        parent = None
        current = self.root
        if current == None:
            return (parent, None)
        while current:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            elif current.data < data:
                parent = current
                current = current.right_child
        return (parent, current)
    
    def delete(self, data):
        parent, node = self.get_parent(data)
        if parent == None and node == None:
            return False
        if node.right_child and node.left_child:
            children = 2
        elif node.right_child == None and node.left_child == None:
            children = 0
        else:
            children = 1
        
        if children == 0:
            if parent:
                if parent.right_child == node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root = None
        elif children == 1:
            if node.right_child:
                next_node = node.right_child
            else:
                next_node = node.left_child
            if parent:
                if parent.left_child == node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root = next_node
        else:
            leftmost_parent = node
            leftmost = node.right_child
            while leftmost.left_child:
                leftmost_parent = leftmost
                leftmost = leftmost.left_child
            node.data = leftmost.data
            if leftmost_parent.right_child == leftmost:
                leftmost_parent.right_child = leftmost.right_child
            else:
                leftmost_parent.left_child = leftmost.right_child
    
    def search(self, data):
        current = self.root
        if current == None:
            return False
        while current:
            if current.data == data:
                return True
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
        return False

    def in_order(self, root):
        current = root
        if root == None:
            return
        self.in_order(current.left_child)
        print(current.data)
        self.in_order(current.right_child)
    
    def pre_order(self, root):
        current = root
        if root == None:
            return
        print(current.data)
        self.pre_order(current.left_child)
        self.pre_order(current.right_child)
    
    def post_order(self, root):
        current = root
        if current == None:
            return
        self.post_order(current.left_child)
        self.post_order(current.right_child)
        print(current.data)
    
    def breadth_first_traverse(self):
        nodes = []
        queue = deque([self.root])

        while len(queue) > 0:
            node = queue.popleft()
            nodes.append(node.data)

            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)
        return nodes

#Testing:
bst = BST()

elements = [5, 3, 7, 2, 4, 6, 8]
for element in elements:
    bst.insert(element)


print(bst.search(3))

bst.delete(3)
print(bst.search(3))

print('In order:')
bst.in_order(bst.root)

print('Pre order:')
bst.pre_order(bst.root)

print('Post order:')
bst.post_order(bst.root)

print('Breadth: ')
print(bst.breadth_first_traverse())
