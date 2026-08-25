class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while prev.next and prev.next.next:
            f=prev.next
            s=f.next

            f.next=s.next
            s.next=f
            prev.next=s
            prev=f
        return dummy.next
      
