from tree_depth_first_search.tree_depth_first_search import TreeDepthFirstSearch, TreeNode
import pytest
from collections import deque

@pytest.fixture
def example_tree_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

def test_path_sum(example_tree_1):
    s = 10
    expected = True
    solver = TreeDepthFirstSearch()
    actual = solver.path_sum(example_tree_1, s)
    assert actual == expected

def print_depth_first(root):
    current_node = root
    print(current_node)
    if current_node.left:
        print_depth_first(current_node.left)
    if current_node.right:
        print_depth_first(current_node.right)



def test_print_depth_first(example_tree_1):
    print_depth_first(example_tree_1)


@pytest.fixture
def example_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    return root