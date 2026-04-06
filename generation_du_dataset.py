import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



N = 2000

#gineration de (x,y) 2000 point 
X = np.random.uniform(-5, 5, (N, 2)) 
# definition de  la fonction f(x,y) = sin(x²+y²) +0.5 cos(2x+2y)
def f(x,y) :
    return np.sin(np.sqrt(x**2 + y**2)) + 0.5* np.cos(2*x +2*y)
 
z= f(X[:,0] , X[:,0])  

z=z.reshape(2000 , 1)

# normalisation  des points (x,y):

mean =np.mean(X , axis=0 )
std =np.std(X,axis=0)
norm = (X - mean)/std

# normalisation  des z:

mean2 =np.mean(z)
std2 =np.std(z,axis=0)
norm2 = (z - mean)/std

#visulisation 

fig =plt.figure()
ax= fig.add_subplot(111,projection='3d')
ax.scatter(X[:,0], X[:,1], z, s=0.2)
plt.savefig("plot.png")
