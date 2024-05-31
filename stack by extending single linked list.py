from Assign3 import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.count_item=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.count_item+=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.count_item-=1
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("stack is empty")
    def size(self):
        return self.item_count
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("the top element",s1.peek())
print(s1.pop())
print()

        
       
    