# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(n) TC and O(1) SC
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node - node before the current group
        dummy = ListNode(0, head)
        groupPrev = dummy

        #get kth node - if k nodes not present in the group, break
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            #start node of next group
            groupNext = kth.next

            #reverse current group
            #1 -> 2 - > 3
            #prev = 4 / curr = 1
            prev, curr = kth.next, groupPrev.next
            #groupNext = 4
            while curr != groupNext:
                #tmp stores the node that was the head before reversal, 
                #which becomes the tail after reversal.
                tmp = curr.next # 2
                curr.next = prev # 1.next = 4
                prev = curr #prev 1
                curr = tmp #curr 2

            #reconnect reversed list back into main list
            tmp = groupPrev.next 
            groupPrev.next = kth #connect dummy to 3
            groupPrev = tmp

        return dummy.next      

    # helper function to get kth node
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr