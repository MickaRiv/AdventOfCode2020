import numpy as np
from functools import reduce

def readMultiline(fileName,dataType):
    data = []
    with open(fileName,"r") as fich:
        data_i = []
        for line in fich.readlines():
            if line == "\n":
                data.append(data_i)
                data_i = []
            else:
                data_i.append(dataType(line.replace("\n","")))
        data.append(data_i)
    return(data)
        
print(np.sum([np.unique([char for string in listOfString for char in string]).shape[0] for listOfString in readMultiline("input",str)]))
print(np.sum([len(reduce(np.intersect1d,[[char for char in string] for string in listOfString])) for listOfString in readMultiline("input",str)]))