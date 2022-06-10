class Node:
    def __init__(self, left=None, right=None, elem=None):
        self.data = elem
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.nodeCount = 0
        self.root = None
    def isEmpty(self):
        return self.size() == 0
    def size(self):
        return self.nodeCount
    def add_elem(self, elem):
        if self.contains_elem(elem):
            return False
        else:
            self.root = self.add_node(self.root, elem)
            self.nodeCount += 1
            return True
    def add_node(self, node, elem):
        if node is None:
            node = Node(None, None, elem)
        else:
            if elem < node.data:
                node.left = self.add_node(node.left, elem)
            else:
                node.right = self.add_node(node.right, elem)
        return node
    def remove_elem(self, elem):
        if self.contains_elem(elem):
            self.root = self.remove_node(self.root, elem)
            self.nodeCount -= 1
            return True
        else:
            return False
    def remove_node(self, node, elem):
        if node is None:
            return None
        if elem < node.data:
            node.left = self.remove_node(node.left, elem)
        elif elem > node.data:
            node.right = self.remove_node(node.rigth, elem)
        else:
            if node.left is None:
                rightChild = node.right
                node.data = None
                node = None
                return rightChild
            elif node.right is None:
                leftChild = node.left
                node.data = None
                node = None
            else:
                tmp = self.digLeft(node.right)
                node.data = tmp.data
                node.right = remove_node(node.right, tmp.data)
        return node
    def digLeft(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur
    def digRight(self, node):
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur
    def contains_elem(self, elem):
        return self.contains_node(self.root, elem)
    def contains_node(self, node, elem):
        if node is None:
            return False
        if elem < node.data:
            return self.contains_node(node.left, elem)
        elif elem > node.data:
            return self.contains_node(node.right, elem)
        else:
            return True
    def height(self):
        return self.height_node(self.root)
    def height_node(self, node):
        if node is None:
            return 0
        return max(self.height_node(node.left), self.height_node(node.right)) + 1
    def print(self, traversal_type):
        if traversal_type == 'pre':
            return self.preOrderTraversal(self.root)
        elif traversal_type == 'in':
            return self.inOrderTraversal(self.root)
        elif traversal_type == 'post':
            return self.postOrderTraversal(self.root)
        elif traversal_type == 'level':
            return self.levelOrderTraversal(self.root)
        else:
            return None

    def preOrderTraversal(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
    def inOrderTraversal(self, node):
        if node is not None:
            self.inOrderTraversal(node.left)
            print(node.data)
            self.inOrderTraversal(node.right)
    def postOrderTraversal(self, node):
        if node is not None:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.data)
    def levelOrderTraversal(self, node):
        if node is not None:
            queue = []
            queue.append(node)
            while queue:
                node = queue.pop()
                if node is None:
                    continue
                print(node.data)
                queue.append(node.left)
                queue.append(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in range(1, 6):
        bst.add_elem(i)

    bst.print('pre')
    print('---')
    bst.print('in')
    print('---')
    bst.print('post')
    print('---')
    bst.print('level')
