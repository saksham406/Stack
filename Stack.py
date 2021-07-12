from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,data):
        return self.container.append(data)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def check_is_empty(self):
        return len(self.container)==0

    def size_of(self):
        return len(self.container)

s=Stack()
s.push(1)
s.push(2)
print(s.container)
print(s.pop())
print(s.peek())
print(s.check_is_empty())
print(s.size_of())
print(s.container)



    
