from collections import deque
class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

#pop remove element from stack and show
    def pop(self):               
        return self.container.pop()

    def peek(self):
        return self.container[-1]

s=stack()
s.push('https://www.cnn.com/')
s.push ('https://www.cnn.com/world')
s.push('https://www.cnn.com/india')
s.push('https://www.cnn.com/china')

print(s.peek())

print(s.pop())

print(s.pop())
print(stack)

