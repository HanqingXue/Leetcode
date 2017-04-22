class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            i += 1
            
        return i
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([0,1,2,3]))