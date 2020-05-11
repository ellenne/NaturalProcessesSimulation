import numpy as np

def explicit(s0,dt,n):
    A = 1 - 10*dt
    s = np.zeros(n+1)
    s[0] = 1
    for j in range(n):
        s[j+1] = s[j] * A
    return s

s = explicit(1,0.05,4)
print('s =',s)
print('s4 =', round(s[4],6))