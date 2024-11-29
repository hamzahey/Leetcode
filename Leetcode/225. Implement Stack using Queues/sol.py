'''
225. Implement Stack using Queues
Solved
Easy
Topics
Companies
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 '''


from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Primary queue
        self.q2 = deque()  # Auxiliary queue

    def push(self, x: int) -> None:
        # Add the element to q1
        self.q1.append(x)

    def pop(self) -> int:
        # Move all elements except the last one to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Remove and return the last element from q1
        last = self.q1.popleft()
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return last

    def top(self) -> int:
        # Return the last element in q1
        return self.q1[-1]

    def empty(self) -> bool:
        # Check if q1 is empty
        return not self.q1


# Example input and output simulation
commands = ["MyStack", "push", "push", "top", "pop", "empty"]
arguments = [[], [1], [2], [], [], []]

# Simulate the commands
result = []
stack = None

for command, arg in zip(commands, arguments):
    if command == "MyStack":
        stack = MyStack()
        result.append(None)
    elif command == "push":
        stack.push(arg[0])
        result.append(None)
    elif command == "pop":
        result.append(stack.pop())
    elif command == "top":
        result.append(stack.top())
    elif command == "empty":
        result.append(stack.empty())

print(result)
