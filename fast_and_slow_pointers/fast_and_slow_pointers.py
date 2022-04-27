
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()



class FastSlowPointers:

    def linked_list_cycle(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def start_of_linked_list_cycle(self, head):
        cycle_length = 0
        slow, fast = head, head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:  # found the cycle
                cycle_length = self.calculate_cycle_length(slow)
                break
        return self.find_start(head, cycle_length)

    def calculate_cycle_length(self, slow):
        current = slow
        cycle_length = 0
        while True:
            current = current.next
            cycle_length += 1
            if current == slow:
                break
        return cycle_length

    def find_start(self, head, cycle_length):
        pointer1 = head
        pointer2 = head
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1
            break
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1

    def happy_number(self, num):
        slow, fast = num, num
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            if slow == fast:
                break
        return slow == 1

    def find_square_sum(self, num):
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10
        return _sum

    def linked_list_middle(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def palindrome_linked_list(self, head):
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        head_second_half = self.reverse_linked_list(slow)
        copy_head_second_half = head_second_half

        while head is not None and head_second_half is not None:
            if head.value != head_second_half.value:
                break
            head = head.next
            head_second_half = head_second_half.next
        self.reverse_linked_list(copy_head_second_half)

        if head is None or head_second_half is None:  # if both halves match
            return True

        return False

    def reverse_linked_list(self, head):
        prev = None
        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def rearrange_linked_list(self, head):
        if head is None or head.next is None:
            return head

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        head_second_half = self.reverse_linked_list(slow)  # reverse the second half
        head_first_half = head

        # rearrange to produce the LinkedList in the required order
        while head_first_half is not None and head_second_half is not None:
            temp = head_first_half.next
            head_first_half.next = head_second_half
            head_first_half = temp

            temp = head_second_half.next
            head_second_half.next = head_first_half
            head_second_half = temp
        if head_first_half is not None:
            head_first_half.next = None
        return head_first_half

