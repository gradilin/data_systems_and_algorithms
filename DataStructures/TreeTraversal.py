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
    
    def breadth_first_search(self): 
        current_node = self.root
        queue = [] 
        results = [] 
        queue.append(current_node)

        while len(queue) > 0: 
            current_node = queue.pop()
            results.append(current_node.value)
            if current_node.left: 
                queue.append(current_node.left)
            if current_node.right: 
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self): 
        results = [] 

        def traverse(current_node): 
            #appending to global results list 
            results.append(current_node.value)
            # traverse left 
            if current_node.left: 
                traverse(current_node.left)
            #traverse right 
            if current_node.right: 
                traverse(current_node.right)

        traverse(self.root )
        return results

    def dfs_post_order(self): 
        results = [] 

        def traverse(current_node): 
            if current_node.left: 
                traverse(current_node.left)
            if current_node.right: 
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results 

    # this oroduces a numerically ordered list 
    def dfs_in_order(self): 
        results = [] 

        def traverse(current_node):
            if current_node.left: 
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right: 
                traverse(current_node.right)
        
        traverse(self.root)
        return results 
    





my_bst = BinarySearchTree()
my_bst.insert(50)
my_bst.insert(72)
my_bst.insert(18)
my_bst.insert(41)
my_bst.insert(65)
my_bst.insert(12)
my_bst.insert(88)
my_bst.insert(91)
my_bst.insert(56)

# print(my_bst.bread_first_search())
print(my_bst.dfs_pre_order())
