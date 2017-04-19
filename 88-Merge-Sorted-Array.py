class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0; j = 0; k = 0;
        while i < m and j < n :
            if nums1[i] < nums2[j]:
            
        '''
        class Solution {
public:
    void merge(int nums1[], int m, int nums2[], int n) {
        int ia = m - 1, ib = n - 1, icur = m + n - 1;
        while(ia >= 0 && ib >= 0)
            nums1[icur--] = nums1[ia] > nums2[ib] ? nums1[ia--] : nums2[ib--];
        while(ib >=0)
            num1[icur--] = num1[ib--];
    }
};
        '''
if __name__ == '__main__':
    s = Solution()
    print (s.merge([0], 0, [1], 1))
    pass
