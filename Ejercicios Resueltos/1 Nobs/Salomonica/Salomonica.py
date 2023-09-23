def divisionSalomonica(valor):
    div = valor
    beneficiarios = 0
    while div > 9:
        div = div / 2
        beneficiarios += 1
    return beneficiarios


def main():
    valor = float(input())
    print(divisionSalomonica(valor))


main()
