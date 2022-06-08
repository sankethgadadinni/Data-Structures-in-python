#There are various ways to implement a queue in Python. 
#This file covers the implementation of queue using data structures and modules from Python library.
#Queue in Python can be implemented by the following ways:


#1) List
#2) collections.deque
#3) queue.Queue



# Python program to 
# demonstrate queue implementation
# using list


queue = []


queue.append('a')
queue.append('b')
queue.append('c')

print("Initial Queue : ", queue)

# pop() function to pop element from stack but pop(0) removes eleemnts from left in FIFo order

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("Final Queue : ", queue)




                                   ###################################################


# Python program to
# demonstrate queue implementation
# using collections.deque


from collections import deque


queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial Queue : ", queue)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("Final Queue : ", queue)





                                   ###################################################


# Python program to
# demonstrate implementation of
# queue using queue module

from queue import Queue

q = Queue(maxsize=3)

q.put('a')
q.put('b')
q.put('c')


print("Initial Queue Size: ", q.full())

print(q.get())
print(q.get())
print(q.get())

print("Final Queue Size : ", q.empty())





                                   ###################################################

# We can write a class and add push and pop functions to implement queue in python


class Queue:
    def __init__(self):

        self.queue = []

    
    def push(self, data):
        if data not in self.queue:
            self.queue.append(data)

            return ("Data pushed to Queue")
        
        else:

            return ("Data Found in the Queue")

    
    def pop(self):

        if len(self.queue) <= 0:
            print("No data found in Queue")

        else:
            return self.queue.pop(0)

    
    def printQueue(self):
        print("Current Queue : ", self.queue)




if __name__ == '__main__':
    
    q = Queue()
    q.push('Monday')
    q.push('Tuesday')
    q.push('Wednesday')

    q.printQueue()

    q.pop()
    q.pop()
    q.pop()

    q.printQueue()
