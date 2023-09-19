from sklearn.impute import SimpleImputer
import numpy as np
array1 = np.array([[1, 2, np.nan], [np.nan, 2, 3], [4, 5, 8]])

imputacion = SimpleImputer(missing_values = np.nan, strategy="mean")
array2 = imputacion.fit_transform(array1)
print(array1)
print(array2)

from sklearn.preprocessing import StandardScaler

escalado = StandardScaler()
array3 =escalado.fit_transform(array2)
print(array3)

from sklearn.preprocessing import Normalizer
normalizar = Normalizer()
array4 = normalizar.fit_transform(array2)
print(array4)

# Regularizacion y Escalado
#Presentar 
