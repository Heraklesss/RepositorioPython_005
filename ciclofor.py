#crear un ciclo for que permita ingresar para n numeros, donde n es un numero ingresado x teclado.
#calcular y mostrar: cantidad de numero pares y cantidad de numeros impares.

veces = int (input("Cuantos numeros ingresa?: "))
par=0
impar=0
for x in range(veces):
    nume = int (input("ingrese un numero : "))
    if (nume%2==0):
        par=par+1
    elif(nume%2!=0):
        impar=impar+1
print("La cantidad de numero pares es: " + str(par))
print("La cantidad de numero impares es: " + str(impar))