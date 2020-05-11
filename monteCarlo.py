from random import randint
import numpy as np

allSuccesses = []

attempts = 10000

simulations = 1000

for j in range(simulations):
    success = 0
    for i in range(attempts):
        if randint(0, 1) + randint(0, 1) + randint(0, 1) + randint(0, 1) == 3:
            success += 1
    allSuccesses.append(success/attempts)
    print(f"Simulation {j} completed - success rate {success/attempts}")


print(f"Maximum success rate={np.max(allSuccesses)}")
print(f"Minimum success rate={np.min(allSuccesses)}")
print(f"St Dev success rate={np.std(allSuccesses)}")

