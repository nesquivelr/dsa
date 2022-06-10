class AVLTreeRecursive:
    class Node:
        def __init__(self, value=None):
            self.bf = 0
            self.value = value
            self.height = 0
            self.left = None
            self.right = None

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def getText(self):
            return str(value)

    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def height(self):
        if self.root is None:
            return 0
        else:
            return self.root.height

    def size(self):
        return self.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def contains(self, value):
        return self.contains_value(self.root, value)

    def contains_value(self, node, value):
        if node is None:
            return False
        if value < node.value:
            return self.contains_value(node.left, value)
        if value > node.value:
            return self.contains_value(node.right, value)
        return True

    def insert(self, value):
        if value is None:
            return False
        if not self.contains_value(self.root, value):
            self.root = self.insert_value(self.root, value)
            self.nodeCount += 1
            return True
        return False

    def insert_value(self, node, value):
        if node is None:
            return self.Node(value)
        if value < node.value:
            node.left = self.insert_value(node.left, value)
        if value > node.value:
            node.right = self.insert_value(node.right, value)
        self.update(node)
        return self.balance(node)

    def update(self, node):
        leftNodeHeight = -1 if node.left is None else node.left.height
        rightNodeHeight = -1 if node.right is None else node.right.height
        node.height = 1 + max(leftNodeHeight, rightNodeHeight)
        node.bf = rightNodeHeight - leftNodeHeight

    def balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self.leftLeftCase(node)
            else:
                return self.leftRightCase(node)
        elif node.bf == +2:
            if node.left.bf >= 0:
                return self.rightRightCase(node)
            else:
                return self.rightLeftCase(node)
        return node

    def leftLeftCase(self, node):
        return self.rightRotation(node)

    def leftRightCase(self, node):
        node.left = self.leftRotation(node.left)
        return self.leftLeftCase(node)

    def rightRightCase(self, node):
        return self.leftRotation(node)

    def rightLeftCase(self, node):
        node.right = self.rightRotation(node.right)
        return self.rightRightCase(node)

    def leftRotation(self, node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        self.update(node)
        self.update(newParent)
        return newParent

    def rightRotation(self, node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        self.update(node)
        self.update(newParent)
        return newParent

    def remove(self, elem):
        if elem is None:
            return False

        if self.contains_value(self.root, elem):
            self.root = self.remove_value(self.root, elem)
            self.nodeCount -= 1
            return True

        return False

    def remove_value(self, node, elem):
        if node is None:
            return None
        if elem < node.value:
            node.left = self.remove_value(node.left, elem)
        elif elem > node.value:
            node.right = self.remove_value(node.right, elem)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.height > node.right.height:
                    successorValue = self.findMax(node.left)
                    node.value = successorValue
                    node.left = self.remove_value(node.left, successorValue)
                else:
                    successorValue = self.findMin(node.right)
                    node.value = successorValue
                    node.right = self.remove_value(node.right, successorValue)
        self.update(node)
        return self.balance(node)

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def findMax(self, node):
        while node.right is not None:
            node = node.right
        return node.value

    def levelOrderTraversal(self):
        return levelOrderTraversal_node(self.root)

    def levelOrderTraversal(self):
        if self.root is not None:
            queue = []
            queue.append(self.root)
            while queue:
                node = queue.pop()
                if node is None:
                    continue
                print(node.value, node.height)
                queue.append(node.left)
                queue.append(node.right)



if __name__ == '__main__':
    avl = AVLTreeRecursive()
    avl.insert(5)
    avl.insert(1)
    avl.insert(9)
    avl.insert(16)
    avl.insert(8)
    avl.insert(10)
    avl.remove(9)
    print('-'*5)
    print('height:', avl.height())
    print('size:', avl.size())
    print('isEmpty:', avl.isEmpty())
    avl.levelOrderTraversal()
