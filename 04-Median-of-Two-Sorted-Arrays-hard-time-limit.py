class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            mid = len(nums2) / 2
            if len(nums2) % 2 == 1:
                return nums2[mid]
            else:
                return float(nums2[mid] + nums2[mid - 1]) / 2
        
        elif len(nums2) == 0:
            mid = len(nums1) / 2
            if len(nums1) % 2 == 1:
                return nums1[mid]
            else:
                return float(nums1[mid] + nums1[mid - 1]) / 2
            return nums1[0]
        
        else:
            pass
        
        m = len(nums1)
        n = len(nums2)
        nums1 = nums1 + [0] * n
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        
        while n > 0:
            nums1[:n] = nums2[:n]
        
        mid = len(nums1) / 2
        if len(nums1) % 2 == 0:
            return float(nums1[mid] + nums1[mid - 1]) / 2
        else:
            return nums1[mid]
