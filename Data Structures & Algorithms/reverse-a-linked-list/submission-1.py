# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive Solution - O(n) TC and O(n) SC
        if not head:
            return None
        
        newhead = head
        #Reverse the rest of list other than the orig head.
        if head.next:
            #get the new head
            newhead = self.reverseList(head.next)
            #make the next node point back to the tmp. head
            head.next.next = head
        #the tmp head now becomes the tail of the list
        head.next = None
    
        return newhead