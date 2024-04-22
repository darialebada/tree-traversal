import unittest
from tree import Tree

class TestFindMethod(unittest.TestCase):

    def test_find_existing_node(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        
        node = tree.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)

    def test_find_non_existing_node(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)

        node = tree.find(5)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()