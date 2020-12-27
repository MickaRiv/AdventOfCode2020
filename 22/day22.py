import numpy as np
from copy import deepcopy

def combat(inputDecks,recursive=False):
    decks = deepcopy(inputDecks)
    memory = ["-".join([",".join([str(d) for d in deck]) for deck in decks])]
    while min(len(decks[0]),len(decks[1])) > 0:
        if recursive and np.all([len(deck)>deck[0] for deck in decks]):
            w = combat([deck[1:deck[0]+1] for deck in decks])[0]
        else:
            w = int(decks[1][0]>decks[0][0])
        decks[w].extend([decks[w][0],decks[1-w][0]])
        decks[w].pop(0)
        decks[1-w].pop(0)
        string = "-".join([",".join([str(d) for d in deck]) for deck in decks])
        if string in memory:
            return 0, []
        else:
            memory.append(string)
    return w, decks

data = np.loadtxt("input",dtype=str,delimiter=";").tolist()
initDecks = []
initDecks.append(np.array(data[1:data.index("Player 2:")],dtype=int).tolist())
initDecks.append(np.array(data[data.index("Player 2:")+1:],dtype=int).tolist())

winner, finalDecks = combat(initDecks)
print(np.dot(finalDecks[winner][::-1],1+np.arange(len(finalDecks[winner]))))

winner, finalDecks = combat(initDecks,recursive=True)
print(np.dot(finalDecks[winner][::-1],1+np.arange(len(finalDecks[winner]))))