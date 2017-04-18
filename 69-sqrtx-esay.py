class Solution(object):
    def mySqrtForce(self, x):
        """
        Time limited! So bad!
        :type x: int
        :rtype: int
        """
        sqrtdict = {}
        for i in range(0, 1000000000):
            sqrtdict[i] = i*i
            
        for i in range(0, 100000000-1):
            if sqrtdict[i] < x < sqrtdict[i+1]:
                return i
            elif sqrtdict[i] == x:
                return i
    
    def mySqrt(self, x):
        if x == 0 :return 0
        r = x
        while r*r > x:
            r = (r + x/r)/2
        return int(r)
    

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(121))
