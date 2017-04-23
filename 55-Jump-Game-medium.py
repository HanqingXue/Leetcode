class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1 or len(nums) == 0:
            return True
        
        if nums[0] == 0:
            return False
        
        MAX = nums[0]
        for i in range(1, len(nums)):
            if MAX == 0: return False
            MAX -= 1
            
            if nums[i] == 0:
                return False
            
            if MAX <= nums[i]:
                MAX = nums[i]

            if i + MAX >= len(nums) - 1:
                return True
        
        return False

