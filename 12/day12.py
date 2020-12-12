import numpy as np

def apply(instruction, *args):
    cmd = instruction[0]
    val = int(instruction[1:])
    if cmd in cycle:
        return *absoluteMove(cmd,val,*args), orientation
    else:
        return relativeMove(cmd,val,*args)
    
def apply2(instruction, east, north, wpEast, wpNorth):
    cmd = instruction[0]
    val = int(instruction[1:])
    if cmd in cycle:
        return east, north, *absoluteMove(cmd,val,wpEast,wpNorth)
    elif cmd == "F":
        return *absoluteMove("N",wpNorth*val,*absoluteMove("E",wpEast*val,east,north)), wpEast, wpNorth
    else:
        return east, north, *rotate(cmd,val,wpEast,wpNorth)
    
def rotate(cmd, val, east, north):
    if cmd == "R":
        rotMat = np.array([[0,1],[-1,0]])
    else:
        rotMat = np.array([[0,-1],[1,0]])
    vect = np.array([east,north])
    return np.dot(np.linalg.matrix_power(rotMat,val//90),vect)
    
def relativeMove(cmd, val, east, north, orientation):
    if cmd == "F":
        return *absoluteMove(orientation, val, east, north), orientation
    else:
        sign = (cmd=="R") - (cmd=="L")
        current = cycle.index(orientation)
        orientation = cycle[np.mod(current+sign*val//90,4)]
        return east, north, orientation
    
def absoluteMove(cmd, val, east, north, *args):
    east += val * ((cmd=="E") - (cmd=="W"))
    north += val * ((cmd=="N") - (cmd=="S"))
    return east, north

data = np.loadtxt("input",dtype=str)
cycle = ["N","E","S","W"]
east = 0
north = 0
orientation = "E"
for instruction in data:
    east, north, orientation = apply(instruction, east, north, orientation)
print(east,north,abs(east)+abs(north))

east = 0
north = 0
wpEast = 10
wpNorth = 1
for instruction in data:
    east, north, wpEast, wpNorth = apply2(instruction, east, north, wpEast, wpNorth)
print(east,north,abs(east)+abs(north))