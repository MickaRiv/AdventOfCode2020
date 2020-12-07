import numpy as np

data = np.loadtxt("input",dtype=str,delimiter=";")

dataDic = {}
for d in data:
    dSplitted = d.split(" bags contain ")
    dataDic[dSplitted[0]] = {}
    if "no other" not in dSplitted[1]:
        contentList = dSplitted[1].split(",")
        for content in contentList:
            contentSplitted = content.split()
            dataDic[dSplitted[0]][contentSplitted[1]+" "+contentSplitted[2]] = int(contentSplitted[0])

#print(dataDic)
searchList = ["shiny gold"]
nOld = 0
n = 1
while nOld < n:
    nOld = n
    for name,content in dataDic.items():
        if name not in searchList and np.any([key in searchList for key in content.keys()]):
            searchList.append(name)
    n = len(searchList)
print(n-1)
    
def contentNumber(name):
    if not dataDic[name]:
        return 0
    return np.sum([(contentNumber(contentName)+1)*contentNum for contentName,contentNum in dataDic[name].items()])
    
print(contentNumber("shiny gold"))