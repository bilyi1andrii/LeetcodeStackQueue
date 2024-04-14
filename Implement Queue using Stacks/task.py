class MyQueue:

    def __init__(self, data = None):
        self.data = data
        self.next = None

    def push(self, x: int) -> None:
        if self.data is None:
            self.data = x
        else:
            current = self
            while current.next:
                current = current.next
            current.next = MyQueue(x)



    def pop(self) -> int:
        desired = self.data
        new_head = self.next
        if new_head is None:
            self.data = None
            self.next = None
        else:
            self.data = new_head.data
            self.next = new_head.next
        return desired


    def peek(self) -> int:
        return self.data


    def empty(self) -> bool:
        if self.data is None:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()