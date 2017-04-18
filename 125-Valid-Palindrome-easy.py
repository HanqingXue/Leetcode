class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        
        
        if s == '':
            return True
        
        s_list = []
        for i in range(0, len(s)):
            if s[i].isdigit() or s[i].isalpha():
                s_list.append(s[i])

        s = s_list
        if len(s)%2 == 1:
            mid  = len(s)/2
            s.pop(int(mid))
        
        l = 0; r= len(s)-1
        while l < r:
            if s[l] == s[r]:
                pass
            else:
                return False
            l += 1
            r -= 1
        return True