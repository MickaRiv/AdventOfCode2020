import numpy as np

data = np.loadtxt("input",dtype=int)
dataSorted = np.sort(data)
dataSortedWithBounds = np.concatenate(([0],dataSorted,[dataSorted[-1]+3]))
deltas = dataSortedWithBounds[1:]-dataSortedWithBounds[:-1]
n1 = np.sum(deltas==1)
n3 = np.sum(deltas==3)
print(n1,n3,n1*n3)

def nPossibilities(a):
    if a <= 3:
        return 2**(a-1)
    else:
        return 2*nPossibilities(a-1)-1

oneCounts = [len(ones) for ones in "".join([str(d) for d in deltas]).split("3") if len(ones) > 0]
print(np.prod([nPossibilities(count) for count in oneCounts],dtype=np.int64))
