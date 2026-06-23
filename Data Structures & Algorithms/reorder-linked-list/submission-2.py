# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #O(n) TC and O(1) SC
        #find the middle element
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        second = slow.next #tmp var
        prev = slow.next = None
        #Save next node
        #Attach current node to front of reversed list
        #Update reversed list head
        #Move to next node
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first, second = head, prev
        while second:
            # save next nodes
            # Because we’re about to change pointers and 
            # don’t want to lose where the rest of the lists are.
            tmp1, tmp2 = first.next, second.next
            # connect first node in 1st half with first node in second half
            first.next = second
            # reconnect second half's first node with the next element in first half
            second.next = tmp1
            # move the pointers forward in both the halves
            first, second = tmp1, tmp2
        