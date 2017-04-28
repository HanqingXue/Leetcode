class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        
        s_alpha = set(list(s))
        t_alpha = set(list(t))
        if s_alpha != t_alpha:
            return False
        
        s_dict = {}
        t_dict = {}
        for item in s_alpha:
            s_dict[item] = 0
            
        for item in t_alpha:
            t_dict[item] = 0
            
        for item in s:
            s_dict[item] += 1
            
        for item in t:
            t_dict[item] += 1
            
        if s_dict == t_dict:
            return True
            
        else:
            return False
