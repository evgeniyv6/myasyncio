

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self,x):
        self.stack.append(x)
        if self.min:
            if x < self.min[-1]: self.min.append(x)
            else: self.min.append(self.min[-1])
        else: self.min.append(x)

    def pop(self):
        self.min.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    print(minStack.top()) # return 0
    print(minStack.getMin()) # return -2