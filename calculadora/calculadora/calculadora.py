from math import log


print("---------------------------")
print("--------CALCULADORA--------")
print("---------------------------")

#INPUT
bandera = False

x = float(input("Dame el valor de el numero x: "))
y = float(input("Dame el valor de el numero y: "))

print("Dame la opcion que deseas realizar: \n")

# Se despliega el menu para colocar la opcion que deseas realizar
print("1. Sumar (El primero mas el segundo)")
print("2. Restar (El primero menos el segundo)")
print("3. Multiplicar (El primero por el segundo)")
print("4. Dividir (El primero sobre el segundo)")
print("5. Potencia (El primero mas el segundo)")
print("6. Logaritmo (El logaritmo del segundo)")

opcion = int(input("\n dame la opción: "))

#PROCESS
if (opcion == 1 ):
    z = x + y
    print(x, "+" ,y )
elif (opcion == 2 ):
    z = x - y
    print(x, "-" ,y )
elif (opcion == 3 ):
    z = x * y
    print(x, "x" ,y )
elif (opcion == 4 and y!= 0 ):
    z = x / y
    print(x, "/" ,y )
elif (opcion == 4 and y==0  ):
    print("El denominador es igual a cero y \n NO SE PUEDE REALIZAR LA DIVISIÓN. " )
    bandera = True
elif (opcion == 5 ):
    z = pow(x,y)
    print(x, "^" ,y )
elif (opcion == 6 and x > 0):
    z = log(x)
    print("Logaritmo de ", x )
elif (opcion ==  bandera <= 0  ):
    print("El valor de x es <= cero y \n NO SE PUEDE CALULAR EL lOGARITMO.")
    bandera= True
else:
    print("Opción no valida. ")

# Se escribe el resultado
if ( opcion < 7 and bandera == False):
    print("Resultado = " , z )

#Fin
