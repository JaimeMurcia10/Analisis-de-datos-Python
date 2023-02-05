import matplotlib.pyplot as plt
import numpy as np

# Quien levanta mas Peso en sentadilla Libre
personas = ["Jaime", "Miguel", "Jhonier", "Samuel", "Abbat"]
fuerza = [80, 120, 90, 86, 70]

fig, ax = plt.subplots()
ax.pie(fuerza, labels=personas)
ax.set_title('Fuerza de levantamiento de pesos')
plt.show()