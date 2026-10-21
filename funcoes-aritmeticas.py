a = 0 
b = 0
def somar(a, b):
    pass
def subtrair(a, b):
    pass
def multiplicar(a, b):
    pass
def dividir(a, b):
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))
        resultado = a/b if b != 0 else 0 
        try:
         print(f"RESULTADO DE {a}/{b}: {a/b}")
        except:
            print(f"RESULTADO DE {a}/{b}: {resultado}")
        return Menu_principal()

def eh_par(numero):
    pass
def calcular_media(numeros):
    pass
def maior_valor(numeros):
    pass

def calcular_fatorial(numero):
    pass

def gerar_tabuada(numero):
    pass 

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
        opções = input(" Selecione as opções: ")
         
        if opções == "/":
            dividir(a, b)

        elif opções == "S" and opções == "s":
            print("")
            print("saindo do programa")
            print(".")
            print(".")
            print(".")
            break

if __name__ == "__main__":
    Menu_principal()
