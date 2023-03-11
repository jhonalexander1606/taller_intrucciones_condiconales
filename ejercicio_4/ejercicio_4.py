# ejercicio 4
print("------------------------------------")
print("---------------IMC------------------")
print("------------------------------------")

#input

Pe = int(input("ingrese su peso en kilogramos: "))
Al = float(input("ingrese su altura en metros: "))

#processing
IMC = Pe / Al**2

if IMC<16:
    print("Criterio de ingreso al hospital")
else:
    if 16<=IMC<17:
        print("infrapeso")
    else:
        if 17<=IMC<18:
            print("Bajo peso")
        else:
            if 18<=IMC<25:
                print("peso normal (saludable)")
            else:
                if 25<=IMC<30:
                    print("Sobrepeso (obesidad grado I)")
                else:
                    if 30<=IMC<35:
                        print("Sobrepeso cronico (obesidad grado II)")
                    else:
                        if 35<=IMC<40:
                            print("Obesidad premorbida (obesidad grado III)")
                        else:
                            print("Obesidad morbida (obesidad de grado IV)")