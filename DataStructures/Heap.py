# Heaps: 
# very efficient for finding highest value node in a list 

class MaxHeap: 
    def __init__(self):
        self.heap = [] 


    def _left_child(self, index): 
        # 0 index list 
        return 2 * index + 1 
        # # 1 indexed list   
        # return 2 * index 
    
    def _right_child(self, index): 
        # 0 index list 
        return 2 * index + 2 
        # # 1 indexed list   
        # return 2 * index + 1
    
    def _parent(self, index): 
        # 0 index list 
        return (index - 1) // 2  
        # 1 indexed list          
        # return index // 2
    
    def _sink_down(self, index): 
        max_index = index
        heap_length = len(self.heap)
        while True: 
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # check to see if value exists and then evaluate whether value is greater 
            if left_index < heap_length and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
                
            # check to see if value exists and then evaluate whether value is greater 
            if right_index < heap_length and self.heap[right_index] > self.heap[max_index]: 
                    max_index = right_index
            
            # if the max index is not the curent idex, its swap o'clock 
            if max_index!= index: 
                self.swap(index, max_index)
                index = max_index 
            else: 
                return 

        
    
    def swap(self, index1, index2): 
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]  

    def insert(self, value): 
        self.heap.append(value)
        index = len(self.heap) - 1

        while self.heap[self._parent(index)] < value and index > 0: 
            self.swap(index, self._parent(index)) 
            index = self._parent(index)

    def remove(self, index): 
        length = len(self.heap)
        if length == 0: 
            return None 
        if length == 1: 
            return self.heap.pop()

        # getting value and doing the value substitution 
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value 
            



my_heap = MaxHeap()

my_heap.insert(28)
my_heap.insert(19)
my_heap.insert(72)
my_heap.insert(56)
my_heap.insert(91)
my_heap.insert(43)

print(my_heap.heap)

my_heap.remove(0)
print(my_heap.heap)

my_heap.remove(0)
print(my_heap.heap)

