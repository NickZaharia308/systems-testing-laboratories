from node import Node
import unittest

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        # TODO
        if node is not None:
            print(str(node.data) + ' ')
            self._printInorderTree(node.left)
            self._printInorderTree(node.right)

    def _printPostorderTree(self, node):
        # TODO
        if node is not None:
            self._printInorderTree(node.left)
            self._printInorderTree(node.right)
            print(str(node.data) + ' ')


class TestTreeFind(unittest.TestCase):

    def setUp(self):
        """Set up a tree for testing."""
        # Tree structure:
        #       5
        #      / \
        #     3   7
        #    / \ / \
        #   2  4 6  8
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(2)
        self.tree.add(4)
        self.tree.add(6)
        self.tree.add(8)

    def test_find_existing_node_root(self):
        """Test finding the root node."""
        found_node = self.tree.find(5)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 5)

    def test_find_existing_node_leaf(self):
        """Test finding a leaf node."""
        found_node = self.tree.find(8)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 8)

    def test_find_existing_node_internal(self):
        """Test finding an internal node (not root)."""
        found_node = self.tree.find(3)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 3)

    def test_find_non_existing_node(self):
        """Test finding a node that does not exist."""
        found_node = self.tree.find(10)
        self.assertIsNone(found_node)

    def test_find_in_empty_tree(self):
        """Test finding in an empty tree."""
        empty_tree = Tree()
        found_node = empty_tree.find(1)
        self.assertIsNone(found_node)

