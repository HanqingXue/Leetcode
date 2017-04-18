#coding=utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        index = len(nums1) + len(nums2)
        print index
        #print nums1[ ]

if __name__ == '__main__':
    s = Solution()

    s.findMedianSortedArrays([1, 3], [2])
