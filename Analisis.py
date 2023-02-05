import matplotlib.pyplot as plt

# los GymBros de Zona Life Brasil quien levanta mas peso muerto
pesos = {'Jaime': 100, 'Miguel': 140, 'Jhonier': 115, 'Miller': 170}

nombres = list(pesos.keys())
valores = list(pesos.values())

plt.bar(nombres, valores)
plt.xlabel('GymBros')
plt.ylabel('Peso en kg')
plt.title('Quién levanta más peso')

plt.show()