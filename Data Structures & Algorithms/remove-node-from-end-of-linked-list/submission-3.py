# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Optimal O(n) TC and O(1) SC
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #shift right n times
        #reason => to land on the node exactly before the node that we are going to delete
        #for left pointer to land in that place
        while n > 0 and right:
            right = right.next
            n -= 1
        
        #shift both left and right pointers
        while right:
            left = left.next
            right = right.next
        
        #delete nth node
        left.next = left.next.next
        return dummy.next
