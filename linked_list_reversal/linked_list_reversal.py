class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        rep = ""
        temp = self
        while temp is not None:
            rep += f"{temp.value}->"
            temp = temp.next
        rep += "null"
        return rep

class ReverseLinkedList:

    def reverse_linked_list(self, head):
        current = head
        previous = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
