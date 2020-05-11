import numpy as np
import math

class Integrator:
        
    def __init__(self, xMin, xMax, N):
        '''
        Constructor of the class Integrator. It initialise all the instance variables.
        The variables are the following:
        xMin -  lower bound of the integral | needs to be an integer number less than xMax
        xMax -  upper bound of the integral | needs to be an integer number greater than xMin
        N    -  number of parts in which [xMin, xMax] is divided

        '''
        self.xMin = xMin
        self.xMax = xMax
        self.N = N
        self.value = 0  
       
    def integrate(self):       
        '''
        The integrate method numerically calculate the integral of the following function:
        x^2 * exp(-x) * sin(x) between xMin and xMax
        '''
        # to avoid to write self all the times
        N = self.N
        xMin = self.xMin
        xMax = self.xMax
        value = 0

        deltaX = (xMax - xMin) / N

        for i in range(N):            
            xi = xMin + i * deltaX
            value += self.calcFi(xi) * deltaX
        
        self.value = value
                   
    def show(self):
        print(self.value)        

    @staticmethod
    def calcFi(xi):
        return xi ** 2 * np.exp(-xi) * np.sin(xi)
        

examp = Integrator(1,3,200000)
examp.integrate()
examp.show()