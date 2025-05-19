#otros ejercicios for

#Perros de caza
#Pida al usuario la cantidad de perros
#Muestre cual es la cueta minima de conojer
#Luego consulte cuantos conejos trajo
#Si el perro trajo la cantidad minima cumplio la cueta si no, se queda sin filete
#Mostrar resumen de perros que cumplieron y los que no
# while True:
#     try:
#         cantp=int(input("Ingrese un número de perros "))
#         break
#     except ValueError:
#         print("Ingrese un número válido de perros (número entero) ")

# cuota=5
# pv=0
# pw=0

# for i in range(cantp):
#     try:
#         conejos=int(input(F"Cuántos conejos cazó el perro {i+1} "))
#         if conejos>=cuota:
#             print("Su perro cumplió con la cuota minima")
#             pv+=1
#         else:
#             print("Su perro es un inutil")
#             pw+=1
#     except ValueError:
#         conejos=int(input(f"Ingrese número válido de conejos para el perro {i+1} (número entero) "))

# print(f"La cantidad de perros que complieron con la cuota es de {pv}, los perros inutiles son {pw}")

#Quiere pasar el ramo?
#Pregunte la cantidad de rojos en el curso
#Los talleres qye hay en el semestre son 4
#Por cada taller asistido se obtiene 0.3 decimas
#Si el alumno tiene mas de un punto tiene la bendicion del profesor
#Si no no se le puede ayudar
#Ingrese la nota final y sume las decimas acumuladas
#Muestre si repruebe o no

# while True:
#     try:
#         rojos=int(input("Ingrese la cantidad de rojos en el curso "))
#         break
#     except ValueError:
#         print("Solo se aceptan números enteros")

# for i in range(rojos):
#     try:
#         talleres = int(input("¿A cuántos talleres ha asistido? "))
#         if talleres>4:
#             print("Solo son 4, por mentiroso 0 décimas")
#             decimas=0
#         else:
#             decimas=0.3*talleres
#     except ValueError:
#         print("Por favor, ingrese un número entero válido para los talleres.")
    
#     if decimas>1:
#         print(f"Tienes la bendición del profesor además de {decimas} décimas")
#     else:
#         print(f"Tienes {decimas} décimas")
    
#     while True:
#         try:
#             nf=float(input("Ingrese su promedio: "))
#             break  
#         except ValueError:
#             print("Por favor, ingrese un número válido para el promedio.")

#     nd=nf+decimas
#     nd=min(nd,7.0)
#     if nd>=4.0:
#         print(f"Usted ha aprobado pues su promedio es {nd}")
#     else:
#         print(f"Usted ha reprobado pues su promedio es {nd}")

#Lvado de autos
#Crear un menú para lavar autos

#2.- Cursar Pago del lavo
#3.- Ver ventas diarias
#4.- Salir
#El lavado tiene 3 niveles
#1.-Full $15000, 2.-Standar 10000, 3.-Básico 7000
#Al mostrar las ventas diarias, debe mostrar la cantidad de autos que han ingresado y el monto total
#Tambien debe mostrar el monto total más pagado



total=0
autos=0
mayorpago=0  

def lavado():
    global total
    global autos
    global mayorpago
    while True:
        print('''Menú de lavado:
              1.- Full $15000
              2.- Standar $10000
              3.- Básico $7000
              4.- Salir
              ''')
        op=int(input("Selecciona una opción: "))

        match op:
            case 1:
                total+=15000
                autos+=1
                mayor_pago=max(mayorpago, 15000)
            case 2:
                total+=10000
                autos+=1
                mayor_pago=max(mayorpago, 10000)
            case 3:
                total+=7000
                autos+=1
                mayor_pago=max(mayorpago, 7000)
            case 4:
                print("Saliendo del menú de lavado.")
                print('''Menú principal:
                    1.- Menú de lavado
                    2.- Ver ventas diarias
                    3.- Salir
                    ''')
                break
            case _:
                print("Opción no válida. Por favor selecciona una opción entre 1 y 4.")
        
        if op==1 or op==2 or op==3:  
            print("Lavado realizado correctamente. Selecciona otra opción o sal de este menú.")

def ventas():
    print(f"Las ventas totales del día son ${total}")
    print(f"La cantidad de autos lavados hoy es {autos}")
    print(f"El monto total más alto pagado por un lavado es ${mayor_pago}")

print('''Menú principal:
        1.- Menú de lavado
        2.- Ver ventas diarias
        3.- Salir
        ''')

while True:
    op2=int(input("Selecciona una opción: "))

    match op2:
        case 1:
            lavado()
        case 2:
            ventas()
        case 3:
            print("Saliendo del sistema.")
            break
        case _:
            print("Opción no válida. Por favor selecciona una opción entre 1, 2 y 3.")

