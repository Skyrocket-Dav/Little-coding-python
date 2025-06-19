def crear_listado():
    listado=[]
    numero=[]
    return listado, numero
def menu():
    print("\n ----MENU----")
    print("1. Mostrar la agenda")
    print("2. Nuevo contacto")
    print("3. Actualizacion de contacto")
    print("4. Eliminar contacto")
    print("5. Cantidad")
    print("6. Salir")
    op=int(input("\n Ingrese la opcion :  "))
    return op
def mostrar_agenda(listado,numero):
    print("---LISTADO---")
    if len(listado)==0:
        print("No existen contactos en tu agenda")
    else:
        for rep in range(len(listado)):
            print(listado[rep], end="  ")
            print(numero[rep], end="  ")
            print()
def nuevo_contacto(listado,numero):
    respuesta="No"
    while respuesta=="No" or respuesta=="NO" or respuesta=="no":
        nombre=input("Ingrese el nombre del nuevo contacto:   ")
        if nombre in listado:
            nombre_existente=listado.index(nombre)
            nombre=input("El nombre del contacto ya existe, corresponde a", listado[nombre_existente], "con el numero", numero[nombre_existente], "por favor ingrese un nombre diferente:  ")
            respuesta="Si"
        else:
            listado.append(nombre)
            numero_nuevo=int(input("Ingrese el numero de telefono del nuevo contacto: "))
            if numero_nuevo in numero:
                print("Este numero ya existe")
                respuesta="si"
            else:
                respuesta=input("Guardar el nuevo contacto? (si/no):  ")
    if respuesta=="SI" or respuesta=="Si" or respuesta=="si":
        numero.append(numero_nuevo)
    return listado, numero
def actualizacion_contacto(listado, numero):
    numero_actualiza=int(input("Ingrese el numero del contacto a actualizar: "))
    if numero_actualiza not in numero:
        print("El numero ingresado no existe en el listado")
    else:
        indice=numero.index(numero_actualiza)
        numero[indice]=int(input("Ingrese el nuevo numero del contacto:  "))
    print("El numero actualizado de", listado[indice], "tiene ahora el nuevo numero:  ", numero[indice])
    return listado,numero
def eliminar_contacto(listado,numero):
    numero_eliminar=int(input("Ingrese el numero del contacto a eliminar:  "))
    if numero_eliminar not in numero:
        print("No existe el numero que usted desea eliminar.")
    else:
        indice=numero.index(numero_eliminar)
        respuesta=input("Se va a eliminar el contacto con el nombre--"+str(listado[indice]) +str("   con el numero")+str (numero[indice]) +str("         Desea continuar? (si/no):   "))
        if respuesta=="si" or respuesta=="SI" or respuesta=="Si":
            listado.pop(indice)
            numero.pop(indice)
            print("Se ha eliminado el contacto")
        else: 
            print("Se ha cancelado la eliminacion")
    return listado, numero
def cantidad(listado):
    print("En su listado hay un total de", len(listado), "Contactos")

def salir():
    print("Usted a cerrado el programa, gracias por usar el programa")

def main():
    op=0
    listado,numero=crear_listado()
    while op!=6:
        op=menu()
        if op==1:
            mostrar_agenda(listado,numero)
        elif op==2:
            listado,numero=nuevo_contacto(listado,numero)
        elif op==3:
            listado,numero=actualizacion_contacto(listado,numero)
        elif op==4:
            listado,numero=eliminar_contacto(listado,numero)
        elif op==5:
            cantidad(listado)
    salir()
main()    

