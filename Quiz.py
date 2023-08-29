#1. Escriba un programa que almacene (Input) en una Lista las materias
#que has cursado con sus respectivas notas
#Luego muestre la lista por consola mediante un ciclo.
import os
os.system("cls")


print(" MATERIAS CURSADAS ")
print()

Materias_notas = []

Numero_de_cursos_vistos = int(input(" Ingrese la cantidad de materias que ha cursado: "))

for i in range(Numero_de_cursos_vistos):
    Curso_visto = input(f" Ingrese el nombre de la materia cursada {i + 1}: ")
    nota = float(input(f" Ingrese la nota obtenida del {Curso_visto}: "))
    Materias_notas.append((Curso_visto, nota))

print("\ncursos vistos y notas: ")

for curso_visto, nota in Materias_notas:
    print(f"Curso: {curso_visto}, nota: {nota}")


#Escriba un programa que almacene personas (input), luego que le muestre 
#por pantalla el mensaje de ‘Su nombre es ‘nombre'

personas = []

num_personas = int(input(" Digite el numero de personas que desea almacenar: "))

for i in range(num_personas):
    nombre = input(f" ingrese el nombre de la persona {i + 1}: ")
    personas.append(nombre)

print("\nNombres de las personas son: ")
for nombre in personas:
    print(f" Su nombre es {nombre}")


#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. 
# Luego muestre en consola el 
#símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si 
# esa divisa no se encuentra en el diccionario.


