import numpy as np
import sys
from scipy.ndimage import correlate

data = np.loadtxt("input",dtype=str,delimiter=",",comments="%")
n = 10
dic = {}
dic01 = {}
dicBord = {}
for i in range(0,data.shape[0],n+1):
    dic[int(data[i].split()[1][:-1])] = data[i+1:i+n+1]
    dic01[int(data[i].split()[1][:-1])] = np.array([[int(d == "#") for d in dat] for dat in data[i+1:i+n+1]])
    dicBord[int(data[i].split()[1][:-1])] = {}
    dicBord[int(data[i].split()[1][:-1])]["up"] = data[i+1]
    dicBord[int(data[i].split()[1][:-1])]["down"] = data[i+n][::-1]
    dicBord[int(data[i].split()[1][:-1])]["left"] = "".join([d[0] for d in data[i+1:i+n+1]])[::-1]
    dicBord[int(data[i].split()[1][:-1])]["right"] = "".join([d[-1] for d in data[i+1:i+n+1]])

sides = ["up","left","down","right"]

size = int(np.sqrt(len(dicBord)))
neighbours = {}
for tile,tileData in dicBord.items():
    neighbours[tile] = {s:[] for s in sides}
    for otherTile,otherTileData in dicBord.items():
        if tile != otherTile:
            for side in sides:
                for opSide in sides:
                    if tileData[side] == otherTileData[opSide][::-1]:
                        neighbours[tile][side].append({"num":otherTile,"side":opSide,"flipped":False})
                    if tileData[side] == otherTileData[opSide]:
                        neighbours[tile][side].append({"num":otherTile,"side":opSide,"flipped":True})
            if len(neighbours[tile][side]) > 1:
                print("There may be more than one !")
                sys.exit()

corners = [key for key,val in neighbours.items() if np.sum([v == [] for v in val.values()]) >= 2]
print(np.prod(corners,dtype=np.int64))

def sideAfterRotate(side,r):
    return sides[np.mod(sides.index(side)+r,len(sides))]

def sideToSideRot(sideStart,sideEnd):
    return sides.index(sideEnd) - sides.index(sideStart)

def opposite(side):
    return sideAfterRotate(side,2)

def flip(array,direction):
    if direction in ["down","up"]:
        return np.fliplr(array)
    else:
        return np.flipud(array)

def fillLine(iList,jList,direction,checkFlip=False):
    global fullImg,fullImgData
    for k,(i,j) in enumerate(zip(iList[1:],jList[1:])):
        prevRot = fullImgData[iList[k]][jList[k]]["rot"]
        prevFlipped = fullImgData[iList[k]][jList[k]]["flipped"]
        if checkFlip and k == 0 and prevFlipped:
            prevRot += 2
        rawData = neighbours[fullImgData[iList[k]][jList[k]]["num"]][sideAfterRotate(direction,-prevRot)][0]
        fullImgData[i][j] = {"num":rawData["num"],"rot":sideToSideRot(rawData["side"],opposite(direction)),"flipped":rawData["flipped"]^prevFlipped}
        fullImg[i][j] = np.rot90(dic01[fullImgData[i][j]["num"]],fullImgData[i][j]["rot"])
        if fullImgData[i][j]["flipped"]:
            fullImg[i][j] = flip(fullImg[i][j],direction)
        if direction == "down" and np.any(fullImg[i][j][0] != fullImg[iList[k]][jList[k]][-1]):
            print("down wrong")
            sys.exit()
        if direction == "right" and np.any(fullImg[i][j][:,0] != fullImg[iList[k]][jList[k]][:,-1]):
            print("right wrong")
            sys.exit()
    
fullImg = [[[] for _ in range(size)] for _ in range(size)]
fullImgData = [[{} for _ in range(size)] for _ in range(size)]
borders = [key for key,val in neighbours[corners[0]].items() if val == []]
k = 0
rotSides = [sideAfterRotate(side,k) for side in borders]
while not ("up" in rotSides and "left" in rotSides):
    k += 1
    rotSides = [sideAfterRotate(side,k) for side in borders]
fullImgData[0][0] = {"num":corners[0],"rot":k,"flipped":False}
fullImg[0][0] = np.rot90(dic01[fullImgData[0][0]["num"]],fullImgData[0][0]["rot"])
fillLine(np.arange(size),np.zeros(size,dtype=int),"down")
for line in range(size):
    fillLine(np.ones(size,dtype=int)*line,np.arange(size),"right",checkFlip=True)
fullMap = np.block([[bloc[1:-1,1:-1] for bloc in fullImgLine] for fullImgLine in fullImg])

seaMonsterString = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "]
seaMonster = np.array([[int(d == "#") for d in dat] for dat in seaMonsterString])
for _ in range(2):
    for k in range(4):
        nMonsters = np.sum(np.array(correlate(np.rot90(fullMap,k),seaMonster, mode='constant', cval=0.0)/np.sum(seaMonster),dtype=int))
        if nMonsters > 0:
            print(np.sum(fullMap)-nMonsters*np.sum(seaMonster))
            sys.exit()
    fullMap = np.fliplr(fullMap)
print("Not found")