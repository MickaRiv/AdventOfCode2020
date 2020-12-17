import numpy as np

def evolve(center,neighbours):
    return (np.sum(neighbours) == 3) + (center and np.sum(neighbours) == 2)

def grow(array):
    sizes = np.array(array.shape)
    newArray = np.zeros(sizes+2,dtype=int)
    if len(sizes) == 3:
        newArray[1:-1,1:-1,1:-1] = array
    if len(sizes) == 4:
        newArray[1:-1,1:-1,1:-1,1:-1] = array
    return newArray

def iterate(cubes):
    cubes = grow(cubes)
    sizes = np.array(cubes.shape)
    if len(sizes) == 3:
        return update3(cubes,sizes)
    elif len(sizes) == 4:
        return update4(cubes,sizes)

def update3(cubes,sizes):
    newCubes = cubes.copy()
    for i in range(sizes[0]):
        for j in range(sizes[1]):
            for k in range(sizes[2]):
                neighbours = cubes[max(0,i-1):min(sizes[0],i+2),max(0,j-1):min(sizes[1],j+2),max(0,k-1):min(sizes[2],k+2)].flatten().tolist()
                neighbours.remove(cubes[i,j,k])
                newCubes[i,j,k] = evolve(cubes[i,j,k], neighbours)
    return newCubes

def update4(cubes,sizes):
    newCubes = cubes.copy()
    for i in range(sizes[0]):
        for j in range(sizes[1]):
            for k in range(sizes[2]):
                for l in range(sizes[3]):
                    neighbours = cubes[max(0,i-1):min(sizes[0],i+2),max(0,j-1):min(sizes[1],j+2),max(0,k-1):min(sizes[2],k+2),max(0,l-1):min(sizes[3],l+2)].flatten().tolist()
                    neighbours.remove(cubes[i,j,k,l])
                    newCubes[i,j,k,l] = evolve(cubes[i,j,k,l], neighbours)
    return newCubes

data = np.loadtxt("input",dtype=str,comments="%")

cubes = np.array([[[int(char=="#") for char in line] for line in data]])
for _ in range(6):
    cubes = iterate(cubes)
print(np.sum(cubes))

cubes = np.array([[[[int(char=="#") for char in line] for line in data]]])
for _ in range(6):
    cubes = iterate(cubes)
print(np.sum(cubes))