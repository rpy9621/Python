class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) >= 1:  # ✅ allow peek if at least 1 element
            return self.stack[-1]  # ✅ correct indexing
        return None
    
    def show(self):
        print(self.stack)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element:", s.peek())  # ✅ 30
s.pop()
s.show()  # ✅ [10, 20]
