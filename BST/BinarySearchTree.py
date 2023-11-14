from simpleQueue import *

class BinarySearchTree:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def add_node(self, value):
        current = parent = self.root

        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            new_node = self._Node(value)
            if parent is None:
                self.root = new_node
            else:
                if value < parent.value:
                    parent.left = new_node
                else:
                    parent.right = new_node
            self.size += 1
        return self.size

    def search_node(self, value):
        if not self.is_empty():
            current = self.root
            while current is not None:
                if current.value == value:
                    break
                else:
                    if current.value > value:
                        current = current.left
                    else:
                        current = current.right
            return current is not None
        else:
            return False

    def inorder_traversal(self):
        result = []
        if not self.is_empty():
            self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        if not self.is_empty():
            self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        if not self.is_empty():
            self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node is not None:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)

    def levelorder_traversal(self):
        if not self.is_empty():
            result = []
            queue = SimpleQueue()
            queue.enqueue(self.root)
            while not queue.is_empty():
                node = queue.dequeue()
                result.append(node.value)
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return result
        else:
            return None

    def get_leaf_count(self):
        if not self.is_empty():
            return self._leaf_count(self.root)
        else:
            return 0

    def _leaf_count(self, node):
        if node:
            if self.is_leaf_node(node):
                return 1
            else:
                return self._leaf_count(node.left) + self._leaf_count(node.right)
        else:
            return 0

    def is_leaf_node(self, node):
        return node.left is None and node.right is None

    def traverse_descending_order(self):
        result = []
        if not self.is_empty():
            self._descending_order(self.root, result)
            return result

    def _descending_order(self, node, result):
        if node:
            self._descending_order(node.right, result)
            result.append(node.value)
            self._descending_order(node.left, result)

    def get_height(self):
        if not self.is_empty():
            return self._get_height(self.root) + 1

    def _get_height(self, node):
        if node.right and node.left:
            return max(self._get_height(node.left), self._get_height(node.right))
        else:
            if node.right:
                return self._get_height(node.right) + 1
            elif node.left:
                return self._get_height(node.left) + 1
            else:
                return 1

    def delete_node(self, key):
        if not self.is_empty():
            self.root = self._node_delete(self.root, key)
            return self.size
        else:
            return None

    def _node_delete(self, node, key):
        if node is None:
            return None
        elif key < node.value:
            node.left = self._node_delete(node.left, key)
        elif key > node.value:
            node.right = self._node_delete(node.right, key)
        else:
            if node.left and node.right:
                temp = self._find_min(node.right)
                node.value = temp.value
                node.right = self._node_delete(node.right, temp.value)
            else:
                if node.right is None:
                    node = node.left
                    self.size -= 1
                else:
                    node = node.right
                    self.size -= 1

        return node

    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)


bst = BinarySearchTree()
assert(bst.get_size() == 8)
assert(bst.search_node(60) == True)
assert(bst.search_node(70) == False)
assert(bst.get_height() == 5)
assert(bst.get_leaf_count() == 2)
assert(bst.add_node(45) == 9)
assert(bst.add_node(50) == 10)
assert(bst.add_node(40) == 11)
assert(bst.add_node(48) == 12)
assert(bst.get_height() == 5)
assert(bst.get_leaf_count() == 4)
assert(bst.inorder_traversal() == [28, 32, 35, 38, 40, 45, 48, 50, 53, 58, 60, 65])
assert(bst.preorder_traversal() == [53, 38, 32, 28, 40, 35, 45, 60, 58, 50, 48, 65])
assert(bst.postorder_traversal() == [28, 35, 40, 32, 48, 50, 58, 65, 60, 53, 45, 38])
assert(bst.levelorder_traversal() == [53, 38, 60, 32, 45, 50, 65, 28, 40, 35, 58, 48])
assert(bst.traverse_descending_order() == [65, 60, 58, 53, 50, 48, 45, 40, 38, 35, 32, 28])
assert(bst.delete_node(40) == 11)
assert(bst.inorder_traversal() == [28, 32, 35, 38, 45, 48, 50, 53, 58, 60, 65])
assert(bst.delete_node(53) == 10)
assert(bst.traverse_descending_order() == [65, 60, 58, 50, 48, 45, 38, 35, 32, 28])
assert(bst.get_height() == 4)
assert(bst.get_leaf_count() == 4)

