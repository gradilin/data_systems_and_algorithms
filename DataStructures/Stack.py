class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 
    
class Stack: 
    def __init__(self, value): 
        new_node = Node(value)
        self.top = new_node
        self.height = 1 

    def print_stack(self): 
        temp = self.top 
        while temp is not None: 
            print(temp.value)
            temp = temp.next 
    
    def push(self, value): 
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node 
        self.height += 1 

    def pop(self): 
        if self.height < 1: 
            return None 
        temp = self.top 
        self.top = temp.next
        temp.next = None 
        self.height -= 1 
        return temp 
        

my_stack = Stack(10)
my_stack.push(9)
my_stack.push(8)
my_stack.push(7)

print(my_stack.pop())
my_stack.print_stack()