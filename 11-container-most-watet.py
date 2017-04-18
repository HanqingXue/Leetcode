class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0; r= len(height)
        maxArea = 0;
        
        while l < r:
            curArea = min(height[l], height[r])*(r-l)
            maxArea = max(maxArea, curArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxArea