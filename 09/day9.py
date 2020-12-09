import numpy as np

def sumOfPrevious(num,nPrevious):
    global data
    d = data[num-nPrevious:num]
    return [d_i + d_j for i,d_i in enumerate(d[:-1]) for d_j in d[i+1:]]

data = np.loadtxt("input",dtype=np.int64)
N = data.shape[0]
preamble = 25
nPrevious = 25
for i,d in enumerate(data[preamble:]):
    if d not in sumOfPrevious(i+preamble, nPrevious):
        break
invalidNumber = d
print(invalidNumber)

iMin = 0
iMax = 0
while True:
    if iMin == iMax or np.sum(data[iMin:iMax]) < invalidNumber:
        iMax += 1
    elif np.sum(data[iMin:iMax]) > invalidNumber:
        iMin += 1
    else:
        break
print(iMin,iMax,np.sum(data[iMin:iMax]),np.min(data[iMin:iMax])+np.max(data[iMin:iMax]))