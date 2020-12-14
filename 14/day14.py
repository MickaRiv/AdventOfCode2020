import numpy as np

def execute(cmd,mask,mem,mode=1):
    if cmd[0].startswith("mask"):
        return cmd[1], mem
    else:
        if mode == 1:
            mem[cmd[0][4:-1]] = maskedValue(int(cmd[1]),mask)
        else:
            for address in maskedAddresses(int(cmd[0][4:-1]),mask):
                mem[address] = int(cmd[1])
        return mask, mem

def maskedValue(val,mask):
    N = len(mask)
    binVal = "0"*N+bin(val)[2:]
    maskedVal = ''.join([m if m != "X" else b for m,b in zip(mask,binVal[-N:])])
    return int(maskedVal,2)

def maskedAddresses(val,mask):
    N = len(mask)
    nums = np.array([N-i-1 for i,m in enumerate(mask) if m == "X"],dtype=np.int64)
    binVal = "0"*N+bin(val)[2:]
    maskedVal = ''.join([b if m == "0" else quickTransform(m) for m,b in zip(mask,binVal[-N:])])
    val = int(maskedVal,2)
    return [val+add for add in powersOf2(nums)]

def quickTransform(a):
    return "1"*(a=="1")+"0"*(a=="X")

def powersOf2(powers):
    if powers.shape[0] == 1:
        return [0,2**powers[0]]
    else:
        return np.concatenate((powersOf2(powers[:-1]),powersOf2(powers[:-1])+2**powers[-1]))

data = np.loadtxt("input",dtype=str,delimiter=" = ")
mem = {}
mask = ""
for cmd in data:
    mask, mem = execute(cmd, mask, mem)
print(np.sum(list(mem.values()),dtype=np.int64))

mem = {}
mask = ""
for cmd in data:
    mask, mem = execute(cmd, mask, mem, mode=2)
print(np.sum(list(mem.values()),dtype=np.int64))