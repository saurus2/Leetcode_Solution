class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        nLen = len(nums1)
        if nLen == 1:
            return nums1[0]
        elif nLen > 1:
            if nLen % 2 != 0:
                return nums1[nLen//2]
            else:
                mIdx = nLen // 2
                return (nums1[mIdx - 1] + nums1[mIdx]) / 2
        return 0
