class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(x)
            self.tail = current.next

    def peek(self):
        return self.head.data

    def pop(self):
        desired = self.head.data
        new_head = self.head.next
        if new_head is None:
            self.head = None
            self.tail = None
        else:
            self.head.data = new_head.data
            self.head.next = new_head.next
        return desired

    def empty(self):
        if self.head is None:
            return True
        return False

class MyStack:

    def __init__(self, data = None):
        self.main = Queue()
        self.sub = Queue()


    def push(self, x: int) -> None:
        while not self.main.empty():
            self.sub.push(self.main.pop())
        self.main.push(x)
        while not self.sub.empty():
            self.main.push(self.sub.pop())


    def pop(self) -> int:
        return self.main.pop()


    def top(self) -> int:
        return self.main.peek()


    def empty(self) -> bool:
        return self.main.empty()




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
