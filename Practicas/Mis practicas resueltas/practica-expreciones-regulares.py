#Ejercicio 1

def caracter_permitido(string):
    listaaz = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lista = list(listaaz)
    palabras = list(string)
    contador = 0
    for c in palabras:
        if c in lista:
            contador += 1
    if contador > 0:
        print("La palabra tiene al menos un caracter permitido")
    else:
        print("La palabra no tiene ni un caracter permitido")


#Ejercico 2

def todos_caracter_permitido(string):
    listaaz = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lista = list(listaaz)
    palabras = list(string)
    contador = 0
    for c in palabras:
        if c in lista:
            contador += 1
    if contador == len(string):
        print("La palabra tiene todos sus caracteres permitidos")
    else:
        print("La palabra no tiene todos sus caracteres permitidos")


#Ejercicio 3
def hseguguidadee(string):
    import re
    re.search("h", string)


#Ejercicio 4

def palabra_con_guion(string):
    import re
    print(bool(re.search("_", string)))


#Ejercicio 5

def empieza_con_numero(string, numero):
    import re
    print(bool(re.search("^"+str(numero), string)))


#Ejercicio 6

def strings_en_frase(listadestrings,  frase):
    import re
    contador = 0
    for string in listadestrings:
        if re.search(string, frase):
            contador += 1
    print(contador > 0)


#Ejercicio 7

def Stringsoloconcaracterespermitidos(archivo):
    import re
    with open(archivo, "r") as f:
        lineas = f.readlines()
        palabras = lineas.split()
        for palabra in palabras:
            if re.search("^[a-zA-Z0-9_]+$", palabra):
                print(palabra)