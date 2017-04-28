class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        elm = [False]*n
        visited = []
        for i in range(0, m):
            visited.append(elm)
        
        
        if len(word) <= 0 or word == None:
            return False
        
        if len(board) == None or len(board)<=0 or len(board[0]) <= 0:
            return False
       
        for i in range(0, m):
            for j in range(0, n):
                if self.dfs(board, word, 0, i, j, visited):
                    return True
        
        
        return False
    
    def dfs(self, board, word, index, i,  j, visited):
        print(index)
        if index == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) \
                 or visited[i][j] or board[i][j] != word[index]:
            return False
        
        visited[i][j] = True;
        res =    self.dfs(board, word, index+1, i - 1, j,   visited)  \
              or self.dfs(board, word, index+1, i + 1, j,   visited) \
              or self.dfs(board, word, index+1, i,     j-1, visited) \
              or self.dfs(board, word, index+1, i,     j+1, visited)
        
        visited[i][j] = False
    
        return res
    
if __name__== '__main__':
    '''
    case:
    ["ABCE","SFCS","ADEE"]
    "ABCCED"
    '''
    s = Solution()
    print(s.exist(["ABCE","SFCS","ADEE"], 'SE'))