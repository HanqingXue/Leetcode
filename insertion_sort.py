import random
# iinsterion_sort direct way

class Sort():
    # iinsterion_sort direct way

    def intertion_sort(self, L):
        for i in range(1, len(L)):
            j = i
            while j > 0 and L[j] <  L[j - 1]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                j -= 1
        return L
    
    def bubble_sort(self, L):
        for i in range(0, len(L)):
            for j in range(0, len(L)):
                if L[i] > L[j]:
                    L[i], L[j] = L[j], L[i] 
        return L

    def select_sort(self, L):
        for i in range(0, len(L)):
            index = i
            for j in range(0, len(L)):
                if L[i] < L[j]:
                    index = j
            
            if index != i:
                L[index], L[i] = L[i], L[index]
                
        return L
    
    def shell_sort(self, L):
        gap = len(L) / 2
        for i in range(0, len(L)):
            j = i
            while j < i + gap:
                k = j
                while k > 0 and L[k] > L[k-1]:
                    L[k], L[k-1] = L[k-1], L[k]
                    k -= 1
                gap /= 2
        return L
        
if __name__ == '__main__':
    test = random.sample(range(1000), 100)
    S  = Sort()
    interset = S.intertion_sort(test)
    bubble = S.bubble_sort(test)
    select = S.select_sort(test)
    test.sort()
    assert bubble == test
    print(bubble)
    #print(intertion_sort(test))