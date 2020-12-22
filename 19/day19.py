import numpy as np
import re
import sys

def buildRulesDic(rulesString,dic={}):
    if len(dic) == 0:
        for ruleStr in rulesString:
            if '"a"' in ruleStr or '"b"' in ruleStr:
                info = ruleStr.split(": ")
                dic[int(info[0])] = eval(info[1])
        dic.update(buildRulesDic(rulesString,dic))
    elif len(dic) < len(rulesString):
        for ruleStr in rulesString:
            info = ruleStr.split(": ")
            key = int(info[0])
            if key in dic:
                continue
            nums = info[1].split(" | ")
            vals = [[int(n) for n in num.split()] for num in nums]
            if np.all([val in dic for val in [v for vs in vals for v in vs]]):
                dic[key] = "("+"|".join(["".join([dic[v] for v in val]) for val in vals])+")"
        dic.update(buildRulesDic(rulesString,dic))    
    return dic

data = np.loadtxt("input",dtype=str,delimiter=",")
rules = [d for d in data if ":" in d]
messages = [d for d in data if ":" not in d]

rulesDic = buildRulesDic(rules)
okMsgs = [i for i,msg in enumerate(messages) if re.search("\A"+rulesDic[0]+"\Z",msg)]
print(len(okMsgs),"/",len(messages))

for i,r in enumerate(rules):
    if r.startswith("8:"):
        for k in range(2,8):
            addStr = " ".join([str(num) for num in np.ones(k,dtype=int)*42])
            rules[i] += " | "+addStr
        print("New rule 8:")
        print(rules[i])
        break
for i,r in enumerate(rules):
    if r.startswith("11:"):
        for k in range(2,5):
            addStr = " ".join([str(num) for num in np.ones(k,dtype=int)*42])
            addStr += " "+" ".join([str(num) for num in np.ones(k,dtype=int)*31])
            rules[i] += " | "+addStr
        print("New rule 11:")
        print(rules[i])
        break

rulesDic = buildRulesDic(rules,{})
okMsgs = [i for i,msg in enumerate(messages) if re.search("\A"+rulesDic[0]+"\Z",msg)]
print(len(okMsgs),"/",len(messages))