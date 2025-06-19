ahorro=0
def menu():

    print(" opciones")
    print("1. Aumentar ahorro")
    print("2. Disminuir ahorro")
    print("3. Consultar ahorro")
    print("4.Terminar programa")
    opcion=int(input("ingrese su opcion (Ingrese solo el numero):"))
    while opcion<1 or opcion>4:
        print("Su opcion es invalida introduzcalo de nuevo")
        opcion=int(input())
    return opcion


def incrementar_ahorro(ahorro):

    aumento_ahorro=int(input("Introduzca el valor  a incrementar del ahorro. (min $100 pesos):"))
    while aumento_ahorro<100:
        print("Valor incorrecto introduza de nuevo el valor")
        aumento_ahorro=int(input())
    ahorro+=aumento_ahorro
    print("Con el aumento su ahorro queda con valor de $", ahorro)
    return ahorro
def reducir_ahorro(ahorro):
    disminucion_ahorro=int(input("Introduzca el valor de la disminucion "))
    while disminucion_ahorro>ahorro/2:
        print("Usuario, usted esta solictando un valor mayor a la mitad de su ahorro, esto no es posible,pir favor introduzca de nuevo el valor de la disminucion")
        disminucion_ahorro=int(input())
    while disminucion_ahorro<100: 
        print("Usted esta retirando un valor que es menor a $100 pesos, por favor introduzca de nuevo el valor")
        disminucion_ahorro=int(input())
    ahorro-=disminucion_ahorro
    print("Con el valor disminuido, su ahorro queda en $", ahorro)
    return ahorro

def consultar_ahorro(ahorro):
    print(ahorro)

def terminar():
    print("Gracias por usar el programa")




def main():
    opcion=menu()
    ahorro=0
    while opcion!=4:
        if opcion==1:
            ahorro=incrementar_ahorro(ahorro)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==2:
            ahorro=reducir_ahorro(ahorro)            
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==3:
            consultar_ahorro(ahorro)
            opcion=int(input("Introduzca su nueva opcion:"))
    if opcion==4:
        terminar()
main()