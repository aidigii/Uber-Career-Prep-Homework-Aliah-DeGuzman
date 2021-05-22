
"""
EX 1
Implement a method called print() to print the values of the data in all the TreeNodes in a Tree above.
"""

class Tree:

    # initialize tree
    def __init__(self, root):
        self.root = root

    #pre-order printing
    def print(self, root):

        # stops here so we don't access null nodes
        if root is None:
            return

        # print data
        print(root.data)

        # recursively goes on left first and then right
        self.print(root.left)
        self.print(root.right)

    # used for printing later
    def getRoot(self):
        return self.root


# class of nodes to be used for trees
class TreeNode:

    # constructor
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# create tree, main method
leftChild = TreeNode(6, None, None)
rightChild = TreeNode(3, None, None)
left = TreeNode(7, None, None)
right = TreeNode(17, leftChild, rightChild)
root = TreeNode(1, left, right)
tree = Tree(root)

tree.print(tree.getRoot())
