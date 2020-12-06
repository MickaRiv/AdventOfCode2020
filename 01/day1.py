import numpy as np

def findSum(array,target):
    global p
    i = 0
    j = array.shape[0]-1
    sum = array[i] + array[j]
    while sum != target:
        p += 1
        if sum < target:
            i += 1
        else:
            j -= 1
        if i == j:
            return False, 0, 0
        sum = array[i] + array[j]
    return True, i, j
    
p = 0
data = np.sort(np.loadtxt("input",dtype=int))

boolean,i,j = findSum(data,2020)

print(i,j)
print(data[i],data[j])
print(data[i]+data[j])
print(data[i]*data[j])
print(p)

p = 0
data2 = np.sort(2020-data)
inds = [[i for i,v1 in enumerate(data) if data[0]+v1 <= v2] for v2 in data2]
out = [False,0,0]
for k,(ind,target) in enumerate(zip(inds,data2)):
    if len(ind) > 1:
        out = findSum(data[ind],target)
    if out[0]:
        break
    
res = [data.shape[0]-1-k,out[1],out[2]]

print("")
print(res)
print(data[res])
print(np.sum(data[res]))
print(np.prod(data[res]))
print(p)