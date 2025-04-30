
comuna=int(input("""Ingrese su comuna
#                  1.-La Florida
#                  2.-La Pintana
#                  3.-Puente Alto
#                  4.-San Joaquín
#                  """))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("Opción Inválida")

familia=int(input("Ingrese su grupo familiar(número entero )"))

if familia==1:
    descuento+=2
elif familia>=2 or familia<=4:
    descuento+=3
elif familia>=5:
    descuento+=4
else:
    print("Opción Inválida")

print("El total del descuesto es ", descuento)
dc=descuento/100*200000
apagar=200000-dc

print("Su total con el descuento aplicado es",apagar)
#Clasificar segun categoria y precio
#Cat 1 +200, cat 2 +400, cat 3 +600
#Precios:1000 y menos;3%, entre 1001 y 5000;5%, 5001 y mas 6%
#Poner listado de 3 productos por categoria, las cat son 1, 2 y 3
#Agregar los impuestos al precio segun la cat y luego aplicar descuento al total de la boleta segun el monto 