import time
class Solution(object):
    def countPrimes1(self, n):
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
        
    def isPrimes1(self, n):
        if n == 1:
            return False
        
        if n % 2 == 0:
            return False
        
        for i in range(2, int(n**0.5) +1):
            if n % i == 0:
                return False
        return True
    
    def countPrimes(self, n):
        s = [True] * n
        s[0] = s[1] = False
        sqrtn = int(round(n ** 0.5))
        count = 0
        for i in range(2, sqrtn + 1):  # xrange for Py2
            if s[i]:
                count += 1
                s[i*i : n: i] = [False] * len(range(i * i, n, i))  # xrange for Py2
        print(count)
        return s.count(True)
    
if __name__ == '__main__':
    s = Solution()
    s.countPrimes(99983)