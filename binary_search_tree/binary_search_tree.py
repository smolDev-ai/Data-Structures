import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # plan:
        # if value is less than current_node, move it to the left.
        # If it's greater move it to the right.
        current_node = self
        new_sub_tree = None
        while True:
            if value < current_node.value and current_node.left is not None:
                current_node = current_node.left
            elif value > current_node.value and current_node.right is not None:
                current_node = current_node.right
            elif value < current_node.value and current_node.left is None:
                current_node.left = BinarySearchTree(value)
                new_sub_tree = current_node.left
            elif value > current_node.value and current_node.right is None:
                current_node.right = BinarySearchTree(value)
                new_sub_tree = current_node.right
                # where do I break the loop? Have I met all the cases? What am I missing?

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
