import numpy as np

def stringTo2D(string):
    return eval("np.array([0,0])"+string.replace("nw","+np.array([0,1])").replace("ne","+np.array([-1,1])").replace("sw","+np.array([1,-1])").replace("se","+np.array([0,-1])").replace("w","+np.array([1,0])").replace("e","+np.array([-1,0])"))

def getNeighbours(loc):
    return [tuple((np.array(loc)+direct).tolist()) for direct in hexDirections]

def flipTile(tiles,locationString):
    loc = tuple(stringTo2D(locationString).tolist())
    if loc in tiles:
        tiles[loc] = np.mod(tiles[loc]+1,2)
    else:
        tiles[loc] = 1
    return tiles

def getAllNeighboursOfActive(tiles):
    neighbours = {}
    for tile in tiles:
        if tiles[tile]:
            neighbours[tile] = getNeighbours(tile)
    return neighbours

def onNumber(locs,tiles):
    n = 0
    for loc in locs:
        if loc in tiles:
            n += tiles[loc]
    return n

def evolve(loc,tiles):
    onNeighbours = onNumber(getNeighbours(loc),tiles)
    if loc in tiles:
        if (tiles[loc] and onNeighbours == 1) or onNeighbours == 2:
            return 1
    else:
        if onNeighbours == 2:
            return 1
    return 0
            
def iterate(tiles):
    newTiles = {}
    allNeighbours = np.array(list(getAllNeighboursOfActive(tiles).values()))
    shape = allNeighbours.shape
    allNeighbours = allNeighbours.reshape(shape[0]*shape[1],shape[2])
    candidates = np.unique(np.concatenate((np.array(list(tiles.keys())),allNeighbours)),axis=0)
    for candidate in candidates:
        newTiles[tuple(candidate.tolist())] = evolve(tuple(candidate.tolist()),tiles)
    return newTiles
    
hexDirections = np.array([[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,-1]])

data = np.loadtxt("input",dtype=str)
tiles = {}
for d in data:
    tiles = flipTile(tiles,d)
print(np.sum(list(tiles.values())))

for _ in range(100):
    tiles = iterate(tiles)
print(np.sum(list(tiles.values())))

