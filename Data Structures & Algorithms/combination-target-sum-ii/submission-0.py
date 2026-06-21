class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(n * 2^n) TC and O(n) SC
        res = []
        # sorting the candidates so that we effectively skip duplicates.
        candidates.sort()

        # recursive backtracking function - dfs
        # i - pointer pointing to the element, cur - cur list of candidates, total - total so far for the chpsen candidates
        def dfs(i, cur, total):
            #base cases:
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            #since we need to skip it at the next step
            cur.pop()

            #skip candidates[i]
            while i + 1 < len(candidates) and  candidates[i] == candidates[i+1]:
                #to skip the duplicate
                i += 1
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        return res



        