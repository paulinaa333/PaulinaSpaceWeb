notas = []

while True:
    entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
    if entrada.lower() == 'fin': #no
        break
    nota = float(entrada)
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Error: La nota debe ser entre 0 y 10")
    #try: #no

    #except ValueError:
    #    print("Ingrese un número válido o 'fin' para terminar")

if notas:
    promedio = sum(notas) / len(notas) #len nop
    print("Promedio de notas:", promedio)
    if promedio >= 7:
        print("El estudiante aprobó")
    else:
        print("El estudiante desaprobó")
else:
    print("No se ingresaron notas")
