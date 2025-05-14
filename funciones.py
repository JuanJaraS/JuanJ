#Funciones
# def suma():
#     n1=int(input("Ingrese un número "))
#     n2=int(input("Ingrese otro número "))
#     print("La suma es", n1+n2)
# def resta():
#     n1=int(input("Ingrese un número "))
#     n2=int(input("Ingrese otro número "))
#     print("La resta es", n1-n2)
# def div():
#     try:
#             n1 = int(input("Ingrese un número "))
#             n2 = int(input("Ingrese otro número "))
#             print("La división es", n1 / n2)
#     except ZeroDivisionError:
#         print("Error: No se puede dividir entre cero.")
# def mult():
#         n1=int(input("Ingrese un número "))
#         n2=int(input("Ingrese otro número "))
#         print("La multiplicación es", n1*n2)
# def calcu():
#     op=int(input("""Seleccione una operación 
#                 1.- Suma
#                 2.- Resta
#                 3.- División
#                 4.- Multiplicación
#                 5.- Salir
#                 """))
#     while True:
#         match op:
#             case 1:
#                 suma()
#             case 2:
#                 resta()
#             case 3:
#                 div()
#             case 4:
#                 mult()
#             case 5:
#                 print("Saliendo")
#                 break
#         op=int(input("""Seleccione una operación 
#                 1.- Suma
#                 2.- Resta
#                 3.- División
#                 4.- Multiplicación
#                 5.- Salir
#                 """))
# calcu()  
# Errores comunes  
# ValueError	Cuando un valor tiene el tipo correcto pero un contenido inválido. Ej: int("abc")
# TypeError	Cuando usas un tipo de dato incorrectamente. Ej: "5" + 2
# ZeroDivisionError	Cuando intentas dividir entre cero. Ej: 5 / 0
# IndexError	Cuando accedes a una posición inválida de una lista. Ej: lista[100]
# KeyError	Cuando accedes a una clave inexistente en un diccionario. Ej: dict["clave"]
# NameError	Cuando usas una variable que no ha sido definida. Ej: print(x) sin definir x
# AttributeError	Cuando llamas un atributo o método que no existe. Ej: "hola".append()
# FileNotFoundError	Cuando intentas abrir un archivo que no existe. Ej: open("no_existe.txt")
# ImportError	Cuando falla la importación de un módulo. Ej: import modulo_que_no_existe
# IndentationError	Cuando la indentación es incorrecta en el código.
# SyntaxError	Cuando hay un error de sintaxis en el código Python.
        

