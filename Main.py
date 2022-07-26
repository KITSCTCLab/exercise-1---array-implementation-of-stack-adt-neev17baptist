import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        global top,l,size
        return self.top==-1

    def is_full(self): 
        global top,size
        return top==size-1

    def push(self, data):  #pushing a value if the empty
        if not self.is_full():
           print("The Stack is Full")
        else:
            top+=1
            l[top]=data
            
    def pop(self):  #popping out a value is the stack is not empty
        if not self.is_empty():
            print("THE STACK IS EMPTY")
        else:
            out=top
            top-=1
            return l.pop(out)
     
    def status(self): #Displaying the elements
       for i in range(size):
        print(i)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
