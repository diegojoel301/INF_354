#import pandas as pd
#datos = pd.read_csv("vegetable.csv")

#print(datos)

import numpy as np

print(np.NaN)

list1 = [[np.nan, 4, 5], 
         [4, 3, np.nan],
         [1, 2, 1]]
matriz1 = np.array(list1)
print(list1)

from sklearn.impute import SimpleImputer

imputar = SimpleImputer(missing_values=np.nan, strategy="mean")
salida_imputar = imputar.fit_transform(matriz1)

print(salida_imputar)

for i in range(3):
    for j in range(3):
        
        if list1[i][j] is np.nan:
            promedio = 0
            nro_elem = 0
            for k in list1:
                if k[j] is not np.nan:
                    promedio += int(k[j])
                    nro_elem += 1

            list1[i][j] = promedio / nro_elem

print(np.array(list1))

from sklearn.datasets import load_iris

data = load_iris()

x = data.data
y = data.target
#print(x)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

Yt = y_train.T

print(y_test)
print(y_train.shape)
print(y_test.shape)
print(Yt.shape)


#Investigar procesamiento de matrices sparce

# El motivo de normalizar es la representacion de los datos

