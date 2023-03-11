# ejercicio 1

print("------------------------------")
print("-------plano cartesiano-------")
print("------------------------------")

# input
x = int(input("ingrese el punto en x: "))
y = int(input("ingrese el punto en y: "))

#processing

if ( x == 0):
    if (y == 0):
        print("se encuentra en el origen, en los puntos")
    else:
        print("se cuentra en el eye y")
else:
    if(y == 0):
        print( "se encuentra en el eje x")

    else:
        if(x > 0):
            if(y > 0):
                print( "se encuentra en el primer cuadrante")
            else:
                print("se encuentra en el cuarto cuadrante")
        else:
            if( y > 0):
                print("se encuentra en el segundo cuadrante")
            else:
                print("se encuentra en el tercer cuadrante")
#output