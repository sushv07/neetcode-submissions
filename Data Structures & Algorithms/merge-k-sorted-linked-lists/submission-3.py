# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(nlogk) TC and O(1) SC
# We merge the lists in pairs. Each round reduces the number of lists by about half, 
# so there are log k rounds. 
# During each round, every node is processed exactly once across all merges, 
# which costs O(N). Therefore, the total complexity is O(N log k).
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #edge cases check:
        if not lists or len(lists) == 0:
            return None

        #merge lists in pairs of 2 until we have a single merged list
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
            
    #helper function to merge 2 sorted lists
    def mergeList(self, list1, list2):
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
        

