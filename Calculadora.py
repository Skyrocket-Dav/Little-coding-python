def menu():
    print(" opciones")
    print("3. Suma")
    print("4. Resta Normal")
    print("5. Resta invertida")
    print("6. Primo Uno")
    print("7. Primo dos")
    print("8. Divisor Uno")
    print("9. Divisor dos")
    print("10. Terminar")
    opcion=int(input("ingrese su opcion (Ingrese solo el numero):"))
    while opcion<1 or opcion>10:
        print("Su opcion es invalida introduzcalo de nuevo")
        opcion=int(input())
    return opcion
def solictar_primer():
    operando1=int(input("Introduzca el primer operando:"))
    while operando1<0:
        print("Este programa no maneja numeros negativos, por favor introduzca el valor de nuevo")
        operando1=int(input())
    return operando1
def solicitar_segundo():
    operando2=int(input("Introduzca el operando dos:"))
    while operando2<0:
        print("Este programa no maneja numeros negativos, por favor introduzca el valor de nuevo")
    return operando2
def suma(operando1,operando2):
    total=operando1+operando2
    print("La suma del total de los dos operandos es:", total)
def resta_normal(operando1,operando2):
    resta1=operando1+operando2
    print("La resta del primer operando menos el segundo operando es:", resta1)
def resta_invertida(operando1,operando2):
    resta2=operando2-operando1
    print("La resta del segundo operando menos el primer operando es:", resta2)
def primo_uno(operando1):
    if operando1%1==0 or operando1%operando1==0:
        print("El numero SI es primo")
    else:
        print("El numero NO es primo")
def primo_dos(operando2):
    if operando2%1==0 or operando2%operando2==0:
        print("El numero SI es primo")
    else:
        print("El numero NO es primo")
def divisor_uno(operando1, operando2):
    if operando2%operando1==0:
        print("El primer operando es divisor del segundo")
    else:
        print("No es divisor el primer operando del segundo operando")
def divisor_dos(operando1, operando2):
    if operando1%operando2==0:
        print("El segundo operando es divisor del primero")
    else:
        print("No es divisor el segundo operando del primer operando")
def terminar():
    print("Gracias por usar el programa")
def main():
    operando1=solictar_primer()
    operando2=solicitar_segundo()
    opcion=menu()
    while opcion!=10:
        if opcion==3:
            suma(operando1,operando2)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==4:
            resta_normal(operando1, operando2)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==5:
            resta_invertida(operando1, operando2)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==6:
            primo_uno(operando1)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==7:
            primo_dos(operando2)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==8:
            divisor_uno(operando1,operando2)
            opcion=int(input("Introduzca su nueva opcion:"))
        elif opcion==9:
            divisor_dos(operando1,operando2)
            opcion=int(input("Introduzca su nueva opcion:"))
    if opcion==10:
        terminar()
main()
