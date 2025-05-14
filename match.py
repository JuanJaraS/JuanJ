#case _: Es para todas los opciones no válidas

#Crear un menu de carrito con las siguientes opciones
#1.-Ingresar nombre del usuario
#Sera mostrado en la boleta, con un saludo
#2.- Comprar, poner los productos para poder comprar con su precio correspondiente
#3.- Sacar Boleta, calcula el precio neto y el precio mas IVA. Mostrar totales
#4.-Salir
#Consideraciones:
#Por lo menos 3 productos
#No hay limite de compra
#Se puede salir en cualquier momento
#Los montos de los productos son fijos



def nombre():
    nom = input("Ingrese su nombre ")
    print(f"¡Bienvenido {nom}!")

def menú():
    global total
    print(""" Seleccione su producto
          1.-Jabón $1000
          2.-Shampoo $2500
          3.-Pasta de dientes $2000
          4.-Salir
          """)
    
    op = int(input())
    while True:
        match op:
            case 1:
                total = total + 1000
                print(f"Su total parcial es ${total}")
            case 2:
                total = total + 2500
                print(f"Su total parcial es ${total}")
            case 3:
                total = total + 2000
                print(f"Su total parcial es ${total}")
            case 4:
                break
            case _:
                print("Opción no válida")
        print(""" Seleccione su producto
          1.-Jabón $1000
          2.-Shampoo $2500
          3.-Pasta de dientes $2000
          4.-Salir al menú principal
          """)
        op = int(input())  

def boleta():
    global total
    print(f"El valor neto de sus productos hasta ahora es ${total}")
    print(f"El valor con IVA de sus productos hasta ahora es ${total * 1.19}")




total = 0  
while True:
    op = int(input("""Seleccione una opción:
          1.-Ingresar Nombre
          2.-Menú productos
          3.-Boleta
          4.-Salir
          """))
    match op:
        case 1:
            nombre()
        case 2:
            menú()
        case 3:
            boleta()
        case 4:
            print("¡Muchas gracias por su compra!")
            break
        case _:
            print("Opción no válida")

      
