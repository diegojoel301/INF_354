from sklearn.datasets import load_iris
import numpy as np 

data = load_iris()

X = data.data

y = data.target

yp = np.asarray(y, dtype = "float")
yp[140] = np.nan
ypos = np.array(range(yp.shape[0]))
yp1 = yp
print(yp)
print(np.isnan(yp[140]))
print(np.isnan(yp[141]))
media = np.mean(np.where(np.isnan(yp1), 0, yp1))
yp2 = np.where(np.isnan(yp), media, yp)
print(yp2)
matriz = np.array([[1, 2, 3], [6, 7, 8], [3, 7, 1]])

print(np.mean(matriz))

print(np.mean(matriz, axis = None))
print(np.mean(matriz, axis = 0))
print(np.mean(matriz, axis = 1))

print(X)
print(X[1, :])

c3 = matriz[:,0]
c3[2] = 3.5
print(c3)
matriz[:,0] = c3
print(matriz)
