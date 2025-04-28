from collections import deque
class queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
pq = queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})    

print(pq.dequeue())