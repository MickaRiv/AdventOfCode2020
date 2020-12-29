import numpy as np

def key(subject,threshold,loopsize):
    val = 1
    for _ in range(loopsize):
        val = iterKey(val,subject,threshold)
    return val    

def iterKey(val,subject,threshold):
    return val*subject % threshold
    
data = np.loadtxt("input",dtype=np.int64)
thresh = 20201227
val = 1
found = [0,0]
loop = 0
while not any(found):
    loop += 1
    val = iterKey(val,7,thresh)
    for i in range(2):
        if val == data[i]:
            found[i] = loop
if found[0]:
    print(key(data[1],thresh,found[0]))
else:
    print(key(data[0],thresh,found[1]))