
import numpy as np
import plotly.graph_objects as go
#----------------------------------
#        dataset  :    

N = 2000

X = np.random.uniform(-5, 5, (N, 2))

def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) + 0.5 * np.cos(2*x + 2*y)

z = f(X[:, 0], X[:, 1])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
norm = (X - mean) / std

mean2 = np.mean(z)
std2 = np.std(z)
norm2 = (z - mean2) / std2

fig = go.Figure(data=[
    go.Scatter3d(
        x=norm[:,0],
        y=norm[:,1],
        z=norm2,
        mode='markers',
        marker=dict(size=1)
    )
])

fig.show()

#------ parity 2:
# couche 1
W1 = np.random.randn(2, 64) * np.sqrt(2 / 2)
b1 = np.zeros((1, 64))

# couche 2
W2 = np.random.randn(64, 64) * np.sqrt(2 / 64)
b2 = np.zeros((1, 64))

# sortie
W3 = np.random.randn(64, 1) * np.sqrt(2 / 64)
b3 = np.zeros((1, 1)) 

def relu(x):
    return np.maximum(0, x)

# couche 1
Z1 = norm @ W1 + b1
A1 = relu(Z1)

# couche 2
Z2 = A1 @ W2 + b2
A2 = relu(Z2)

# sortie (linéaire)
Z3 = A2 @ W3 + b3
y_pred = Z3

y_true = norm2.reshape(-1, 1)

loss = np.mean((y_true - y_pred) ** 2)

print("erreur =", loss)