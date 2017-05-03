class SCP(object):
    def __init__(self):
        super(SCP, self).__init__()
        self.X  = set([x for x in range(0, 12)])
        self.Y1 = [0, 1, 2, 3, 4, 5, 6]
        self.Y2 = [5, 6, 8, 9]
        self.Y3 = [1, 4, 7, 10]
        self.Y4 = [2, 5, 8, 11]
        self.Y5 = [3, 6, 9, 12]
        self.Y6 = [10, 11]
        
    def greedy(self):
        F = [self.Y1, self.Y2, self.Y3, self.Y4, self.Y5, self.Y6]
        U = self.X
        C = []
        state = [0]*len(F)
        intersetion = {}
        index = -1
        while len(U) != 0:
            
            for i in range(0, len(F)):
                if state[i] == -1:
                    intersetion[i] = -1
                    continue
                intersetion[i] = len(set(F[i]) & U)
            
            for item in intersetion:
                if intersetion[item] == max(intersetion.values()):
                    index = item
                    break
           
            U = U - set(F[index])
            C.append(F[index])
            state[index] = -1
        
        return C
    
if __name__ == '__main__':
    S = SCP()
    print(S.greedy())