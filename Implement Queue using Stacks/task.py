from collections import deque

class MyQueue:

    def __init__(self):
        self.line = deque()

    def push(self, x: int) -> None:
        self.line.appendleft(x)


    def pop(self) -> int:
        return self.line.pop()


    def peek(self) -> int:
        index = 0
        for elm in self.line:
            if index == len(self.line) - 1:
                return elm
            index += 1


    def empty(self) -> bool:
        if not self.line:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
