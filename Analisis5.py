import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

personas = ["Jaime", "Miguel", "Jhonier", "Miller", "Andres"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2 * np.pi, 100)
z = np.array([0 for i in range(100)])
x = np.array([0 for i in range(100)])
y = np.array([0 for i in range(100)])
start = 0
fuerza = [75, 85, 90, 80, 100]
for i in range(len(fuerza)):
    end = start + (fuerza[i] / 100 * 2 * np.pi)
    x = np.concatenate([x, (np.sin(np.linspace(start, end, 100)))])
    y = np.concatenate([y, (np.cos(np.linspace(start, end, 100)))])
    start = end

# Graficar
ax.plot(x, y, z, color='blue')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
plt.title('Analisis de Fuerza')
plt.show()