class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest = ''
        if len(s) < 2:
            return s
        
        for i in range(0, n):
            expendString = self.expend(s, i, i)
            if len(expendString) > len(longest):
                longest = expendString
            
            expendString = self.expend(s, i, i + 1)
            if len(expendString) > len(longest):
                longest = expendString
        
        return longest
    
    def expend(self, s, l, r):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l + 1:r]