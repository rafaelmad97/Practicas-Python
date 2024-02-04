def Panini(laminas):
    laminasRepetidas = i = aux = 0
    while i < len(laminas):
        if i != aux:
            if laminas[i] == laminas[aux]:
                laminasRepetidas += 0.5
        i += 1
        if i == len(laminas) and aux < len(laminas) - 1:
            aux += 1
            i = 0
    return int(len(laminas) - laminasRepetidas)


def agregarLaminas():
    laminas = []
    lamina = 1
    while lamina > 0:
        lamina = int(input())
        laminas.append(lamina)
    return laminas


def main():
    laminas = agregarLaminas()
    print(laminas)
    print(Panini(laminas))


main()
