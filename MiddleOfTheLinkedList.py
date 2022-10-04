# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = node = head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        md = count // 2
        c = 0
        while node:
            if c == md:
                return node
            else:
                c += 1
                node = node.next
        return None
            
