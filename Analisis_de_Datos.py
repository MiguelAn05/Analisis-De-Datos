from datasets import load_dataset
import numpy as np



dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]


# Extrae la lista de edades del conjunto de datos
ages = data['age']

# Convierte la lista a un arreglo de NumPy
ages_array = np.array(ages)

# Calcula el promedio de las edades
average_age = np.mean(ages_array)

print(f'El promedio de edad de las personas participantes en el estudio es {average_age}')



