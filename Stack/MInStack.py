class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack  or val<=self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()