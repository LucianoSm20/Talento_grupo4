import decimal

number_keys = {
    "unidad_cien_mil" : 0,
    "unidad_diez_mil" : 0,
    "unidad_mil" : 0, 
    "centena" : 0,
    "decena" : 0,
    "unidad" : 0   
    }

def numero_a_diccionario(numero):
    largo = len(str(numero))
    for i in str(numero):
        if largo == 6:
            number_keys['unidad_cien_mil'] = int(i)
        elif largo == 5:
            number_keys['unidad_diez_mil'] = int(i)
        elif largo == 4:
            number_keys['unidad_mil'] = int(i)
        elif largo == 3:
            number_keys['centena'] = int(i)
        elif largo == 2:
            number_keys['decena'] = int(i)
        elif largo == 1:
            number_keys['unidad'] = int(i)
        largo = (largo-1)


def graficar(lista_numeros_ingresados):
    contador = 11
    for i in range(0,12):
        #for j in range(0,6):
        for j in number_keys:
            if(i==0)or(i==11):
                print("   +-+   ", end="")
            elif(((number_keys[j])-contador)==0):
                print("  XXXXX  ", end="")
                number_keys[j]=number_keys[j]-1
            else:
                print("   | |   ", end="")
        contador = contador -1
        print("")
    print(" 100.000   10.000   1.000     100      10        1")

    consulta_fin(lista_numeros_ingresados)

def consulta_fin(lista_numeros_ingresados):
    consulta = str(input("¿Desea seguir jugando? S/N:"))    

    if(consulta.lower() == 'salir' or consulta.lower() == 'n'):
        for i in lista_numeros_ingresados:
            print(i)
        print('fin de la ejecucion')
    elif( consulta.lower() == 's'):
        inicio(lista_numeros_ingresados)
    else:
        print("respuesta invalida, vuelva a intentarlo")
        consulta_fin(lista_numeros_ingresados)
   


def inicio (lista_numeros_ingresados):
    
    num = int(input("Ingrese un numero de hasta 6 digitos: "))

    if len(str(num)) > 6:
        print("el numero excede el largo, intentalo de nuevo")
        inicio(lista_numeros_ingresados)
    else:
        lista_numeros_ingresados.append(num)
        for i in lista_numeros_ingresados:
            print("numero_69:", i)
        numero_a_diccionario(num)
        graficar(lista_numeros_ingresados)


print("bienvenidos")
lista_numeros_ingresados = []
inicio(lista_numeros_ingresados)