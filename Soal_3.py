class Queue:
    def _init_(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def remove_at(self, index):
        if 0 <= index < len(self.queue):
            return self.queue.pop(index)
        else:
            return None

    def head(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None 

    def display(self):
        print("Queue:", self.queue)

    def is_empty(self):
        return len(self.queue) ==0
