class MyStack:

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
            current.next = MyStack(x)


    def pop(self) -> int:
        current = self
        if current.next is None:
            desired = self.data
            self.data = None
            self.next = None
            return desired

        while current.next.next:
            current = current.next
        desired = current.next.data
        current.next = None
        return desired


    def top(self) -> int:
        current = self
        while current.next:
            current = current.next
        return current.data


    def empty(self) -> bool:
        if self.data is None:
            return True
        return False




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()