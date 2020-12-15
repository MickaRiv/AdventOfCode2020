import numpy as np

def takeTurns(num,n,hist,nTurns):
    while n < nTurns:
        if np.mod(n,nTurns//100) == 0:
            print(str(100*n//nTurns)+"%")
        numOld = num
        if num in hist.keys():
            num = n-hist[num]
        else:
            num = 0
        hist[numOld] = n
        n += 1
    return num

data = [0,14,1,3,7,9]
hist = {d:i+1 for i,d in enumerate(data[:-1])}
valEnd1 = takeTurns(data[-1],len(data),hist,2020)

data = [0,14,1,3,7,9]
hist = {d:i+1 for i,d in enumerate(data[:-1])}
valEnd2 = takeTurns(data[-1],len(data),hist,30000000)
print(valEnd1, valEnd2)