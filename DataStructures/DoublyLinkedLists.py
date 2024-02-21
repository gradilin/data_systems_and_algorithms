class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 

class DoublyLinkedList: 
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def print_list(self):
        temp = self.head 
        while temp: 
            print(temp.value)
            temp = temp.next 

    def append(self, value): 
        new_node = Node(value)
        if self.head is None: 
            self.head == new_node
            self.tail == new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        self.length += 1
        return True
        
    def prepend(self, value): 
        new_node = Node(value)
        if self.length is 0: 
            self.head == new_node
            self.tail == new_node
        else: 
            new_node.next = self.head 
            self.head = new_node
        self.length += 1 
        return True  

    def pop(self):
        if self.length == 0: 
            return None 
        temp = self.tail

        if self.length == 1: 
            self.tail = None 
            self.head = None
        else: 
            self.tail = self.tail.prev  
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1 
        return temp 
    
    def pop_first(self): 
        if self.length == 0: 
            return None
        temp = self.head
        if self.length == 1: 
            self.head = None 
            self.tail = None 
        else: 
            self.head = temp.next 
            temp.next = None 
            self.head.prev = None 
        self.length -= 1 
        return temp 

    def get(self, index): 
        if index < 0 or index >= self.length: 
            return None 
        
        # deciding which end of the linked list to approach from based on the index and the length 
        if index > (self.length/2): 
            temp = self.tail 
            # range(start, stop, step)
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev 
        else: 
            temp = self.head 
            for _ in range(index):
                temp = temp.next
        return temp

    def set(self, index, value): 
        temp = self.get(index)
        if temp is not None: 
            temp.value = value
            return True 
        return False 
        
    def insert(self, index, value): 
        if index < 0 or index > self.length: 
            return False 
        if index == 0: 
            return(self.prepend(value))
        if self.length == index: 
            return(self.append(value))
        
        new_node = Node(value)
        temp = self.get(index)
        prev = temp.prev 

        # setting the "before" pointers 
        prev.next = new_node
        new_node.prev = temp.prev 
        #setting the "after" pointers  
        temp.prev = new_node
        new_node.next = temp 
        #incrementing length 
        self.length += 1 
        return True 
    
    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return False 
        if index == 0: 
            return self.pop_first()
        if index == self.length - 1: 
            return self.pop()

        bad_node = self.get(index)
        before = bad_node.prev
        after = bad_node.next 

        before.next = after
        after.prev = before 
        bad_node.prev = None
        bad_node.next = None  
        self.length -= 1 
        return True 


    def swap_first_last(self): 
        if self.length <= 1: 
            return True
        #temp = self.head.value  
        #self.head.value = self.tail.value
        #self.tail.value = temp 
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True  



my_dll = DoublyLinkedList(6)
my_dll.append(5)
my_dll.append(4)
my_dll.append(3)
my_dll.append(2)
my_dll.append(1)
my_dll.insert(2,2222)
my_dll.set(4,69)
my_dll.print_list()

my_dll.remove(2)
my_dll.print_list()

# my_dll.pop()
# my_dll.print_list()