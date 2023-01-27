def main():
    palavra = str(input("Digite uma palavra: "))
    maximo_caracteres = int(input("Digite o número máximo de caracteres: "))
    texto = ""
    while len(texto) < maximo_caracteres:
        texto += palavra + "? "
        palavra += palavra
    texto = texto[:(maximo_caracteres - 1)] + "?"
    print(texto)


if __name__ == "__main__":
    main()
    pause = input("")
