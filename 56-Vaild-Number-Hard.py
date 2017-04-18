class Solution(object):
    def isInt(self, s):
        INVALID = 0;
        SPACE = 1;
        DIGIT = 2;
        OP = 3;
        transitionTable = [[-1, 0, 1, 1], [-1, 2, 1, -1], [-1, 2, -1, -1]]
        state = 0;
        i = 0;
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i].isdigit():
                inputtype = DIGIT
            elif s[i] in '+-':
                inputtype = OP
            
            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 2 or state == 1
    
    def isFloat(self, s):
        INVALID = 0;
        DOT = 1;
        SPACE = 2;
        DIGIT = 3;
        OP = 4
        E=5
        transitionTable = [[-1, 1, 0 , 2, 2, -1],
                           [-1, -1, 4, 1, -1, -1],
                           [-1, 3, -1, 2, -1, -1],
                           [-1, -1, 3, 1, -1, 5],
                           [-1, -1, 4, -1, -1, -1],
                           [-1, -1, -1, 1, -1, 1]]
        state = 0;
        i = 0;
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i].isdigit():
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] in '+-':
                inputtype = OP
            elif s[i] in 'Ee':
                inputtype = E
                
            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 1 or state == 3 or state == 4
    
    def isSci(self, s):
        INVALID = 0;
        SPACE = 1;
        DIGIT = 2;
        E = 3;
        OP = 4;
        transitionTable = [[-1, 0, 1, -1, 5],
                           [-1, -1, 1, 2, -1],
                           [-1, -1, 3, -1, 4],
                           [-1, 6, 3, -1, -1],
                           [-1, -1, 3, -1, -1],
                           [-1, -1, 1, -1, -1],
                           [-1, 6, -1, -1, -1]]
        state = 0;
        i = 0;
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i].isdigit():
                inputtype = DIGIT
            elif s[i] in 'Ee':
                inputtype = E
            elif s[i] in '+-':
                inputtype = OP
            
            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 3 or state == 6
    
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False
        count = 0
        for i in range(0, len(s)):
            if s[i].isdigit():
                count += 1

        if count == 0 :
            return False

        
        if s.strip() == '.': return False
        
        if self.isInt(s) or self.isFloat(s) or self.isSci(s):
            return True
        else:
            return False


s = Solution()
print(s.isSci('46.E3'))