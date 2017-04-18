
class Solution(object):
    
    self.A = [0]*100
        
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
        print(A)
        if n <= 2 :
            A[n] = n
            
        if A[n] >0:
            return A[n]
        else:
            return  A[n-1] + A[n-2]


if __name__ == '__main__':
    s = Solution()
    for i in range(0, 100):
        print(s.dpClimb(i))

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        
        