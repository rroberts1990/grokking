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

    def __repr__(self):
        return f"Node({self.value})->{self.next}"

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

    def reverse_sub_list(self, head, p, q):
        if p == q:
            return head
        current = head
        previous = None
        i = 0
        while current is not None and i < p - 1:
            previous = current
            current = current.next
            i += 1

        node_before_p = previous
        last_node_of_sublist = current

        i = 0
        while current is not None and i < q - p + 1:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            i += 1

        if node_before_p is not None:
            node_before_p.next = previous
        else:
            head = previous

        last_node_of_sublist.next = current
        return head

    def reverse_every_k_sublist(self, head, k):
        if k <= 1 or head is None:
            return head

        current = head
        previous = None

        while True:
            last_node_of_prev_part = previous
            last_node_of_sublist = current
            i = 0
            while current is not None and i < k:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
                i += 1

            if last_node_of_prev_part is not None:
                last_node_of_prev_part.next = previous
            else:
                head = previous

                # connect with the next part
            last_node_of_sublist.next = current

            if current is None:
                break
            previous = last_node_of_sublist
        return head


