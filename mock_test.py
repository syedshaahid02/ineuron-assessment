# -*- coding: utf-8 -*-
"""Mock_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IMMGBmHaa_8PlLBsE17Y5mdJ0QDEunYZ
"""

#1
def mySqrt(x):
    if x == 0:
        return 0

    low, high = 1, x

    while low <= high:
        mid = (low + high) // 2
        if mid * mid > x:
            high = mid - 1
        else:
            low = mid + 1

    return low - 1

print(mySqrt(4))
print(mySqrt(8))

#2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        total = x + y + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry > 0:
        curr.next = ListNode(carry)

    return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 7 0 8