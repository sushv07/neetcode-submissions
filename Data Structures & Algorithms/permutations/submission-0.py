class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #O(n! * n) TC an O(n) SC
        #resultant permutations
        perms = [[]]
        for n in nums:
            #intermediate list to store the permutations
            new_perms = []
            for p in perms:
                #insert each number at every possible position
                #len(p) + 1 -> becoz every k numebrs will have k + 1 positions where we can insert a new number 
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
        