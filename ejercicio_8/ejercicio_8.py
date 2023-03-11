# ejercicio_8

print("---------------------------------------")
print("----------multiplos entre dos----------")
print("---------------------------------------")

# input

n1=int(input("inserte el numero 1: "))
n2=int(input("inserte el numero 2: "))

# procesing

c= n1%n2
if c == 0:
    d=n2%n1
    if d == 0:
        #output
        print(f"{n1} es igual a {n2}")
    else:
        #output
        print(f"{n1} es multiplo de {n2}")
else:
    d=n2%n1
    if d == 0:
        #output
        print(f"{n2} es multiplo de {n1}")
    else:
        #output
        print(f"{n1} y {n2} no son multiplos")