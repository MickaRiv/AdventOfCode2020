import numpy as np

data = []
with open("input","r") as fich:
    dic = {}
    for line in fich.readlines():
        if line == "\n":
            data.append(dic)
            dic = {}
        else:
            dic.update({bloc.split(":")[0]:bloc.split(":")[1] for bloc in line.replace("\n","").split()})
    data.append(dic)
    
keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
keysMinusCid = keys[:-1]
print(np.sum([np.all([key in np.array(list(d.keys()),dtype=str) for key in keysMinusCid]) for d in data]))

def isValid(dic):
    v = []
    try:
        v.append((len(dic["byr"]) == 4) and (1920 <= int(dic["byr"]) <= 2002))
        v.append((len(dic["iyr"]) == 4) and (2010 <= int(dic["iyr"]) <= 2020))
        v.append((len(dic["eyr"]) == 4) and (2020 <= int(dic["eyr"]) <= 2030))
        v.append(((dic["hgt"].endswith("cm")) and 150 <= int(dic["hgt"].replace("cm","").replace("in","")) <= 193) or
              ((dic["hgt"].endswith("in")) and 59 <= int(dic["hgt"].replace("cm","").replace("in","")) <= 76))
        v.append((len(dic["hcl"]) == 7) and dic["hcl"].startswith("#") and
              np.all([char in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] for char in dic["hcl"][1:]]))
        v.append(dic["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"])
        v.append(len(dic["pid"]) == 9)
        return np.all(v)
    except:
        return False

print(np.sum([isValid(d) for d in data]))