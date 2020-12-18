import numpy as np

def ev(string):
    splitted = string.split()
    if len(splitted) == 3:
        return str(eval(string))
    else:
        if sumFirst and "+" in string:
            ind = splitted.index("+")
        else:
            ind = 1
        return ev(" ".join(splitted[:ind-1])+" "+str(eval(" ".join(splitted[ind-1:ind+2])))+" "+" ".join(splitted[ind+2:]))

data = np.loadtxt("input",dtype=str, delimiter=",")

sumFirst = False
print(np.sum([int(eval("ev('"+d.replace("(","'+ev('").replace(")","')+'")+"')")) for d in data],dtype=np.int64))

sumFirst = True
print(np.sum([int(eval("ev('"+d.replace("(","'+ev('").replace(")","')+'")+"')")) for d in data],dtype=np.int64))