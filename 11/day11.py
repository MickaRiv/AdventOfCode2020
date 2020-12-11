import numpy as np
import sys

def addBoundaries(data,boundChar):
    newData = np.array([[boundChar for j in range(data.shape[1]+2)] for i in range(data.shape[0]+2)])
    newData[1:-1,1:-1] = data
    return newData

def updateUntilConv(data,*args,**kwargs):
    nChanges = 1
    iCount = 0
    while nChanges > 0:
        oldData = data.copy()
        data = update(data,*args,**kwargs)
        nChanges = np.sum(oldData != data)
        iCount += 1
        print("Loop "+str(iCount)+" - "+str(nChanges)+" changes")
    print("--- Convergence reached ---")
    return data

def update(data,method="proxim",threshold=4):
    nRows = data.shape[0]
    nColumns = data.shape[1]
    newData = data.copy()
    for i in range(1,nRows-1):
        for j in range(1,nColumns-1):
            if data[i,j] != ".":
                newData[i,j] = evolve(data[i,j],neighbours(data,i,j,method),threshold)
    return newData

def neighbours(data,i,j,method="proxim"):
    if method == "proxim":
        return np.concatenate((data[i-1,j-1:j+2],data[i,j-1:j+2:2],data[i+1,j-1:j+2]))
    elif method == "visib":
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        return np.array([firstSeen(*direction,data,i,j) for direction in directions])
    
def firstSeen(stepX,stepY,data,i,j):
    nRows = data.shape[0]
    nColumns = data.shape[1]
    k = 1
    while True:
        seen = data[i+stepX*k,j+stepY*k]
        if seen in ["L","#"]:
            break
        k += 1
        if not 0 <= i+stepX*k < nRows or not 0 <= j+stepY*k < nColumns:
            break
    return seen
            
def evolve(center,neighbours,threshold):
    if center == "L" and "#" not in neighbours:
        return "#"
    elif center == "#" and np.sum(neighbours=="#") >= threshold:
        return "L"
    else:
        return center

data = np.loadtxt("input",dtype=str,comments="%")
data = np.array([[char for char in line] for line in data])
data = addBoundaries(data,".")

dataFin1 = updateUntilConv(data)
res1 = np.sum([np.sum([seat=="#" for seat in d]) for d in dataFin1])

dataFin2 = updateUntilConv(data,"visib",5)
res2 = np.sum([np.sum([seat=="#" for seat in d]) for d in dataFin2])

print("Solution to problem 1: ",res1)
print("Solution to problem 2: ",res2)
