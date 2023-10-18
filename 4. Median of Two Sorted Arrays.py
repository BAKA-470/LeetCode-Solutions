class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        nums3 = [None] * (n1 + n2)
        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums3[k] = nums2[j]
                j += 1
                k += 1

        if i < n1:
            while i < n1:
                nums3[k] = nums1[i]
                i += 1
                k += 1
        if j < n2:
            while j < n2:
                nums3[k] = nums2[j]
                j += 1
                k += 1
        n3 = n1 + n2
        if n3 % 2 == 0:
            median = (nums3[n3 // 2] + nums3[(n3 // 2) - 1]) / 2
        else:
            median = nums3[n3 // 2]
        return median
