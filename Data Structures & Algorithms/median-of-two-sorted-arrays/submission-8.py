class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Optimal Binary Search Approach - O(log(m + n))
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            # partition-cut for Array A
            i = (l + r) // 2
            # partition-cut for Array B
            j = half - i - 2

            ALeft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i + 1] if i + 1 < len(A) else float("infinity")
            BLeft = B[j] if j >= 0 else float("-infinity")
            BRight = B[j + 1] if j + 1 < len(B) else float("infinity")

            #check if partition cuts are correct    
            if ALeft <= BRight and BLeft <= ARight:
                #if correct, compute median
                if total % 2:
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            #or if left partition has too many elements: shrink left
            elif ALeft > BRight:
                r = i - 1
            #or if left partition has too little elements, expand left
            elif BLeft > ARight:
                l = i + 1



            