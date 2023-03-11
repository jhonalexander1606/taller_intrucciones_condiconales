# ejercicio_2

print("--------------------------------")
print("-----------PRESTAMO-------------")
print("--------------------------------")

#input

Di = int(input("inserte el valor de sus ingresos: "))
De = int(input("inserte el valor de su deuda (si no tiene digite 0): "))


#processing

if (Di > 945200):
    if (De > 0):
        print("prestamo denegado por motivo de deudas")

    else:
        if (De == 0):
            print("prestamo concecido")
        else:
            print("prestamo denegado por motivo de deudas")
else:
    print("prestamos denegado por motivo de insuficiencia de ingresos")