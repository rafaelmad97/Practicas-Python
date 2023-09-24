def convertirSerpienteaCamello(cadena):
    cadenaDividida = cadena.split("_")
    valorConvertido = ""
    for value in cadenaDividida:
        if len(value):
            # print(f"{value[0:1]} | {value[1:len(value)]}")
            valorConvertido += value[0:1].upper()
            valorConvertido += value[1 : len(value)].lower()
    print(valorConvertido)


def listaFrases(size):
    lista = []
    for i in range(size):
        cadena = input()
        lista.append(cadena)
    return lista


def main():
    lista = listaFrases(int(input()))
    for cadena in lista:
        convertirSerpienteaCamello(cadena)


main()
