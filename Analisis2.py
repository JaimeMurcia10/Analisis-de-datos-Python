import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


meses = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]])

# el valor esta en dolares con la tasa de cambio a pesos Colombianos de 4760 4/02/2023
ventas = np.array([[1150], [1500], [1750], [1800], [1850], [2000], [2350], [2400], [2250], [2500], [1900], [2550]])

model = LinearRegression().fit(meses, ventas)

futuros_meses = np.array([[13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24]])
predicciones = model.predict(futuros_meses)

plt.scatter(meses, ventas, color='red')
plt.plot(futuros_meses, predicciones, color='blue')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Regresión lineal de ventas mensuales')
plt.show()



