from __future__ import annotations
from singly_linked_list import SinglyLinkedList
from typing import TypeVar

T = TypeVar('T')

class Queue:
    def __init__(self: Queue, firstElem : T) -> Queue:
        if firstElem:
            self.list = SinglyLinkedList()
            self.offer(firstElem)
        else:
            self.list = SinglyLinkedList()

    def size(self: Queue) -> int:
        return self.list.size

    def isEmpty(self: Queue) -> bool:
        return self.size() == 0

    def peek(self: Queue) -> T:
        if self.isEmpty():
            raise RuntimeError('Queue Empty')
        return self.list.peekFirst()

    def poll(self: Queue) -> T:
        if self.isEmpty():
            raise RuntimeError('Queue Empty')
        return self.list.removeFirst()

    def offer(self: Queue, elem: T) -> None:
        self.list.addLast(elem)




if __name__ == '__main__':
    queue = Queue(5)
    for i in range(5):
        queue.offer(i)

    for i in range(3):
        print(queue.poll())
