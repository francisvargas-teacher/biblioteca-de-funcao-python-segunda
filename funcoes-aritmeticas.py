def somar(a, b):
    pass
def subtrair(a, b):
    pass

def multiplicar(a, b):
   return a * b
if __name__ == "__main__":
    a = float(input("Informe o primeiro número: "))
    b = float(input("Informe o segundo número: "))

    resultado = multiplicar(a, b)
    print(f"O resultado da multiplicação é: {resultado}")
    
def dividir(a, b):
    pass
def eh_par(numero):
    pass

def calcular_media(numeros):
    #Ricardo Quadros#
    if len(numeros) == 0:
        raise ValueError("A lista não pode estar vazia")
    return sum(numeros) / len(numeros)

def maior_valor(numeros):
    pass

def calcular_fatorial(numero):
    pass

def gerar_tabuada(numero):
    pass
