class Solution:
    def addTwoNumbers(self,l1,l2):
        d=c=ListNode(0); carry=0
        while l1 or l2 or carry:
            s=(l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            carry,c.next=s//10,ListNode(s%10); c=c.next
            l1=l1.next if l1 else None; l2=l2.next if l2 else None
        return d.next
        