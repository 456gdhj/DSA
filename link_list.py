class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None

    def insert_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
          print("The link list is empty")
          return
    
        llstr=''
        itr=self.head
        while itr:
            llstr+= str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
           itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    
    
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
           

        if index==0:
            self.head=self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_atindex(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
    
        if index == 0:
            self.insert_beginning(data)
            return
    
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next
        
if __name__=='__main__':
    ll= linkedlist()
    ll.insert_values(["Mango","Banana","Apple","Coconutes"])
    
    ll.insert_atindex("fruits",1)
    ll.print()


        
