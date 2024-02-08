# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        new_num = ListNode()
        head.next = new_num
        carry = 0
        while l1 or l2:
            if l1 is None:
                while l2 is not None:
                    second = l2.val
                    new_num.next = ListNode((second + carry) % 10)
                    carry = (second + carry) // 10
                    new_num = new_num.next
                    l2 = l2.next
                break
            elif l2 is None:
                while l1 is not None:
                    first = l1.val
                    new_num.next = ListNode((first + carry) % 10)
                    carry = (first + carry) // 10
                    new_num = new_num.next
                    l1 = l1.next
                break
            else:
                first = l1.val
                second = l2.val
                new_num.next = ListNode((first + second + carry) % 10)
                carry = (first + second + carry) // 10
                new_num = new_num.next
            l1 = l1.next
            l2 = l2.next
        if carry != 0:
            new_num.next = ListNode(carry)
        return head.next.next

if __name__ == '__main__':
    s = Solution()
    l11 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    l22 = ListNode(9, ListNode(9, ListNode(9)))
    s.addTwoNumbers(l11, l22)