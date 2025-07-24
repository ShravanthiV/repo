class SimpleQueueTwoStacks:
    def __init__(self):
        self.stack_in = []  
        self.stack_out = []  
    def enqueue(self, item):
        self.stack_in.append(item)
    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            return None  
    def is_empty(self):
        return not self.stack_in and not self.stack_out
q = SimpleQueueTwoStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue()) 
