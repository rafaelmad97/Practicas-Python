def calcularPromedios(lista):
    promedioControl = 0
    for i in range(len(lista)):
        valor = lista[i] * (i + 1) - promedioControl
        print(f"{int(valor)}")
        promedioControl += valor


def llenarRegistros(size):
    lista = []
    for i in range(size):
        lista.append(float(input()))
    return lista


def main():
    nRegistros = int(input())
    lista = llenarRegistros(nRegistros)
    calcularPromedios(lista)


main()
