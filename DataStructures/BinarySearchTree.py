class Node: 
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self): 
        self.root = None 

    def insert(self, value): 
        new_node = Node(value)
        if self.root is None: 
            self.root = new_node
            return True
        temp = self.root
        while True: 
            if temp.value == new_node.value: 
                return False 
            if new_node.value < temp.value: 
                if temp.left == None: 
                    temp.left = new_node
                    return True 
                temp = temp.left 
            if new_node.value > temp.value: 
                if temp.right == None: 
                    temp.right = new_node
                    return True 
                temp = temp.right               

    def contains(self, value): 
        temp = self.root
        while temp: 
            if value == temp.value: 
                return True 
            if value > temp.value:
                temp = temp.right
            else: 
                temp = temp.left 
        return False

my_bst = BinarySearchTree()
my_bst.insert(46)
my_bst.insert(29)
my_bst.insert(18)
my_bst.insert(72)
my_bst.insert(72)
my_bst.insert(81)


print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)
print(my_bst.contains(8))
