import matplotlib.pyplot as plt

# Lista de tareas de Jaime Murcia
tareas = ["Hacer ejercicio", "Buscar trabajo", "Terminar el curso de Python"]

# Marcar tareas como completadas
completadas = []
for tarea in tareas:
    estado = input(f"¿Has completado la tarea {tarea}? (s/n): ")
    if estado == "s":
        completadas.append(tarea)

porcentaje = len(completadas) / len(tareas) * 100

plt.bar(["Tareas completadas"], [porcentaje], color='green')
plt.xlabel("Categoría")
plt.ylabel("Porcentaje de tareas completadas")
plt.title("Checklist de tareas diarias")
plt.ylim(0, 100)
plt.show()