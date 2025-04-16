#Registro de nota de un estudiante
notas=[]
#Le pide al usuario que ingrese sus notas y que ponga 'fin' cuando haya terminado
while True:
    entrada=input("Ingresa una nota (o escribe 'fin' para terminar):")
    if entrada.lower()=='fin':
        break
#Revisa si la nota entra en el rango de 0 y 10.
    try: 
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Error: La nota debe ser entre 0 y 10")
    except ValueError:
        print("Ingrese un numero valido o 'fin' para terminar")

#Verificar si se ingresaron las notas
if len(notas) == 0:
    print("No se ingresaron notas")
else:
    promedio = sum(notas) / len(notas)
    print("Promedio de notas", promedio)
    if promedio >= 7:
        print("El estudiante aprobó")
    else:
        print("El estudiante desaprobo")
