import pandas as pd 
import matplotlib.pyplot as plt

workbook1 = "base.xlsx"

df = pd.read_excel(workbook1)

columna = df['SECTOR']

# Crear histograma
plt.hist(columna, bins=20)
plt.xlabel('datos')
plt.ylabel('Frecuencia')
plt.title('Histograma del sector economico')
plt.show()