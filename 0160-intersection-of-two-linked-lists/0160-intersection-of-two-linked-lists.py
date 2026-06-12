# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        def getLengthAndTail(head):
            if not head:
                return 0, None

            length = 1
            curr = head

            while curr.next:
                curr = curr.next
                length += 1

            return length, curr

        lenA, tailA = getLengthAndTail(headA)
        lenB, tailB = getLengthAndTail(headB)

        if tailA is not tailB:
            return None

        ptrA = headA
        ptrB = headB

        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                ptrA = ptrA.next
        else:
            for _ in range(diff):
                ptrB = ptrB.next

        while ptrA is not ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next

        return ptrA