# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #O(n) TC and O(1) SC 

        #to track the head of the already reversed portion
        prev = None
        #to track the head of the remaining unreversed portion
        curr = head

        while curr:
            #original next node
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev