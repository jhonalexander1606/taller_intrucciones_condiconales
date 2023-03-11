# ejercicio_5

print("----------------------")
print("----PRECIO DEL AGUA---")
print("----------------------")

# input 
m = int(input("Ingrese el numero de m3 de agua gastados: "))

# procesing

if (m<50):
    print(f"Su costo es de: {10000}")
else:
    if (50<=m<200):
        print("su costo es de: {2000+10000}")
    else:
        print(f"su costo es de: {3000+10000}")