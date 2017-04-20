class Solution(object):
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0 and 1162261467 % n == 0:
            return True
        else:
            return False
    
    def isPowerofThree(self, n):
        if n < 3:
            return False
        elif n==3 :
            return True
        else:
            return self.isPowerofThree(n/3)
if __name__ == '__main__':
    s = Solution()
    print(s.isPowerofThree(15))