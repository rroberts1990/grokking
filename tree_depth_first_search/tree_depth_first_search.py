from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def print_tree(self):
        return f"[{self.value}->[{self.left}, {self.right}]"

    def __eq__(self, other):
        return self.value == other.value


class TreeBreadthFirstSearch:

    def level_order_traversal(self, root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_level)
        return result

    def reverse_level_order_traversal(self, root):
        result = deque()
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.appendleft(current_level)
        return list(result)

    def zig_zag_traversal(self, root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        left_to_right = True
        while queue:
            level_size = len(queue)
            current_level = deque()
            for _ in range(level_size):
                current_node = queue.popleft()
                if left_to_right:
                    current_level.append(current_node.value)
                else:
                    current_level.appendleft(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(list(current_level))
            left_to_right = not left_to_right
        return result

    def level_averages(self, root):
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                current_node = queue.popleft()
                level_sum += current_node.value
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            average = level_sum/level_size
            result.append(average)
        return result

    def minimum_depth(self, root):

        queue = deque()
        queue.append(root)
        min_depth = 0
        while queue:
            level_size = len(queue)
            min_depth += 1
            for _ in range(level_size):
                current_node = queue.popleft()
                if not current_node.left and not current_node.right:
                    return min_depth

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

    def level_order_successor(self, root, key):
        queue = deque()
        queue.append(root)

        while queue:
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            if current_node.value == key:
                break
        return queue[0]


    def connect_level_order_siblings(self, root):
        pass
