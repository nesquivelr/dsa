from __future__ import annotations
from typing import TypeVar
from singly_linked_list import SinglyLinkedList


T = TypeVar('T')


class Stack:
    def __init__(self: Stack, firstElem: T = None):
        if firstElem:
            self.list = SinglyLinkedList()
            self.push(firstElem)
        else:
            self.mlist = SinglyLinkedList()

    def size(self: Stack) -> int:
        return self.list.size

    def isEmpty(self: Stack) -> bool:
        return self.size() == 0

    def push(self: Stack, elem: T) -> None:
        self.list.addLast(elem)

    def pop(self: Stack) -> T:
        if self.isEmpty():
            raise IndexError()
        return self.list.removeLast()

    def peek(self: Stack) -> T:
        if self.isEmpty():
            raise IndexError()
        return self.list.peekLast()


if __name__ == '__main__':
    stack = Stack(5)
    for i in range(5):
        stack.push(i)
        print(stack.peek())
    for i in range(3):
        print(stack.pop())
