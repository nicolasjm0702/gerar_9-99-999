palavra = str(input("Palavra ou caractere : "))
max = int(input("Maximo de caracteres: "))

def GerarNove(palavra, max):
    lista = []
    posAtual = int(1)
    resultado = str('')
    posSubstituida = 1
    outraPosSubstituida = 2
    x = 4
    y = 4

    while posAtual < max:
        lista.append(palavra)
        posAtual = posAtual + 1

    while posSubstituida < max ^ 2:
        lista.insert(posSubstituida, "?")
        posSubstituida = posSubstituida + x
        x = x + 1
        lista.insert(outraPosSubstituida, " ")
        outraPosSubstituida = outraPosSubstituida + y
        y = y + 1

    lista.append("? ")

    while len(lista) > max:
        lista.pop(max)

    for i in lista:
        resultado = f"{resultado}" + f"{i}"

    while len(resultado) > max:
        resultado = resultado[:-1]

    resultado = f"{resultado}?"

    if len(resultado) > max:
        char = resultado[-2]
        resultado = resultado[::-1].replace(char[::-1], ""[::-1], 1)[::-1]
        resultado = resultado.replace("? ? ", "? ")
        resultado = resultado.replace("? ? ", "?")
        resultado = resultado.replace("??", "?")
        resultado = resultado.replace("? ?", "?")
        print(resultado)
    else:
        print(resultado)

GerarNove(palavra, max)

pause = input(" ")