class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if nums == [] or len(nums)<3:
            return []
        
        if nums.count(0) == len(nums):
            return [[0, 0, 0]]
        
        resSet = set()
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i == j: continue
                diff = 0 - (nums[i] + nums[j])
                if (diff in nums) and (diff != nums[i]) and (diff != nums[j]):
                    candidate = [nums[i], nums[j], diff]
                    candidate.sort()
                    resSet.add(tuple(candidate))
                
        resList = []
        for item in resSet:
            resList.append(list(item))
            
        if nums.count(0) >= 3: resList.append([0, 0, 0])

        return resList
s = Solution()
A = s.threeSum([0,1])
print(A)
