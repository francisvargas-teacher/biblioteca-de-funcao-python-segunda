def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for caractere in texto if caractere in vogais)


def inverter_texto(texto):
    return texto[::-1]


def eh_palindromo(texto):
    texto_limpo = "".join(caractere.lower() for caractere in texto if caractere.isalnum())
    return texto_limpo == texto_limpo[::-1]


def contar_palavras(texto):
    return len(texto.split())

