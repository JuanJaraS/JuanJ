# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostrar nota
# 4.- Sacar promedio, nota mayor y nota menor 
# 5.- Limpiar toda las notas
# 6.- Salir


# def menú():
#     print("""1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostrar nota
# 4.- Sacar promedio, nota mayor y nota menor 
# 5.- Limpiar toda las notas
# 6.- Salir
# """)
# notas=[] 
# while True:
    
#     menú()
#     op=int(input("Elige una opción "))
#     match op:
#         case 1:
#             try:
#                 nota=float(input("Ingresa la nota: "))
#                 if 1<=nota<=7:
#                     notas.append(nota)
#                     print("Nota agregada.")
#                 else:
#                     print("La nota debe estar entre 1 y 7.")
#             except ValueError:
#                 print("Por favor, ingresa un número válido.")
#         case 2:
#             try:
#                 print("Estas son sus notas {notas}")
#                 nota=float(input("Ingresa la nota a borrar: "))
#                 if nota in notas:
#                     notas.remove(nota)
#                     print("Nota eliminada.")
#                 else:
#                     print("Esa nota no está en la lista.")
#             except ValueError:
#                 print("Por favor, ingresa un número válido.")
#         case 3:
#             print("Notas:", notas)
#         case 4:
#             if notas:
#                 promedio= sum(notas)/len(notas)
#                 mayor= max(notas)
#                 menor= min(notas)
#                 print(f"Promedio: {promedio:.2f}")
#                 print(f"Nota mayor: {mayor}")
#                 print(f"Nota menor: {menor}")
#             else:
#                 print("No hay notas para calcular estadísticas.")
#         case 5:
#             notas.clear()
#             print("Todas las notas han sido eliminadas.")
#         case 6:
#             print("Saliendo del programa...")
#             break
#         case _:
#             print("Opción no válida. Intenta de nuevo.")

notas=[4.6, 7.0, 5.6]
#num=indice
#n=elemento como ral
for num, n in enumerate(notas):
    print(num+1,".-",n)
    

            

