import numpy as np

def getSeatInfo(string):
    row = int(string[:7].replace("F","0").replace("B","1"),base=2)
    column = int(string[7:].replace("L","0").replace("R","1"),base=2)
    return row, column, row*8+column

def getLonely(array):
    return array[[not ((val-1 in array) or (val+1 in array)) for val in array]]

data = np.loadtxt("input",dtype=str)

print(np.max([getSeatInfo(d)[2] for d in data]))

allNums = np.arange(1024)
foundNums = [getSeatInfo(d)[2] for d in data]
print(getLonely(np.setdiff1d(allNums,foundNums)))