class hash_table:
    def __init__(self):
        self.max=100
        self.arr=[[] for _ in range (self.max)]
    
    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash%100
    
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                self.arr[h][idx]=(key,value)
                return
            
        self.arr[h].append((key,value))
    
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
            
        return None
    
h=hash_table()
h["march 6"]=130
h["march 7"]=120
h["march 11"]=150
h["march 17"]=170
h["march 17"]=190
h["march 25"]=110

print(h["march 17"])
print(h.arr)
            
    


        