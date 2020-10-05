#crear menu con 3 opciones: 1. numeros, 2. personas, 3. Finalizar
import os
def Numeros():
    #ingresar n numeros donde n es un numero ingresado por el usuario.
    #mostrar la cantidad de numero positivos, cantidad de numero negativos y cantidad
    #de numeros iguales a 0
    n=int(input("ingrese cuantos numeros necesita: "))
    a=0
    b=0
    c=0
    d=0
    for i in range(n):
    
        a=int(input("ingrese un numero: "))
        if(a>0):
       	    b=b+1
        elif(a==0):
       	    c=c+1
        elif(a<0):
            d=d+1
    print("positivos: "+ str(b)+ " negativos: "+ str(d)+ " cero: "+ str(c))
    pausa=input("Presione una teclapara continuar... ")


def Personas():
    #ingresar nombre y edad para n personas. N es un numero ingresado por teclado.
    #mostrar: promedio de todas las edades ingresadas
    n=int(input("ingrese numero de personas: "))
    a=0
    sum=0
    for i in range(n):
        nom=input("ingrese nombre de la persona: ")
        a=int(input("ingrese  edad de la persona: "))
        sum=sum+a

    print("promedio de las edades: " + str(sum/n))
    pausa=input("Presione una teclapara continuar... ")



seguir = True 
while(seguir):
    os.system('cls')
    print(" ---- Menu Principal ---- ")
    print("1. Numeros")
    print("2. Personas")
    print("3. Finalizar")
    op=int(input("Digite opción 1,2,3: "))
    if (op == 1):
        Numeros() #invocamos a un def
    if (op==2):
        Personas() #invocamos un def
    if (op==3):
        print("Programa Finalizado")
        seguir=False
        break