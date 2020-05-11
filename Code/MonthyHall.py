from random import randrange

winStay = 0
winSwitch = 0

N = 1000000
i = 0

while i <= N:
    doors = [0, 0, 0]
    # 0 is a goat
    # 1 is a car

    # let's generate an integer between 1 and 3 for the position where we put the car 
    pos = randrange(3)

    # let's place the car in the correct door
    doors[pos] = 1

    # now the person chooses a door
    choice = randrange(3)

    # let's compare the two strategies
    stay = choice

    goatsDoors = [index for index, value in enumerate(doors) if value == 0]

    otherGoat = list( set(goatsDoors) - set([choice]) )[0]

    switch = list(set([0, 1, 2]) - set([otherGoat]) - set([choice]))[0]

    if doors[stay] == 1:
        winStay += 1

    elif doors[switch] == 1:
        winSwitch += 1

    i += 1    

    print(f"Iteration {i} out {N} {i/N*100:.2f} : Stay win = {winStay} - Switch win = {winSwitch}")

