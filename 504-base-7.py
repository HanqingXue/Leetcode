class Solution(object):
    def convertToBase7(self, num, abase=7):
        """
        :type num: int
        :rtype: str
        """
        base = abase
        ans = []
        sevenBin = ""
        hexMapper = {}
        for i in range(0, 10):
            hexMapper[str(i)] = str(i)

        hexMapper['10'] = "A"
        hexMapper['11'] = "B"
        hexMapper['12'] = "C"
        hexMapper['13'] = "D"
        hexMapper['14'] = "E"
        hexMapper['14'] = "F"

        if abs(num) < base:
            return str(num)

        oper = '-' if num < 0 else ''
        num = abs(num)
        while num!= 0:
            remainer = num % base
            ans.append(hexMapper[str(remainer)])
            num /= base

        for i in range(1, len(ans) + 1):
            sevenBin += ans[-i]

        return oper + sevenBin

if __name__ == "__main__":
    s = Solution()
    print s.convertToBase7(196, 16)