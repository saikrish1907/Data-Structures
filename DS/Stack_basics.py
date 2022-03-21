'''

LIFO functionality 
The functions associated with stack are:

empty() – Returns whether the stack is empty – Time Complexity: O(1)
size() – Returns the size of the stack – Time Complexity: O(1)
top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

'''
# most function are similar to list. 
#Other than list we can import from package and use it 
#Collections.deque
#queue.LifoQueue

stack = []

n = int(input())
for i in range(n):
    stack.append(i)

print(stack)

stack.pop(0)
print(stack)



