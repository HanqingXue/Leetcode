class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        resSet = set()
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i == j: continue
                '''
                diff = 0 - (nums[i] + nums[j])
                print(diff)
                if diff in nums:
                    candidate = (nums[i], nums[j], diff)
                    resSet.add(candidate)
                
                '''
                
                for k in range(j, len(nums)):
                    if j == k:continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        candidate = (nums[i], nums[j], nums[k])
                        resSet.add(candidate)
                        pass
                
                
        resList = []
        print(resList)
        for item in resSet:
            resList.append(list(item))
            
        print(resList)
            
        return resList

s = Solution()
s.threeSum([1,0,-1])