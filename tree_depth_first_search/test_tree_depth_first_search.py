from tree_depth_first_search.tree_depth_first_search import TreeDepthFirstSearch, TreeNode
import pytest
from collections import deque
from typing import List

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


def test_build():
    arr = [0, 1, 2, 3, 4, 5, 6]
    A = [x for x in arr]
    def build_subtree(A, i ,j):
        c = (i + j)//2
        root = TreeNode(A[c])
        # print(root)
        if i < c:
            root.left = build_subtree(A, i, c-1)
        if j > c:
            root.right = build_subtree(A, c+1, j)
        return root
    root = build_subtree(A, 0, len(A)-1)
    print(root)
    return root


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(i, left):
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)

            if i not in cache:
                cache[i] = max(mult * nums[left] + dp(i + 1, left + 1),
                               mult * nums[right] + dp(i + 1, left))
            return cache[i]

        cache = {}
        n, m = len(nums), len(multipliers)
        return dp(0, 0)

def test_max_score():
    solver = Solution()
    actual = solver.maximumScore([1, 2, 3], [3, 2, 1])
    print(actual)

def check_height(root):
    if root == None:
        return -1

def is_balanced(root):
    return check_height(root) != (-10**32)


def test_reverse_string():
    string = list("hello world")
    start = 0
    end = len(string)-1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    print("".join(string))