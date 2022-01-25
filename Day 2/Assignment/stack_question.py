#Taking no.of elemets in Stack
n=int(input())

#Creating a class
class Stack:
    def __init__(self):
        self.stack1=[]
    def push(self,x):
        return self.stack1.append(x)
    def pop(self):
        self.stack1.pop()
        return
    def maximum(self):
        return max(self.stack1)

stack_object=Stack()
for _ in range(n):
    # taking query number
    a=list(map(int,input().split()))
    
    # pushing element
    if a[0]==1:
        stack_object.push(a[1])
    #poping element
    elif a[0]==2:
        stack_object.pop()
    #printing max element
    else:
        print(stack_object.maximum())