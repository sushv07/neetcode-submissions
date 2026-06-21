class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #O(n! * n) TC an O(n * n!) SC
        #resultant permutations - start with a single empty permutation
        perms = [[]]
        for n in nums:
            #intermediate list to store the permutations after inserting n
            new_perms = []
            for p in perms:
                #insert current number at every possible position
                #len(p) + 1 -> becoz a list of length k will have k + 1 positions where we can insert a new number 
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
        