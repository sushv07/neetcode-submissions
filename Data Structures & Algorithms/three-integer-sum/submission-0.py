class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #resultant array to store the list of unique triplets
        res = []
        #sort the input list
        nums.sort()
        
        #iterate through the input list, keeping 1st number of each triplet fixed
        for index,firstValue in enumerate(nums):

            #skip duplicates from 2nd round onwards - to avoid same triplets
            if index > 0 and firstValue == nums[index - 1]:
                continue
            
            #2-sum approach to find the other 2 members of the triplet
            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = firstValue + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([firstValue, nums[l], nums[r]])
                    l += 1
                    #skip duplicates again if 2nd member is same as prev triplet combination
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res