# coding=utf-8

def qsort(L):
    equal = [L[-1]]
    small = []
    large = []
    
    if len(L) > 1:
        for item in L:
            if item < equal[0]:
                small.append(item)
            elif item == equal[0]:
                pass
            else:
                large.append(item)
        return qsort(small) + qsort(equal) + qsort(large)
    else:
        return L


def elgent_qsort(L):
    if len(L) > 1:
        return elgent_qsort([x for x in L[1:] if x< L[0]]) + [L[0]] + elgent_qsort([x for x in L[1:] if x>L[0]])
    else:
        return L
    pass

print(elgent_qsort([6, 2, 4]))
