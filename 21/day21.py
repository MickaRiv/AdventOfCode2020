import numpy as np

data = np.loadtxt("input",dtype=str,delimiter=";")
ingredients = [d.split("(")[0].split() for d in data]
allergens = [d.split("(contains ")[1].split(")")[0].split(", ") for d in data]
allIngredients = np.unique([i for ing in ingredients for i in ing])
allAllergens = np.unique([a for al in allergens for a in al])
allergenDic = {al:allIngredients.tolist() for al in allAllergens}

for ing, al in zip(ingredients,allergens):
    for a in al:
        allergenDic[a] = np.intersect1d(allergenDic[a],ing).tolist()
allAllergIngredients = np.unique([i for ing in allergenDic.values() for i in ing])
print(np.sum([np.sum([(i not in allAllergIngredients) for i in ing]) for ing in ingredients]))

done = []
for _ in range(len(allergenDic)):
    for al,alList in allergenDic.items():
        if (al not in done) and len(alList) == 1:
            for a,l in allergenDic.items():
                if a != al:
                    try:
                        l.remove(alList[0])
                    except:
                        pass
assert np.all([len(l) == 1 for a,l in allergenDic.items()])
print(",".join([allergenDic[key][0] for key in sorted(allergenDic)]))
            