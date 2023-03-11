#ejercicio_3

print("----------------------------")
print("-----------PRECIO-----------")
print("----------------------------")

#input

c = int(input("ingrese el costo del articulo: "))

#processing

if c < 3000:
    g = (15*c)/100
    rta = (f"la ganancia es ")

else:
    if 3000 >= c <= 6000:
        g = 500
    else:
        g = (25*c)/100

#processing

p = c + g
    
print("el precio de venta del articulo es de:" , p,)    

 
