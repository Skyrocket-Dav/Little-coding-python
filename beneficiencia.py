
def inicio_administrador(contrasena_administrador, usuario_administrador):
    intentos_nombre=3
    intentos_contrasena=3
    print("\t INICIO DEL PROGRAMA")
    print("\t ADMINISTRADOR")
    nombre_administrador=input("Ingrese su primer nombre (En mayusculas):    " )
    while nombre_administrador not in usuario_administrador and intentos_nombre>0:
        intentos_nombre=intentos_nombre-1
        print("Le quedan", intentos_nombre, "intentos")
        nombre_administrador=input("Nombre incorrecto, ingrese de nuevo el nombre (En mayusculas):  ")
    if intentos_nombre==0:
        print("Los nombres que usted utilizo no estan registrados como administrador, Gracias por usar el programa")
    else: 
        contrasena=int(input("Ingrese la contraseña del administrador:   "))
        while contrasena!=contrasena_administrador:
            intentos_contrasena=intentos_contrasena-1
            contrasena=int(input("Contraseña incorrecta, le quedan "+str(intentos_contrasena) +str("intentos") +str(" Ingrese de nuevo la contraseña:   ")))
        if contrasena==contrasena_administrador:
            print("Este programa se crea para dar empleos a personas que lo necesiten basandonos en su nivel academico y experiencia laboral")
            numero_trabajos=int(input("Ingrese la cantidad de tipos de trabajos que usted va a crear:  "))
            while numero_trabajos <=0 :
                numero_trabajos=int(input("Inválido, ingresa un número positivo:   "))
            trabajos=[0]*numero_trabajos
            cantidad_cupos=[0]*numero_trabajos
            for rep in range(len(trabajos)):
                trabajos[rep]=input("Ingrese el nombre del Trabajo #"+str(rep+1)+str(" "))
            print("\n Ahora usted va a ingresar la cantidad de cupos para cada trabajo")
            respuesta=input("usted desea dar un valor de cupos fijo para todos los trabajos? (SI/NO):   ")
            if respuesta=="Si" or respuesta=="SI" or respuesta=="si":
                cantidad_fija=int(input("Que cantidad le va a asignar a TODOS los empleos:    "))
                can=0
                for can in range(len(cantidad_cupos)):
                    cantidad_cupos[can]=cantidad_fija
            else:
                posicion=0
                for posicion in range(len(cantidad_cupos)):
                    print("Ingrese la cantidad de cupos que desea agregar al trabajo de", trabajos[posicion])
                    cantidad_cupos[posicion]=int(input("\n Ingrese la cantidad a agregar:   "))
    return cantidad_cupos, trabajos, numero_trabajos


def menu():
    print("\t BIENVENIDO")
    print("\n----MENU----")
    print("1. Administrador")
    print("2. Registro inicial (Candidatos)")
    print("3. Beneficiario (Usuarios registrados)")
    print("4. Terminar")
    opcion=int(input("Seleccione una opcion:    "))
    while opcion<1 and opcion>3:
        opcion=int(input("Ingreso un dato incorrecto por favor seleccione una nueva opcion:   "))
    return opcion 
def datos_y_variables():
    usuario_administrador=[""]*2
    usuario_administrador[0]="JUAN"
    usuario_administrador[1]="SARA"
    contrasena_administrador=12345 #Contraseña para los administradores 
    return usuario_administrador, contrasena_administrador

def admin(contrasena_administrador, usuario_administrador,nombre_beneficiario, poblacion, interesados, cantidad_cupos, trabajos, nombre_trabajo, numero_trabajos):
    nombre_beneficiario=0
    poblacion= interesados=0
    cantidad_cupos=0
    trabajos=0
    nombre_trabajo=0
    nombre=input("Ingrese su nombre:  ")
    intentos_nombre=3
    intentos_contrasena=3
    nombre_administrador=input("Ingrese su primer nombre (En mayusculas):    " )
    while nombre not in usuario_administrador and intentos_nombre>0:
        intentos_nombre=intentos_nombre-1
        print("Le quedan", intentos_nombre, "intentos")
        nombre=input("Nombre incorrecto, ingrese de nuevo el nombre (En mayusculas):  ")
    if intentos_nombre==0:
        print("Los nombres que usted utilizo no estan registrados como administrador, Gracias por usar el programa")
    else: 
        contrasena=int(input("Ingrese la contraseña del administrador:   "))
        while contrasena!=contrasena_administrador:
            intentos_contrasena=intentos_contrasena-1
            contrasena=int(input("Contraseña incorrecta, le quedan "+str(intentos_contrasena)+str(" Ingrese de nuevo la contraseña:   ")))
        if contrasena==contrasena_administrador:
            print("\t RESULTADOS DE LA CAMPAÑA")
            print(" -Interesados (personas que no lograron pasar por falta de puntaje o cupos)-")
            print(" no existe ningun interesado o beneficiario aun, espere a que se registre alguna persona al puesto  ")
            menu()
            for inter in range (numero_trabajos):
                print(interesados[inter], end=" ")
                print()
            print(" -Beneficiarios-")
            for rep in range(len(nombre_beneficiario)):
                print(nombre_beneficiario[rep], end="  ")
                print(nombre_trabajo[rep], end="  ")
                print()
            print("\n \t RESULTADOS GENERALES")
            print("Total de personas beneficiadas ", len(nombre_beneficiario) )
            print("Total de cupos disponibles")
            for rc in range(len(cantidad_cupos)):
                print(cantidad_cupos[rc], end=" ")
                print(trabajos[rc], end=" ")
                print()
            print("\t POBLACIONES")
            print("1-Pobreza extrema: ", poblacion[0])
            print("2-Pobreza moderada: ", poblacion[1])
            print("3-Vulnerable: ",poblacion[2] )
            print("4-No vulnerable: ", poblacion[3])
            valor_mayor=max(poblacion)
            indice=poblacion.index(valor_mayor)
            print("La poblacion con mayor numero de beneficiados y/o interesados fue la #: ", poblacion[indice], "con un total de ", valor_mayor , "beneficiados")

def registro_iniciaL(cantidad_cupos, trabajos):
    interesados=[]
    puntaje=0
    nombre_beneficiario=[]
    identificacion=[]
    poblacion=[0]*4
    nombre_trabajo=[]
    print("\t TRABAJOS DISPONIBLES")
    cont=1
    for rep in range(len(trabajos)):
        print("#", cont,"  ",trabajos[rep], end="  ")
        print("")
        cont=cont+1
    opcion_trabajo=input("Ingrese el nombre del trabajo al cual va a aplicar (Por favor sea exacto):  ")
    while opcion_trabajo not in trabajos:
        print("Opcion invalida")
        opcion_trabajo=input("Ingrese el nombre del trabajo al cual va a aplicar (Por favor sea exacto):  ")
    indice_trabajo=trabajos.index(opcion_trabajo)
    nombre=input("ingrese su nombre completo (Nombres y apellidos) : ")
    identificacion_numero=int(input("ingrese su numero tarjeta de cedula : "))
    edad= int(input("ingrese su edad : "))
    while edad<0 or edad>100:
        print("Edad invalida")
        edad= int(input("ingrese su edad : "))
    if edad < 18 :
        print("Usted es menor de edad por lo tanto no se puede inscribir a este programa:  ")
    else:
        print("\t TIPOS DE POBLACIONES \n 1. Pobreza Extrema \n 2. Pobreza moderada \n 3. Vulnerable \n 4. No vulnerable")
        poblacion_Seleccion=int(input("seleccione a la poblacion a la que pertenece (Solo el numero): "))
        while poblacion_Seleccion<1 or poblacion_Seleccion>4:
            print("opcion invalida intentelo nuevamente")
            poblacion_Seleccion=input("seleccione a la poblacion a la que pertenece (Solo el numero): ")
        if poblacion_Seleccion == 1:
            puntaje=puntaje + 200
            poblacion[0]=poblacion[0]+1
        elif poblacion_Seleccion == 2:
            puntaje = puntaje + 150
            poblacion[1]=poblacion[1]+1
        elif poblacion_Seleccion== 3 : 
            puntaje = puntaje + 100
            poblacion[2]=poblacion[2]+1
        elif poblacion_Seleccion== 4 :
                puntaje= puntaje + 50
                poblacion[3]=poblacion[3]+1
        nivel_educativo=int(input("seleccione su nivel de educación \n 1.media basica\n 2.tecnico \n 3.tecnologo \n 4.pregrado \n Ingrese solo el numero: "))
        while nivel_educativo<1 or nivel_educativo>4:
                print("opcion invalida intentelo nuevamente")
                nivel_educativo=int(input("seleccione su nivel de educación: (media basica/tecnico/tecnologo/pregrado) : "))
        if nivel_educativo == 1:
            puntaje=puntaje + 50
        elif nivel_educativo == 2:
            puntaje = puntaje + 100
        elif nivel_educativo == 3 : 
            puntaje = puntaje + 150
        elif nivel_educativo == 4 :
            puntaje= puntaje + 200
        estado_civil=int(input("Selecione el estado civil en el que se encuentra con el numero \n1. solter@ \n 2. casad@ \n 3. viud@) \n Ingrese solo el numero: "))
    while estado_civil > 3 or estado_civil < 0:
        print("opcion invalida intentelo nuevamente")
        estado_civil=int(input("Selecione el estado civil en el que se encuentra (soltero,casado,viudo) : "))
    idioma=input("¿Tiene dominio de alguno de los siguientes idiomas? \n Ingles \n Frances \n Portugues (si/no):  ")
    if  idioma == "si" or idioma=="SI" or idioma=="Si":
        puntaje = puntaje + 100
    elif idioma == "no" or idioma=="NO" or idioma=="No" : 
            puntaje=puntaje + 50
    experiencia_laboral=input("Tiene experiencia en  este trabajo ? (si/no) :")
    if experiencia_laboral == "si"or experiencia_laboral=="SI" or experiencia_laboral=="Si": 
        puntaje= puntaje + 200
    elif experiencia_laboral == "no" or experiencia_laboral=="NO" or experiencia_laboral=="No" :
        puntaje=puntaje + 50
    print(puntaje)
    if puntaje < 300 :
        print("Lo sentimos no tiene el puntaje necesario para el puesto , por lo que no obtendra en beneficio")
        interesados.append(nombre)
    elif cantidad_cupos[indice_trabajo]==0:
        print("Lo sentimos no hay mas cupos disponibles")
        interesados.append(nombre)
    elif puntaje > 300 and cantidad_cupos[indice_trabajo]>0:
        print("felicidades",nombre,"con este puntaje a sido beneficiado para obtener el puesto de secretario(a) ")
        cantidad_cupos[indice_trabajo]=cantidad_cupos[indice_trabajo]-1
    nombre_trabajo.append(opcion_trabajo)
    nombre_beneficiario.append(nombre)
    identificacion.append(identificacion_numero)

    return nombre_beneficiario, identificacion, interesados, poblacion, nombre_trabajo
    
def beneficiarios(identificacion, nombre_beneficiario,nombre_trabajo):
    nombre=input("Ingrese su nombre completo (Tal cual como lo ingreso en el registro):    ")
    if nombre not in nombre_beneficiario:
            print("Usted no se encuentra registrado en nuestro sistema")
    else:
        cont=3
        indice=nombre_beneficiario.index(nombre)
        contras=int(input("Por favor ingrese su contraseña (Su identificacion):   "))
        while contras!=identificacion[indice] and cont!=0:
            print("CONTRASEÑA INCORRECTA")
            print('Le quedan', cont, "intentos")
            contras=input("Ingrese su contraseña de nuevo:  ")
            cont-=1
        if cont==0: 
            print("Ya gasto todos los intentos, si usted es el titular de la cuenta por favor comuniquese con el banco")
        if contras==identificacion[indice]:
            respuesta_1=input("1. Debes comunicarte con nosotros para empezar a ser beneficiario, ¿Ya lo hiciste? (Si/No): ")
            if respuesta_1=="Si" or respuesta_1=="SI" or respuesta_1=="si":
                print("EXCELENTE!!!!")
                respuesta_2=input("El siguiente paso es entregar su hoja de vida, ¿Ya la entrego? (SI/NO): ")
                if respuesta_2=="Si" or respuesta_2=="SI" or respuesta_2=="si":
                    print("EXCELENTE")
                    respuesta_3=input("Ahora presentara una entrevista (SI/NO): ")
                    if respuesta_3=="Si" or respuesta_3=="SI" or respuesta_3=="si":
                        print("EXCELENTE")
                        respuesta_4=input("Ahora usted sera notificado ¿Usted ya fue notificado? (SI/NO):  ")
                        if respuesta_4=="Si" or respuesta_4=="SI" or respuesta_4=="si":
                            print("Usted ya tiene el trabajo de", nombre_trabajo[indice])
            else:
                print("Por favor siga con lo que se le esta solicitando")

def main():
    usuario_administrador, contrasena_administrador=datos_y_variables()
    cantidad_cupos, trabajos, numero_trabajos=inicio_administrador(contrasena_administrador, usuario_administrador)
    opcion=0
    while opcion!=4:
        opcion=menu()
        if opcion==1:
            nombre_beneficiario=0
            poblacion= interesados=0
            cantidad_cupos=0
            trabajos=0
            nombre_trabajo=0
            nombre_beneficiario, poblacion, interesados, cantidad_cupos, trabajos, nombre_trabajo=admin(contrasena_administrador, usuario_administrador,nombre_beneficiario, poblacion, interesados, cantidad_cupos, trabajos, nombre_trabajo)
        elif opcion==2:
            nombre_beneficiario, identificacion, interesados, poblacion, nombre_trabajo=registro_iniciaL(cantidad_cupos, trabajos)
        elif opcion==3:
            beneficiarios(identificacion, nombre_beneficiario,nombre_trabajo)
    print("Gracias por usar el programa")
main()
