palavra = input("digite uma palavra: ")

tam = len(palavra)
for i in range (0, tam):
    if palavra[i] != palavra[tam - i - 1]:
        palindromo = False
    else:
        palindromo = True
    break

if (palindromo == True):
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
