class Hash_table:
    def __init__(self):
        self.max=100
        self.arr=[[] for _ in range (self.max)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash +=ord(char)
        return hash%100
    
    def __setitem__(self,key,val):
         h=self.get_hash(key)
         self.arr[h]=val
    
    def __getitem__(self,index):
        h=self.get_hash(index)
        return self.arr[h]
    
    

t=Hash_table()
t["march 6"]=310
t["march 7"]=420
t["march 9"]=370
t["march 14"]=267
t["march 43"]=412
print(t.arr)
print(t["march 7"])
    
    
    
    


