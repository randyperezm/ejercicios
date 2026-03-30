notas = {
    "matematicas": 4.5,
    "ingles": 4.0,
    "programacion": 5.0
}

suma = 0

for n in notas.values():
    suma += n

promedio = suma / len(notas)

print("Promedio:", promedio)