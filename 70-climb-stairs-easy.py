
class Solution(object):
    def __init__(self):
        super(Solution, self).__init__()
        self.A = [0]*1000
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1 = 1;
        step2 = 2;
        temp = 0;
        
        if n == 1 or n == 2:
            return n
        else:
            i = 3
            while i < n + 1:
                temp = step1 + step2
                step1 = step2
                step2 = temp
                i += 1
            return temp
    
    def iterClimb(self, n):
        if n <= 2:
            return n
        else:
            return self.iterClimb(n-1) + self.iterClimb(n-2)
        
    def dpClimb(self, n ):
        if n <= 2 :
            self.A[n] = n
            
        if self.A[n] > 0:
            return self.A[n]
        else:
            self.A[n] = self.dpClimb(n-1) + self.dpClimb(n-2)
        
        return self.A[n]


if __name__ == '__main__':
    s = Solution()
    for i in range(0, 100):
        pass