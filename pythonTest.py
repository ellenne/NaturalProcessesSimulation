# Exercise 1
a = 2
b = 3 
c = -1
d = -0.5

print(-b//a-(-1)*c*b/d**c%c%d + (0 and 1 or not 0) )

# Exercise 2
def foo(x):
    x += 1
    if x<20:
        return foo(x)+1 # !recursion
    else:
        return x

x = 10
print(foo(x)) 

# Exercise 3
def change1(mylist):
    mylist[0] = 2
    print(mylist)
    return

def change2(mylist):
    #this is another variable that lives just inside here
    mylist = [1,2,3,4]
    print(mylist)
    return

mylist = [10,20,30]
change1(mylist)
print(mylist)
change2(mylist)
print(mylist) 

# Exercise 4
import numpy as np
x1 = np.arange(8)
x2 = np.reshape(x1,(2,4))
print("x1",x1)
print("x2",x2)
print(np.roll(x2,1,axis=0))