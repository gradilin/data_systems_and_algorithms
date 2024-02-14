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
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # create a node and and add that node to the end
    def append(self, value):
        new_node = Node(value)
        # check if self.head exists (all nodes could be removed)
        if self.head is None:
            # if there is no tail assume there is also no head
            self.head = new_node
            self.tail = new_node
        else:
            # assign the pointer from none to new node
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
            pre = self.head
            temp = self.head
            # check if temp.next is true (ie. not none)  iterate down the line
            while temp.next:
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

    def get(self, index):
        # index cant be greater then the length, or less than 0 
        #checks all the edge cases 
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # range already calulates the proper index 
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value): 
        # referencing the function written just above 
        temp = self.get(index) 
        if temp is not None:
            temp.value = value 
            return True 
        return False
        

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert(self, index, value): 
        #edge cases 
        # out of bounds error 
        if index < 0 or index > self.length: 
            return False 
        # straight prepend 
        if index == 0: 
            return self.prepend(value)
        #straight append
        if index == self.length:
            return self.append(value)
        #logic 
        new_node = Node(value)
        # use the get method to find the node before and affter the index 
        prev = self.get(index -1)
        # insert the new node by pointing the previous node at new node and the new node at the next node
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1 
        return True
    
    def remove(self, index): 
        # edge cases index out of bounds or empty list 
        if index < 0 or index >= self.length:
            return None
        # first index
        if index == 0: 
            return self.pop_first()
        #last index 
        if index == self.length -1: 
            return self.pop()
        prev = self.get(index - 1)
        # assigning the index "next value" to the previous node 
        temp = prev.next
        prev.next = temp.next 
        temp.next = None 
        self.length -= 1 
        return temp.value
    
    def reverse(self): 
        # checking for empty list 
        if self.length == 0: 
            return True
        # setting temp to hold original beginning of list 
        temp = self.head 
        # reversing head an tail 
        self.head = self.tail
        self.tail = temp
        # getting next position in linked list before reversing node  
        temp_prev = None 
        while temp is not None: 
            temp_next = temp.next
            temp.next = temp_prev
            temp_prev = temp
            temp = temp_next
        return True   
         

# testing code
my_linked_list = LinkedList(11)
my_linked_list.pop()
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)
# my_linked_list.set_value(2,29)
my_linked_list.reverse()
my_linked_list.print_list()

