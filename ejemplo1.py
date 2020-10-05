#ingresar 2 numeros, mostrar la suma y la umtiplicacion de ambos

a=int(input("Digite un numero: "))
b=int(input("Digite otro numero: "))
suma=a+b
multi=a*b
print("La suma de " + str(a) + "y de" +  str(b) + "es igual a: " + str(suma))
print("La multiplicacion de " + str(a) + "y de" +  str(b) + "es igual a: " + str(multi))
#estructura if
if(a>b):
    print("El numero " + str(a) + "Es mayor que: " + str(b))
elif (a<bool):
    print("El numero " + str(a) + "Es menor que: " + str(b))
else:
    print("Los numeros son iguales!")
