# Draw a sqare (-1\leq x\leq 1,-1\leq y\leq 1)(−1≤x≤1,−1≤y≤1)
# Generate N points(x,y), which are distributed randomly in the square.
# Draw a circle ((x_0,y_0)=(0,0), r=1(x0,y0)=(0,0),r=1)
# Count the number of the points CC which fall in the circle.
# When this experiment is repeated numerous times, to which value will the average of C/N converge

from random import randint
from random import randrange
import decimal

simulations = 100
output = []

for i in range(simulations):
    N = randint(1, 100) 
    p = []
    inside = 0
    outside = 0
    for j in range(N):
        x = float(decimal.Decimal(randrange(-100, 100))/100)
        y = float(decimal.Decimal(randrange(-100, 100))/100)
        point = (x, y)
        p.append(point)
        if x ** 2 + y ** 2 > 1 :
            outside += 1
        else:
            inside += 1

    print(inside / N)
    output.append(inside / N)

