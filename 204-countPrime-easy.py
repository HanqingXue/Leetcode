from math import sqrt
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        if n == 0 or n == 1 or n == 2:
            return 0
        

        
        for i in range(2, n):
            if i % 2 == 0:
                continue
            
            if self.isPrimes(i):
                ans += 1

        return ans + 1
        
    def isPrimes(self, n):
        if n == 1:
            return False
        
        if n % 2 == 0:
            return False
        
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True
'''
if __name__ == '__main__':
    s = Solution()
    print (s.countPrimes(100))
'''