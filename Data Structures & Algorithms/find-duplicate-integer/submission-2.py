class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #O(n) TC and O(1) SC
        #fast and slow pointers
        #Floyd's Hare and Tortoise cycle detection
        slow, fast = 0, 0

        #detect meting point inside cycle
        #detect if cycle exists
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #find the starting point of cycle (i.e the duplicate)
        #he duplicate value is the first node (or value) 
        #reached from index 0 where two different paths merge.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            



        