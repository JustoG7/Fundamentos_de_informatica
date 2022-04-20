#Ejercicio 1

def linea_de_archivo(archivo, letra):
    with open(archivo, "r") as f:
        contador = 0
        linea = f.readline()
        if linea[0] == letra:
            contador += 1        
        return contador


#Ejercicio 2

def imprimir_lineas(archivo, n):
    with open(archivo, "r") as f:
        for i in range(n):
            print(f.readline())


#Ejercicio 3

def n_ultimas_lineas(archivo, n):
    with open(archivo, "r") as f:
        lineas=[]
        for linea in lineas:
            lineas.append(f.readline())
        print(lineas[-n:])


#Ejercicio 4

def cuantas_palabras_archivo(archivo):
    with open(archivo, "r") as f:
        linea = f.readline()
        palabras = linea.split()
        return len(palabras)

#Ejercicio 5

def remplazar_letra(archivo, letra):
    with open(archivo, "r") as f:
        linea = f.readline()
        lineas = linea.replace(letra, letra + "\n")
        with open("archivo_nuevo", "w") as f2:
            f2.write(lineas)


#Ejercicio 6

def sin_salto_de_linea(archivo):
    with open(archivo, "r") as f:
        linea = f.readline()
        lineas = linea.replace("\n", "")
        with open("archivo_nuevo", "w") as f2:
            f2.write(lineas)


#Ejercicio 7

def palabra_mas_larga(archivo):
    with open(archivo, 'r') as f:
        palabras = f.read().split()
        maslarga = max(palabras, key=len)
    return print(maslarga), print(len(maslarga))


#Ejercicio 8

def Joinfiles(file1, file2, file3):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "a") as f3:
        f3.write(f1.read() + f2.read())
Joinfiles("Docuemento 1", "Documento 2", "Documento 3")


#Ejercicio 9

def frecuencia_palabra(archivo, palabra):
    with open(archivo) as f:
        linea = f.readline()
        palabras = linea.split()
        contador = 0
        for i in range(len(palabras)):
            if palabras[i] == palabra:
                contador += 1
        return contador/len(palabras)


#Ejercicio 10

def  agregar_archivos(path_carpeta):
    import os
    lista = os.listdir(path_carpeta)
    for i in lista:
        if i.endswith(".txt"):
            with open("documento", "a") as f:
                with open(i, "r") as f2:
                    f.write(f2)