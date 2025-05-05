#Calcular el puntaje de credito
#Se debe calcular que tanto credito tiene una persona
#en cierta entidad financiera, debera considerar
#cantidad de ingresos, nivel educaional y nacionalidad
#Cantidad de ingresos:
#500000 a 1000000: 300000
#1.000.000 a 1.500.000: 650.000
#1.500.001 o más:1.000.000
#Nivel educaional
#Basico:x1 medio:x1.3 superior: 1.5
#Nacionalidad
#Chilena:+300000 Extranjero: nada

# credito=0

# print("Bienvenido a su simulación de crédito bancario")
# ing= int(input("""Seleccione su rango de ingresos:
#           1.- $500.000 a 1.000.000
#           2.- $1.000.000 a $1.500.000
#           3.- $1.500.000 o más
          
#           """))

# if ing==1:
#     credito+=300000
# elif ing==2:
#     credito+=650000
# elif ing==3:
#     credito+=1000000
# else:
#     print("Ingrese una opción válida")

# ne= int(input("""Seleccione su nivel educacional:
#           1.- Básica
#           2.- Media
#           3.- Superior
          
#           """))
# if ne==1:
#     credito=credito
# elif ne==2:
#     credito=credito*1.3
# elif ne==3:
#     credito=credito*1.5
# else:
#     print("Ingrese una opción válida")

# nacio=int(input("""Seleccione su nacionalidad:
#           1.- Chilena
#           2.- Extranjera
          
#           """))

# if nacio==1:
#     credito+=300000
# elif nacio==2:
#     credito=credito
# else:
#     print("Ingrese una opción válida")


# print(f"Su crédito estimado es: {credito}") #PON CORCHETES Y NO PARENTESIS AWEONAO

#Pedir dia y mes de nacimiento y mostrar signo zodiacal

#Pida al usuario 2 digitos verificando que el segundo sea mayor
#Genere un numeo aleatoreo entre esos sigitos
#e imprima la cantidad de veces el simbolo
# 
# import random
# print("Ingrese dos números") 
# n1=int(input("Ingrese el primer número "))
# n2=int(input("Ingrese otro número "))
# while n1>n2:
#     print("Ingrese otro número que sea mayor que el primero")
#     n2=int(input())
# valorazar=random.randint(n1,n2)
# print("▄"*valorazar)

#crear un programa que pida la cantidad de ramos
#luego pida el promedio por cada materia
#basados en su promedio final, aplicar puntaje de beneficios
#4.5 y 5,0:300, 5,1 y 6.0:500 y 6.1 y 7.0:800
#Agregar puntaje según carrera
#Técnico:+60, ingenieria:+40, diplomado:+20
total=0
cr=int(input("Ingrese la cantidad de ramos "))
for i in range (cr):
    nota=float((input("Ingrese el promedio del ramo ")))
    total+=nota
pf=total/cr
print(f"Su promedio es de",pf)

beneficio=0
if pf>=4.5 and pf<=5.0:
    beneficio+=300
elif pf>=5.1 and pf<=6.0:
    beneficio+=500
elif pf>=6.1 and pf<7.0:
    beneficio+=800

carrera=int(input("""Ingrese su carrera
                  1.-Técnico
                  2.-Ingenieria
                  3.-Diplomado
                  
                  """))
if carrera==1:
    beneficio+=60
elif carrera==2:
    beneficio+=40
elif carrera==3:
    beneficio+=20

print("Su beneficio es de",beneficio)


   