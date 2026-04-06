import numpy as np



N = 2000

#gineration de (x,y) 2000 point 
X = np.random.uniform(-5, 5, (N, 2))  
# definition de  la fonction f(x,y) = sin(x²+y²) +0.5 cos(2x+2y)
def f(x,y) :
    return np.sin(np.scrt(x**2 + y**2)) + 0.5* np.cos(2*x +2*y)
 
z= f(X[:,0] , X[:,0])  

z=z.rechape(2000 , 1)
