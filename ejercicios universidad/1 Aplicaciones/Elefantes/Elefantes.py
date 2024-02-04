def Elefantes(resistencia):
    elefantes = pesoAcumuladoElefante = 0
    cantidadElefantes = int(input())
    for e in range(cantidadElefantes):
        pesoAcumuladoElefante += int(input())
        if pesoAcumuladoElefante <= resistencia:
            print(
                f"{e+1} Un elefante se balanceaba sobre la tela de una araña, como veía que resistía fue a llamar a otro elefante."
            )
            elefantes += 1
    print(f"e: {elefantes}")


def main():
    resistencia = int(input())
    Elefantes(resistencia)


main()
