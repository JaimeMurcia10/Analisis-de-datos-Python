import matplotlib.pyplot as plt

# Datos de hábitos de Jaime
habitos = ["Ejercicio en el GYM", "Estudiar Analisis de datos ", "Montar Bicileta", "Buscar Trabajo"]
porcentajes = [70, 60, 20, 90]

# Crear gráfico circular
plt.pie(porcentajes, labels=habitos, startangle=90, counterclock=False, autopct="%1.1f%%")
plt.axis("equal")
plt.title("Porcentaje de hábitos de Jaime")
plt.show()