palavra = input("digite uma palavra: ")
caracter = input("digite um caracter: ")

tam = len(palavra)

for i in caracter:
    palavra = palavra.replace(i,'')

print(palavra)
