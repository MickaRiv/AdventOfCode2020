import numpy as np
import sys

def buildRulesDic(rulesString,dic={}):
    if len(dic) == 0:
        for ruleStr in rulesString:
            if '"a"' in ruleStr or '"b"' in ruleStr:
                info = ruleStr.split(": ")
                dic[int(info[0])] = [eval(info[1])]
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
                dic[key] = []
                for val in vals:
                    if len(val) == 2: 
                        dic[key].extend([c1+c2 for c1 in dic[val[0]] for c2 in dic[val[1]]])
                    elif len(val) == 1:
                        dic[key].extend(dic[val[0]])
        dic.update(buildRulesDic(rulesString,dic))    
    return dic

data = np.loadtxt("input",dtype=str,delimiter=",")
rules = np.array([d for d in data if ":" in d])
messages = np.array([d for d in data if ":" not in d])
rulesDic = buildRulesDic(rules)
lowRules = [r.lower() for r in rulesDic[0]]
okMsg = [msg in lowRules for msg in messages]
print(np.sum(okMsg),"/",len(messages))