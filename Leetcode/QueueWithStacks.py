class MyQueue:
    def __init__(self):
        self.queue_stack = []
        self.hold_stack = []
        
    def push(self, x: int) -> None:
        
        if not self.queue_stack:
            self.queue_stack.append(x)
        else:
            while self.queue_stack:
                self.hold_stack.append(self.queue_stack.pop())
            self.queue_stack.append(x)
            while self.hold_stack:
                self.queue_stack.append(self.hold_stack.pop())

    def pop(self) -> int:
        return self.queue_stack.pop()
        
    def peek(self) -> int:
        return self.queue_stack[len(self.queue_stack) -1]

    def empty(self) -> bool:
        
        return len(self.queue_stack) > 0