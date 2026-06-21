# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Optimal solution O(n + m) TC
        #O(1) SC - because we are only reusing the existing nodes of list1 and list2
        
        #contains the merged list
        dummy = ListNode()
        #tail pointer which keeps moving in the merged list
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                #points tail pointer to the current pointer of list1
                node.next = list1
                list1 = list1.next
            else:
                #points tail pointer to current pointer of list2
                node.next = list2
                list2 = list2.next
            #update the tail pointer, to avoid overlaps while merging
            node = node.next

        #edge case check - if either of lists are empty
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        
        #to skip dummy and return real head
        return dummy.next