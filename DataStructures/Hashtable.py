class HashTable: 
    def __init__(self, size = 7):
        # create a list of seven items and then populate it with None 
        self.data_map = [None] * size 

    def hash(self, key): 
        my_hash = 0 
        for letter in key: 
            # ord is an ordinal aka ascii number for each letter as we loop though key 
            # we use 23 because  its prime number 
            # modulo operator ensures we get a value less than the length ( for 7 result will be 0-6)
            my_hash = (my_hash + ord(letter) * 23) % len (self.data_map)
            return my_hash
        
    def print_table(self): 
        for i, val in enumerate(self.data_map):
            print(i , ": ", val)

    def set_item(self, key, value):
        index = self.hash(key)
        if self.data_map[index] == None:  
            # ony want to do this if empty list has not been initialized 
            self.data_map[index] = [] 
        self.data_map[index].append([key, value])

    def get_item(self, key): 
        index = self.hash(key)
        address = self.data_map[index] 
        if address == None:
            return None
        # for entry in address: 
        #     print(entry)  
        #     if entry[0] == key: 
        #         return entry[1]
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key: 
                return self.data_map[index][i][1]
        return None

    def get_keys(self):
        keys = []  
        for address in range(len(self.data_map)):
            if self.data_map[address]:
                for i in range(len(self.data_map[address])): 
                    keys.append(self.data_map[address][i][0])
        return keys 

            

my_hastable = HashTable(7)
my_hastable.set_item("nails", 1000)
my_hastable.set_item("bolts", 1300)
my_hastable.set_item("washers", 700)
my_hastable.set_item("lumber", 600)
my_hastable.print_table()
print(my_hastable.get_item("lumber")) 
print(my_hastable.get_item("washers")) 
print(my_hastable.get_item("maple syrup")) 
print(my_hastable.get_keys())