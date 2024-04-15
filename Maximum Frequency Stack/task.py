from collections import deque

class Element:
    def __init__(self, value, number = 1):
        self.value = value
        self.number = number

class FreqStack:
    def __init__(self):
        self.elements = deque()

    def push(self, val: int) -> None:
        new_elm = Element(val)
        for elm in self.elements:
            if elm.value == new_elm.value:
                new_elm.number += (elm.number + 1)
                break
        self.elements.appendleft(new_elm)


    def pop(self) -> int:
        biggest_num = -1
        value = None
        for elm in self.elements:
            if elm.number > biggest_num:
                biggest_num = elm.number
                value = elm
        self.elements.remove(value)
        return value.value