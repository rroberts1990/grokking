from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def print_tree(self):
        return f"[{self.value}->[{self.left}, {self.right}]"

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return f'Node({self.value})'

    def is_leaf(self):
        return self.left is None and self.right is None


class TreeDepthFirstSearch:

    def path_sum(self, root, s):
        if root is None:
            return False
        print(root)
        if root.is_leaf() and root.value == s:
            return True
        return self.path_sum(root.left, s - root.value) or \
            self.path_sum(root.right, s - root.value)


    def find_paths(self, root, path_sum):
        all_paths = []
        self.find_paths_recursive(root, path_sum, [], all_paths)
        return all_paths

    def find_paths_recursive(self, current_node, current_sum, current_path, all_paths):
        if current_node is None:
            return

        current_path.append(current_node.val)

        if current_node.is_leaf() and current_node.val == current_sum:
            all_paths.append(current_path)

        else:
            self.find_paths_recursive(current_node.left, current_sum - current_node.value, current_path, all_paths)
            self.find_paths_recursive(current_node.right, current_sum - current_node.value, current_path, all_paths)

        del current_path[-1]

    def sum_of_path_numbers(self, root):
        current_node = root
        if current_node is None:
            return 0
        





