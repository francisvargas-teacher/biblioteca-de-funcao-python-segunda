def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return 0
    return a / b


def eh_par(numero):
    return numero % 2 == 0


def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)


def maior_valor(numeros):
    if not numeros:
        return None
    return max(numeros)


def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("Não existe fatorial de número negativo.")

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    return fatorial


def gerar_tabuada(numero):
    return [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]


def Menu_principal():
    while True:
        print("")
        print("")
        print("-=-=-=-=-=-=-=-=-==-=-=-=-=-=-===-=-=-=-=-")
        print("")
        print("             MENU_ARITMETICA:")
        print("")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("")
        print(" + = soma, - = subtração, * = multiplicação, / = divisão ")
        print("")
        print(" t = tabuada, f = fatorial, v = maior valor, p = par ")
        print("")
        print(" CM = calcular media, S = Sair")
        print("")
        opcoes = input(" Selecione as opções: ")

        if opcoes == "/":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(f"RESULTADO DE {a}/{b}: {dividir(a, b)}")

        elif opcoes == "S" or opcoes == "s":
            print("")
            print("saindo do programa")
            print(".")
            print(".")
            print(".")
            break


if __name__ == "__main__":
    Menu_principal()
