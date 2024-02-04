def leerArchivo():
    try:
        contenido = open("mensaje.txt", "r")
        for mensaje in contenido:
            print(mensaje.strip("\n")[::-1])
    except:
        print("el archivo no existe")


leerArchivo()
