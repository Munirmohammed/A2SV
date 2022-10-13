class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        myHead = ListNode(val=-5000, next=head)
        lsorted = head 
        cur = head.next 
        while cur:
            if cur.val >= lsorted.val:
                lsorted = lsorted.next
            else:
                prev = myHead
                while prev.next.val <= cur.val:
                    prev = prev.next
                    
                lsorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
                
            cur = lsorted.next
            
        return myHead.next
