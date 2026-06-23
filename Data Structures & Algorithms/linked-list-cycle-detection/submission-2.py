# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            #slow pointer moves 1 step at a time
            slow = slow.next
            #fast pointer moves 2 steps at a time
            fast = fast.next.next
            #if slow and fast pointers meet, then cycle exists
            if slow == fast:
                return True
        return False
        