class Stack:
    def __init__(self, limit_stack): #Hàm tạo để khởi tạo Stack với limit nhất định
        self.limit_stack = limit_stack
        self.stack = []
        self.count = 0

    def push(self, item): #Hàm thêm một phần tử vào Stack
        if self.isFull():
            print("Stack đầy")
        else:
            self.stack.append(item)
            self.count += 1

    def pop(self):
        if self.isEmpty():
            print("Stack trống")
            return None
        else:
            self.count -= 1
            return self.stack.pop()

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.limit_stack

    def count(self):
        return self.count

    def printStack(self):
        print("Nội dung của Stack:", self.stack)

stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.printStack()  
print("Số phần tử của Stack:", stack.pop())  
stack.printStack()  