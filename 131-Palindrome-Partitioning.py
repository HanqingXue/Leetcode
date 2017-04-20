import time

class Solution(object):
    def minCut(self, s):
        cuts = self.partition(s)
        cuts_count = []
        for cut in cuts:
            #print(cut)
            c=len([x for x in cut])
            cuts_count.append(c)
        
        return min(cuts_count) - 1
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        result = []
        for i in range(0, len(s)):
            if self.isPalindrome(s[:i+1]):
                for r in self.partition(s[i+1:]):
                    result.append([s[:i+1]]+r)
        
        return result
    
    def isPalindrome(self, s):
        l = 0; r = len(s) -1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
                
        return True
'''
if __name__ == "__main__":
    #print( Solution().partition(""kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu""))
    s = Solution()
    #print(s.partition('bbba'))
    #print(s.minCut('bbba'))
    start = time.time()
    print(s.minCut('"ababababababababababababcbabababababababababababa"'))
    end = time.time()
    print(end - start)
    #print(s.partition('abcdshsd'))
'''