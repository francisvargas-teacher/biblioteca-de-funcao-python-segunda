def segunda_maior(lista):
    maior = None
    segunda = None

    for nota in lista:
        if maior == None or nota > maior:
            segunda = maior
            maior = nota

        elif nota != maior:
            if segunda == None or nota > segunda:
                segunda = nota

    return segunda


notas = [8.5, 9.0, 7.5, 9.0, 6.0]

print(segunda_maior(notas))
