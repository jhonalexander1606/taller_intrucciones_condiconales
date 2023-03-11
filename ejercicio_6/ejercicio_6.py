# ejercicio_6
import math
print("--------------------------")
print("----------raices----------")
print("--------------------------")

# input

n1 = int(input("ingrese el valor de n1: "))
n2 = int(input("ingrese el valor de n2: "))
n3 = int(input("ingrese el valor de n3: "))

#procesing 

d = (n2**2)-(4*n1*n3)

if (d == 0):
    x = -n2/2*n1
    print("las raices son: " + str(x))
else:
    if (d<0):
        print("son raices imaginarias")
    else:
        x2 = (-(n2)+(math.sqrt(d)))/(2*n1)
        x1 = (-(n2)-(math.sqrt(d)))/(2*n1)
        print("las raices son: "+" x1: "+ str(x1)+" x2: " + str(x2))