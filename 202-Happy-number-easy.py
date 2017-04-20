class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in [2, 3, 4, 5, 6, 8, 9]:
            return False
        elif n in [1, 7]:
            return True
        else:
            s = 0
            
            n = str(n)
            n = list(n)
            n_list = [int(x) for x in n]
            square = lambda x: x * x
            square_list = [square(x) for x in n_list]
            s = sum(square_list)
            if s == 1:
                return True
            j = 0
            while s != 1 and j < 100:
                s = str(s)
                s = list(s)
                s_list = [int(x) for x in s]
                square_list = [square(x) for x in s_list]
                s = sum(square_list)
                j += 1
            
            return j != 100