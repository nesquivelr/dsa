from __future__ import annotations
from typing import TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, datan: T, nextn: Node = None) -> Node:
        self.data = datan
        self.next = nextn

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self) -> SinglyLinkedList:
        self.head = None
        self.tail = None
        self.size = 0

    def clear(self):
        trav = self.head
        while trav:
            tmp = trav.next
            del(trav)
            trav = tmp
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def add(self, elem: T) -> None:
        self.addLast(elem)

    def addFirst(self, elem: T):
        if self.isEmpty():
            self.head = self.tail = Node(elem, None)
        else:
            new_node = Node(elem, self.head)
            self.head = new_node
        self.size += 1

    def addLast(self, elem: T) -> None:
        if self.isEmpty():
            self.head = self.tail = Node(elem, None)
        else:
            new_node = Node(elem, None)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def peekFirst(self) -> T:
        if self.isEmpty():
            raise RuntimeError('Empty list')
        else:
            return self.head.data

    def peekLast(self) -> T:
        if self.isEmpty():
            raise RuntimeError('Empty list')
        else:
            return self.tail.data

    def removeFirst(self) -> T:
        if self.isEmpty():
            raise RuntimeError('Empty list')

        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.isEmpty():
            self.tail = None

        return data

    def removeLast(self) -> T:
        if self.isEmpty():
            raise RuntimeError('Empty list')

        data = self.tail.data
        trav = self.head
        while trav.next != self.tail:
            trav = trav.next

        self.tail = trav
        self.size -= 1

        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None

        return data

    def remove(self, node: Node) -> T:
        if node.next is None:
            return self.removeLast()

        removed_node = node.next
        node.next = node.next.next

        data = removed_node.data

        removed_node.data = None
        removed_node.next = removed_node = None

        self.size -= 1

        return data

    def removeAt(self, index: int) -> T:
        if index < 0 or index >= self.size:
            raise ValueError()

        if index == 0:
            return self.removeFirst()

        if index == self.size - 1:
            return self.removeLast()

        trav = self.head
        for i in range(0, index-1):
            print('from_start', trav)
            trav = trav.next

        return self.remove(trav)

    def indexOf(self, obj: object):
        index = 0
        trav = self.head

        if obj is None:
            while trav:
                if not trav.data:
                    return index
                trav = trav.next
                index += 1
        else:
            while trav:
                if trav.data == obj:
                    return index
                trav = trav.next
                index += 1
        return -1

    def contains(self, obj: object) -> bool:
        return self.indexOf(obj) != -1

    def __str__(self):
        sb = '['
        trav = self.head
        while trav:
            if trav is self.tail:
                sb += str(trav.data)
            else:
                sb += str(trav.data) + ', '
            trav = trav.next
        sb += ']'
        return sb


if __name__ == '__main__':
    my_list = SinglyLinkedList()
    for i in range(5):
        my_list.add(i)
    print(my_list)
    print(my_list.removeAt(4))
    print(my_list)
