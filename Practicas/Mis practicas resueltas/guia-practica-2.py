#ALTERNATIVA CONDICIONAL
#Ejercicio 1

cadena=(input("palabra: "))
if cadena[0] == str.upper(cadena[0]):
    print("Es mayuscula") 
else:
    print("Es minuscula") 


#Ejericicio 2 

def par_o_impar(numero):
    if numero % 2 == 0:
      print("Es par")
    else:
        print ("Es impar")
numero = int(input("Numero: "))
if numero>0:
    print("Es positivo",par_o_impar(numero))
elif numero<0:
    print("Es negativo",par_o_impar(numero))
else:
    print("El numero es 0",par_o_impar(numero))


#Ejercicio 3

def cara_dado(numero):
    if numero==1:
        print("6")
    elif numero==2:
        print("5")
    elif numero ==3:
        print("4")
    elif numero==4:
        print("3")
    elif numero==5:
        print("2")
    elif numero==6:
        print("1")
    else:
        print("Numero ingresado incorrecto")
numero=int(input("Numero: "))
print(cara_dado(numero))


#Ejercicio 4

def costo_translado(zona, peso_gr):
    if peso_gr >= 5000:
        return "No hacemos envios por exceso de peso"
    elif zona==1:
        return peso_gr*10
    elif zona==2:
        return peso_gr*15
    elif zona==3:
        return peso_gr*18
    elif zona==4:
        return peso_gr*24
    elif zona==5:
        return peso_gr*30
zona=int(input("A que zona es:"))
peso_gr=int(input(f"Peso en gramos: "))
print("El costo del translado es de $"+str(costo_translado(zona, peso_gr)))


#Ejercicio 5

semana= ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
numero=int(input("Escribir numero: "))
if 1 <= numero <=7:
    print(semana[numero-1])
else:
    print("El numero ingresado es incorrecto")


#LISTAS

#Ejercicio 6

lista1=[input(), input(), input()]
lista2=lista1.reverse()
print(lista1)


#Ejercicio 7

lista=[]
numero =int(input("Ingrese numero:"))
while numero>=0:
    lista.append(numero)
    numero =int(input("Ingrese numero:"))
if numero<0:
    print(lista)


#Ejercicio 8

lista1=[int(input()), int(input()), int(input()), int(input()), int(input())]
lista2=[int(input()), int(input()), int(input()), int(input()), int(input())]
lista3=[lista1[0]+lista2[0], lista1[1]+lista2[1], lista1[2]+lista2[2],lista1[3]+lista2[3],lista1[4]+lista2[4]]
print(lista3)


# Ejercicio 9

lista_nombres = []
lista_edades = []
nombres = input("ingrese nombre:")
if nombres != "*":
    lista_nombres.append(nombres)
    edad = int(input("ingrese edad:"))
    lista_edades.append(edades)
else:
    print("no hay alumnos")
while nombres != "*":
    nombres = input("ingrese nombre:")
if nombres != "*":
    lista_nombres.append(nombres)
edad = int(input("ingrese edad:"))
lista_edades.append(edades)
else:
    edad_maxima = max(lista_edades)
    ubicacion = list.findex(lista_edades, edad_maxima)
    nombre_maximo = lista_nombres[ubicacion]

    print("la edad maxima es: " + str(edad_maxima) + "y corresponde a la de" + str(nombre_maximo))

#DICCIONARIOS

#Ejercicio 10

def letra(string):
    diccionario = {}
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra("Universidad del cema"))

#Ejercicio 11
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
diccionario = {}
for letra in alfabeto + alfabeto.upper():
    diccionario[letra] = 0 
def letra2(string):
    for letra in string:
        if letra not in diccionario:
            diccionario[letra] = 1
        elif letra in diccionario:
            diccionario[letra] += 1
    return diccionario
print(letra2("Gimnasio"))

# Ejercicio 12 

cantidad = int(input("Introducir cantidad de alumnos:"))
alumnos = {}

for num in range(0, cantidad):
    alumno = input("alumno: ")
    notas = []
    nota =int(input("nota: "))

    while nota >= 0:
        notas.append(nota)
        nota= int(input("nota: "))
    alumnos[alumno] = notas

for alumno in alumnos:
    print(alumno, sum(alumnos[alumno])/len(alumnos[alumno]))


#FUNCIONES
#Ejercicio 13

def esMultiplo(numero1, numero2):
    return numero1 % numero2 == 0 or numero2 % numero1 == 0
print(esMultiplo(2, 4))


#Ejercicio 14

def temperatura_media(temp1,temp2):
	return (temp1 + temp2)/2

cantidad=int(input("¿Cuántas temperaturas vas a calcular?:"))
for indice in range(cantidad):
	tmin = float(input("Introduce temperatura mínima:"))
	tmax = float(input("Introduce temperatura máxima:"))
	print("Temperatura media:",temperatura_media(tmin,tmax))


#Ejercicio 15

def cargarSocios(socios):
    numero = int(input("Número de socio: "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso: ")
        cuota = input("¿Cuota al día? s/n: ")
        pago = cuota.lower() == "s"
        socios[numero] = [nombre, fecha, pago]
        numero = int(input("Número de socio: "))
    return socios
def modificarFecha(socios, fechaAnterior, fechaNueva):
    for datos in socios.values():
        if datos[1] == fechaAnterior:datos[1] = fechaNueva
    return socios
def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower() == nombre.lower():
            return numero
            return 0
def formatoFecha(fecha):
    return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]
def imprimirListado(socios):
    for numero,datos in socios.items():
        print("Número: ", numero)
        print("Nombre: ", datos[0])
        print("Fecha de ingreso ", formatoFecha(datos[1]))
        if datos[2]:
            print("Cuota al día")
        else:
            print("En deuda")
            print("---------------")
        return None
    socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}
    print("Cargar socios")
    socios_activos = cargarSocios(socios_activos)
    print("El club tiene", len(socios_activos), "socios")
    print("Registrar pago de cuotas")
    numero = int(input("Numero de socio: "))
    socios_activos[numero][2] = True 
    print("Modificando fecha de ingreso...")
    socios_activos = modificarFecha(socios_activos, "21102017", "22102017")
    print("Eliminar socio:")
    nombre = input("Nombre y apellido: ")
    numero = numeroSocio(socios_activos, nombre)
    del socios_activos[numero]
    imprimirListado(socios_activos)