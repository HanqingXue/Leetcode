import pulp

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
    
    def LP(self):
        C = []
        F = [self.Y1, self.Y2, self.Y3, self.Y4, self.Y5, self.Y6]
        sub_sets = []
        for i in range(0, len(F)):
            sub_sets.append('Sub{}'.format(i+1))
        
        subject = []
        for i in range(0, 12):
            st = [-1]*len(F)
            for j in range(0, len(F)):
                if i in F[j]:
                    st[j] = 1
                else:
                    st[j] = 0
            subject.append(st)
        
        scp_model = pulp.LpProblem('SCP', pulp.LpMinimize)
        x = pulp.LpVariable.dict('x_%s', sub_sets, lowBound=0, upBound=1)
        cost = dict(zip(sub_sets, [1]*len(F)))
        
        scp_model += sum( cost[i] * x[i] for i in sub_sets)
        parameters = []
        for i in range(0, len(subject)):
            pars = dict(zip(sub_sets, subject[i]))
            parameters.append(pars)
        
        for item in range(0, len(parameters)):
            scp_model += sum( [parameters[item][i]*x[i] for i in sub_sets]) >= 1.0
            
        scp_model.solve()
        lp_result = [x[item].value() for item in sub_sets]
        f = max([sum(item) for item in subject])
        if f == 0:
            f = 0.0001
            
        for i in range(0, len(lp_result)):
            if lp_result[i] > 1.0 / f:
                C.append(F[i])
        return C

    def round(self):
        C = []
        F = [self.Y1, self.Y2, self.Y3, self.Y4, self.Y5, self.Y6]
        sub_sets = []
        for i in range(0, len(F)):
            sub_sets.append('Sub{}'.format(i + 1))

        subject = []
        for i in range(0, 12):
            st = [-1] * len(F)
            for j in range(0, len(F)):
                if i in F[j]:
                    st[j] = 1
                else:
                    st[j] = 0
            subject.append(st)
    
        scp_model = pulp.LpProblem('SCP', pulp.LpMinimize)
        x = pulp.LpVariable.dict('x_%s', sub_sets, lowBound=0, upBound=1)
        cost = dict(zip(sub_sets, [1] * len(F)))
    
        scp_model += sum(cost[i] * x[i] for i in sub_sets)
        # parameters
        parameters = []
        for i in range(0, len(subject)):
            pars = dict(zip(sub_sets, subject[i]))
            parameters.append(pars)
    
        for item in range(0, len(parameters)):
            scp_model += sum([parameters[item][i] * x[i] for i in sub_sets]) >= 1.0
    
        scp_model.solve()
    
        lp_result = [x[item].value() for item in sub_sets]
        f = max([sum(item) for item in subject])
        if f == 0:
            f = 0.0001
    
        for i in range(0, len(lp_result)):
            if lp_result[i] > 1.0 / 2:
                C.append(F[i])
    
        return C
if __name__ == '__main__':
    S = SCP()
    #print(S.greedy())
    LP = S.LP()
    ROUND = S.round()
    assert LP == ROUND
    
