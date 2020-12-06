import numpy as np

data = np.loadtxt("input",dtype=str)
minMax = np.array([d.split("-") for d in data[:,0]], dtype=int)
letter = np.array([d.replace(":","") for d in data[:,1]])
password = data[:,2]
N = np.sum([mM[0] <= np.sum([p_i == l for p_i in p]) <= mM[1] for l,p,mM in zip(letter,password,minMax)])
print(N)
N2 = np.sum([(p[mM[0]-1] == l) ^ (p[mM[1]-1] == l) for l,p,mM in zip(letter,password,minMax)])
print(N2)