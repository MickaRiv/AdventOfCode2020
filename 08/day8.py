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

nopOrJmpIndsinHisto = [i for i,p in enumerate(baseRun[3]) if data[p][0] in ["jmp","nop"]]

def solve(useHistory=False,quickRestart=False,JmpNopFilter=False):
    global nopOrJmpIndsinHisto
    changeInd = 0
    deadHisto = []
    success = False
    while not success:
        changeInd += 1
        if JmpNopFilter:
            changeCmd = nopOrJmpIndsinHisto[changeInd]+1
        else:
            changeCmd = changeInd
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

for inp in range(8):
    inputs = [bool(np.mod(inp//4,2)),bool(np.mod(inp//2,2)),bool(np.mod(inp,2))]
    count = 0
    print('--------------------------')
    print("Result:",solve(*inputs))
    print("Acceleration strategies activated:",inputs)
    print("Number of executed commands:", count)
