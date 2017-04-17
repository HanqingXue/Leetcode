class Solution(object):
    def isInt(self, s):
        s_copy = s
        s_copy = s_copy.lstrip()
        s_copy = s_copy.rstrip()
        if ' ' in s_copy:
            return False
        
        isInt = False
        s = s.rstrip()
        if s == '':
            return isInt 
        else:
            for i in range(0, len(s)):
                if s[i].isdigit():
                    isInt = True
                elif s[i] == ' ':
                    isInt = True
                else:
                    return False
     
        return isInt 
        
    def isFloat(self, s):
        if s == '': return False 
        if s.count('.') != 1: return False
        
        dotIndex = s.index('.')
        if len(s[:dotIndex].rstrip()) != len(s[:dotIndex]):
            return False
        
        
        if dotIndex == 0:
            candiate = s[dotIndex+1:]
            s_lstrip = candiate.lstrip()
            if len(candiate) == len(s_lstrip):
                return self.isInt(s[dotIndex+1:])
            else:
                return False
        else:
            return self.isInt(s[:dotIndex]) or self.isInt(s[dotIndex+1:])
    
    def isSci(self, s):
        if s == '': return False 
        if s.count('e') != 1: return False
        
        dotIndex = s.index('e')

        if dotIndex == 0:
            return False
        else:
            return self.isInt(s[:dotIndex]) and self.isInt(s[dotIndex+1:])    
    
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False
        if '.'in s and 'e' in s:
            return False
        elif self.isInt(s) or self.isFloat(s) or self.isSci(s):
            return True
        else:
            return False
 
if __name__ == '__main__':
     s = Solution()
     print s.isInt(' 0')
     print s.isFloat('0.e')
     print s.isFloat('11.a11')
