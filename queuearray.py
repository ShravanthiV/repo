class SimpleQueueArray:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None  
    def is_empty(self):
        return len(self.items) == 0

q = SimpleQueueArray()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue()) 
         
