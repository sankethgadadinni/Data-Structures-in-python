
#There are various ways from which a stack can be implemented in Python. 
#This file contains implementation of a stack using data structures and modules from the Python library. 
#Stack in Python can be implemented using the following ways:

#1) List
#2) collections.deque
#3) queue.LifoQueue



# Python program to
# demonstrate stack implementation
# using list



stack = []


stack.append('a')
stack.append('b')
stack.append('c')

print("Initial Stack : ", stack)


# pop() function to pop
# element from stack in
# LIFO order


print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Final Stack : ", stack)


                                      ########################################################   



# Python program to
# demonstrate stack implementation
# using collections.deque


from collections import deque


stack = deque()


stack.append('a')
stack.append('b')
stack.append('c')


print("Initial Stack : ",stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())


print("Final Stack : ", stack)


                                      ########################################################   



# Python program to
# demonstrate stack implementation
# using queue module


from queue import LifoQueue

stack = LifoQueue(maxsize=3)

stack.put('a')
stack.put('b')
stack.put('c')

print("Initial Stack Size : ", stack.full())

print(stack.get())
print(stack.get())
print(stack.get())

print("Final Stack Size : ", stack.empty())




                                      ########################################################   


# We can create a class and add function such as push and pop to implement stack in python



class Stack:
    def __init__(self):

        self.stack = []

    
    def push(self, data):

        if data not in self.stack:
            self.stack.append(data)

            return("Data pushed to the Stack")
        
        else:
            
            return("Data already exists")

    
    def pop(self):

        if len(self.stack) <= 0:
            return("Data not found in Stack")

        else:
            
            return self.stack.pop()


    
    def printStack(self):

        print("Current Stack : ", self.stack)




if __name__ == '__main__':

    stk = Stack()
    stk.push('Monday')
    stk.push('Tuesday')
    stk.push('Wednesday')

    stk.printStack()

    stk.pop()
    stk.pop()
    stk.pop()

    stk.printStack()

