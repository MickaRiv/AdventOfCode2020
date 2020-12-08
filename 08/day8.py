import numpy as np
import sys

def executeCommand(pos,acc,invert):
    cmd = data[pos].copy()
    if invert:
        cmd[0] = invertJmpNop(cmd[0])
    return pos+(cmd[0] == "jmp")*cmd[1]+(cmd[0] in ["acc","nop"]), acc+(cmd[0] == "acc")*cmd[1]

def invertJmpNop(string):
    if string in ["jmp","nop"]:
        return (string=="jmp")*"nop" + (string=="nop")*"jmp"
    else:
        return string

def runCode(changeCmd=-1,deadHisto=[],initHistos=[[],[]]):
    global count
    success = False
    posHistory = initHistos[0][:-1]
    accHistory = initHistos[1][:-1]
    pos = ([0]+initHistos[0])[-1]
    acc = ([0]+initHistos[1])[-1]
    while True:
        count += 1
        if pos in posHistory:
            break
        elif pos in deadHisto and len(posHistory)>changeCmd:
            break
        elif pos == len(data):
            success = True
            break
        posHistory.append(pos)
        accHistory.append(acc)
        pos,acc = executeCommand(pos,acc,len(posHistory)==changeCmd)
    return success, pos, acc, posHistory, accHistory

dataRaw = np.loadtxt("input",dtype=str)
data = [[d[0],int(d[1])] for d in dataRaw]

count = 0
baseRun = runCode()
print(baseRun[:3])
print(count)

def solve(quickRestart=False,useHistory=False):
    changeCmd = 0
    deadHisto = []
    success = False
    while not success:
        changeCmd += 1
        kwargs = {"changeCmd":changeCmd}
        if useHistory:
            kwargs["deadHisto"] = deadHisto
        if quickRestart:
            initHistos = [baseRun[3][:changeCmd],baseRun[4][:changeCmd]]
            kwargs["initHistos"] = initHistos
        success, pos, acc, pHisto, aHisto = runCode(**kwargs)
        if useHistory:
            deadHisto = np.unique(np.concatenate((deadHisto,pHisto)))
    return pos, acc

for inputs in [[False,False],[True,False],[False,True],[True,True]]:
    count = 0
    print(solve(*inputs))
    print(count)
