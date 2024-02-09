# Example of linked list form in Json 
# head =  {
#             "value": 4, 
#             "next": { 
#                 "value": 10, 
#                 "next": {
#                     "value": 15, 
#                     "next": None
#                 }
#             }
#         }

# print(head["next"]["next"]) 

# since all the linked list functions involve creating a node we want to standardize that process 
class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    # create a node and initialize the new linked list 
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    # create a node and and add that node to the end 
    def append(self, value):
        new_node = Node(value)
        # check if self.head exists (all nodes could be removed) 
        if self.head is None: 
            #if there is no tail assume there is also no head 
            self.head = new_node
            self.tail = new_node
        else:
            #assign the pointer from none to new node 
            self.tail.next = new_node
            self.tail = self.tail.next
        # increment the length 
        self.length += 1 
        return True

    # removes the last item from the linked list
    def pop(self): 
        # if no nodes, return NOne 
        if self.length == 0:
            return None
        else:            
            # we need to consider the edge case of a single node
            # setting both to the first node here means we will evaluate the first node 
            # then when we increment we can just ensure Pre always gets set to temp and temp increments up
            # in the first loop iteration "pre" will not change in value, only temp will progress down the list  
            # assign both as temp values            
            w = self.head
            temp = self.head
            # check if temp.next is true (ie. not none)  iterate down the line   
            while(temp.next): 
                # set pre to current node 
                pre = temp
                # set temp to next node 
                temp = temp.next
            # once temp.next is None assign tail value to temp prev and change its next value to none  
            self.tail = pre 
            self.tail.next = None 
            self.length -= 1 
            # after the decrement, if the length is 0 we need to fix head and tail 
            if self.length == 0: 
                self.head = None 
                self.tail = None 
            return temp 
    
    def pop_first(self): 
        if self.length == 0: 
            return None 
        # create temp variable holding return 
        temp = self.head 
        # whether temp.next is none or a value this is still valid 
        self.head = temp.next
        # clearing node from list now that we've moved the head   
        temp.next = None 
        self.length -= 1 
        if self.length == 0: 
            self.tail = None
        return temp 


    # create a node and prepend that node at the beginning 
    def prepend(self, value): 
        new_node = Node(value)
        # in the case of empty linked list 
        if self.length == 0: 
            self.head == new_node
            self.tail == new_node
            self.length += 1  
            return True      
        # set the nead to the new node and point the new node to the original firs t
        new_node.next = self.head
        self.head = new_node
        self.length += 1 
        return True

    def get(self,value):
        if self.length == 0: 
            return None 
        if value >= self.length: 
            return None 
        
        temp = self.head 
        for _ in range(value):
            current = temp 
            temp = temp.next 
            

    def print_list(self): 
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next


# testing code 
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print_list()
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
my_linked_list.print_list()