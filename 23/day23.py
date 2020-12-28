import numpy as np
import sys

def nextBelow(val,possible=None,avoid=None):
    if possible is not None:
        return next(num for num in np.mod(val-np.arange(4)-2,nCups)+1 if num in possible)
    elif avoid is not None:
        return next(num for num in np.mod(val-np.arange(4)-2,nCups)+1 if num not in avoid)

def move(cups,current):
    doubleCups = 2*cups
    remaining = doubleCups[current+4:nCups+current]
    ind = remaining.index(nextBelow(cups[current],possible=remaining))
    doubleNewCups = 2*([cups[current]]+remaining[:ind+1]+doubleCups[current+1:current+4]+remaining[ind+1:])
    return doubleNewCups[nCups-current:2*nCups-current]

def moveManagingNextOnly(nextCups,currentCup):
    pickedCups = [nextCups[currentCup],nextCups[nextCups[currentCup]],nextCups[nextCups[nextCups[currentCup]]]]
    destination = nextBelow(currentCup,avoid=pickedCups)
    nextCups[currentCup] = nextCups[pickedCups[-1]]
    nextCups[pickedCups[-1]] = nextCups[destination]
    nextCups[destination] = pickedCups[0]
    return nextCups

print("--- Part 1 ---")
cups = [1,5,7,6,2,3,9,8,4]
nCups = len(cups)
for i in range(100):
    cups = move(cups,np.mod(i,nCups))
res1 = "".join([str(num) for num in cups[cups.index(1)+1:]])+"".join([str(num) for num in cups[:cups.index(1)]])
print("--- Done ---")

print("--- Part 2 ---")
cups = [1,5,7,6,2,3,9,8,4,10]
nCupsTot = 1000000
nextCups = [0]+[cups[np.mod(cups.index(i)+1,nCups+1)] for i in range(1,nCups+1)]+np.arange(nCups+2,nCupsTot+1).tolist()+[cups[0]]
nCups = nCupsTot
nTurns = 10000000
currentCup = cups[0]
for i in range(nTurns):
    if np.mod(i,nTurns//100) == 0: print(100*i//nTurns,"%")
    nextCups = moveManagingNextOnly(nextCups,currentCup)
    currentCup = nextCups[currentCup]
print("--- Done ---")
print("Result Part 1:",res1)
print("Result Part 2:",nextCups[1]*nextCups[nextCups[1]])
