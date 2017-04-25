class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        value = 0
        for i in range(0, len(digits)):
            value = value*10 + digits[i]
        
        value += 1
        value = list(str(value))
        ans = [int(x) for x in value]
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2]))