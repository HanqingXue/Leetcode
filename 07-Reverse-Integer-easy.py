class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        op = 1
        max_int = 2147483648
        if x < 0:
            op = -1
            x=str(x)[1:]
        
        print type(x)
        #x_copy = ''
        #x = x[::-1]
        x = str(x)
        x = list(x)
        i = len(x)-1
        s = 0
        while i >= 0:
            s = 10*s + int(x[i])
            i -= 1

        if s >= max_int:
            return 0
        else :
            return op * s

if __name__ == '__main__':
    s = Solution()
    print (s.reverse(-8463847412))

