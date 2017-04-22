class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        
        if len(haystack) < len(needle):
            return -1
        
        elif haystack == '' or needle == '':
            return 0
        
        else:
            for i in range(0, len(haystack) - len(needle) + 1):
        
                if haystack[i] == needle[0]:
                    haystack_copy = haystack[i:i+len(needle)]
                    
                    if self.equl(haystack_copy, needle):
                        return i
                    else:
                        continue
         
            return -2
    
    def equl(self, s1, s2):
        while len(s1) != len(s2):
            return False
        
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                return False
            i += 1
        
        return True