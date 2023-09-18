def convertirHoraReflejada(horas, minutos):
    hora_real = minuto_real = 0
    if minutos == 00:
        hora_real = 12
    else:
        hora_real = minutos // 5
    if horas == 12:
        minuto_real = 00
    else:
        minuto_real = horas * 5
        if minutos % 5 != 0:
            minuto_real += minutos % 5 + 1
    print(
        f"hora reflejada ingresada -> hrs: {horas}:{minutos} \n hora real convertida -> hrs: {hora_real} : mins {minuto_real}"
    )


convertirHoraReflejada(12, 00)
convertirHoraReflejada(12, 30)
convertirHoraReflejada(6, 00)
convertirHoraReflejada(6, 30)
convertirHoraReflejada(2, 48)
convertirHoraReflejada(6, 42)
