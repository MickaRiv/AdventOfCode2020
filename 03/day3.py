import numpy as np

def nTree(right,down):
    lines = np.arange(data.shape[0])[::down]
    columns = np.mod(np.arange(data.shape[0])*right,len(data[0]))
    path = [data[l][c] for l,c in zip(lines,columns)]
    return np.sum([p == '#' for p in path])
    

data = np.loadtxt("input",dtype=str,comments="%")
print(nTree(3,1))
pairs = [[1,1],[3,1],[5,1],[7,1],[1,2]]
nTrees = np.array([nTree(*args) for args in pairs],dtype=np.int64)
print(nTrees)
print(np.prod(nTrees))