class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #O(V + E) TC and O(V + E) SC 
        # map each course to prereq list (adjacency list)
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #visitSet - to track all courses that have been visited along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] == []
            return True

        #call dfs for every single course, 
        #fully looping because to handle even if the nodes are like 2 diff graphs and not fully connected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        