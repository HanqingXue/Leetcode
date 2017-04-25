class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        word_list = []
        alpha_word = {}
        appear = {}
        
        for item in board:
            word_list += item
            
        for alpha in word_list:
            alpha = alpha.lower()
            alpha_word[alpha] = word_list.count(alpha)
            appear[alpha] = 0
            
        for letter in word:
            if letter not in alpha_word:
                return False
            
            appear[letter] += 1
            if appear[letter] > alpha_word[letter]:
                return False
        
        return True


class Solution(object):


if __name__== '__main__':
    '''
    case:
    ["ABCE","SFCS","ADEE"]
    "ABCCED"
    '''
    s = Solution()
    print(s.exist(["ABCE","SFCS","ADEE"], 'ABCCED'))