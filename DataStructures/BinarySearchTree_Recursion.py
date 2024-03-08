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


    #actual recursive part of the recursive contains 
    def __r_contains(self, current_node, value): 
        # if node doesnt exist return false 
        if current_node == None: 
            return False 
        # if value matches return true 
        if value == current_node.value: 
            return True 
        if value < current_node.value: 
            return self.__r_contains(current_node.left, value)
        if value > current_node.value: 
             return self.__r_contains(current_node.right, value)
    
    # recursive contains 
    def r_contains(self, value): 
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value): 
        # if no value for node 
        if current_node == None: 
            return Node(value)
        if current_node.value > value: 
            # since we are assiging value here you can return a node in the code previous 
            current_node.left = self.__r_insert(current_node.left, value)
        if current_node.value < value: 
            current_node.right = self.__r_insert(current_node.right, value)        
        return current_node

    def r_insert(self, value):  
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        # if node doesnt exist we need to return the None value to satify recursion call  
        if current_node == None:
            return None 
        # traversing left 
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        # traversing right 
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # if value = current_node.value - we foudn the node to remove 
        else: 
            # leaf node 
            if current_node.left == None and current_node.right == None: 
                return None 
            # node with right value but no left 
            elif current_node.right == None:
                # returning the value to the right as the next value for the previous call 
                current_node = current_node.left  
            # node with right value but no left 
            elif current_node.left == None:
                # returning the value to the left as the next value for the previous call 
                current_node = current_node.right 
            else: 
                sub_tree_min = self.min_value(current_node)
                current_node.value = sub_tree_min
                # this value will guaranteed to not have the a child node on each side because its the minimum value whic is always open on left 
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            #once existing node has no pointer it gets GC'ed 
            return current_node
            # node with both righ and left child values             
        # once we have traversed to the bottom 
        return current_node

    def delete_node(self, value): 
        root_node = self.root
        self.__delete_node(root_node, value)
        return

    # iterative not recursive 
    def min_value(self, current_node): 
        # lowest value is always the bottom left of tree 
        while current_node.left is not None: 
            current_node = current_node.left 
        #when current.left is None return the calue 
        return  current_node.value 



    # def contains(self, value): 
    #     temp = self.root
    #     while temp: 
    #         if value == temp.value: 
    #             return True 
    #         if value > temp.value:
    #             temp = temp.right
    #         else: 
    #             temp = temp.left 
    #     return False

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
