# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre=head
        i=head
        length=0
        while i:
            length+=1
            i=i.next
        #     len2待删除的第几个元素位置
        len2=length-n+1
        i=head
        j=1
        if length==1:
            return []
        if n==length:
            head=head.next
            return head
        while j<len2-1:
            i=i.next
            j+=1
        k=i.next.next
        i.next=k
        return head

l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l1.next=l2
l2.next=l3
s=Solution()
print(s.removeNthFromEnd(l1,2))



