'''
Suppose you have 10 piles of 10 coins each.

Say now that you are playing the following game. At each turn you pick a coin from each pile and move it in 
a randomly selected pile (it can be any of the piles). You can repeat the process an arbitrary amount of times. 
If a pile becomes empty, you cannot move a coin back to it. Therefore if there is only one pile left 
the game is over.

Can you guess the number of piles that will remain if you are allowed to play an infinite amount of turns?

If not, the program attached "piles.py" is an implementation of this game. You can change the parameter 
maxIter which changes the maximal number of turns to get a better understanding of what is actually 
happening with the number of piles.
'''


import numpy as np
import random

numberOfPiles = 10
maxIter = 10000000

piles = np.empty(numberOfPiles)
piles.fill(numberOfPiles)
totPiles = np.sum(piles)
numPiles = numberOfPiles
x = 0;
while (x < maxIter and piles.size > 1):
    # the function np.nonzero returns the position of the 
    # elements that are nonzero in an array
    # therefore using as argument of a list it gives you only 
    # those piles that are not empty
    piles = piles[np.nonzero(piles)]
    for i in np.arange(piles.size):
        # takes a token from the first pile available and reassign it randomly to another pile
        piles[i] -= 1
        num = np.random.randint(piles.size)
        piles[num] += 1
    numPiles = piles.size
    x += 1


print("The number of piles remaining are: ", numPiles)