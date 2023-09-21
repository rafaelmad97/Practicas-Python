def validarCirculodeCables(value):
    listaCables = value.split(" ")
    conectoresf = conectoresm = 0
    for cable in listaCables:
        conectoresf += cable.count("F")
        conectoresm += cable.count("M")
    if conectoresm == conectoresf:
        print("Es posible hacer un unico circulo")
    else:
        print("No es posible")


def ingresarValores(size):
    lista = []
    for x in range(size):
        value = input()
        lista.append(value.upper())
    return lista


def leerValores(lista):
    for cables in lista:
        validarCirculodeCables(cables)


def main():
    size = int(input())
    lista = ingresarValores(size)
    leerValores(lista)


main()
