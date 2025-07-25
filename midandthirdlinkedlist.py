class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_mid_and_third(head):
    slow = fast = head
    count = 0
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        count += 1
    return slow.val if slow else None
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
result = find_mid_and_third(n1)
print(result)
