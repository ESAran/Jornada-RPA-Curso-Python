def bubblesort(vet):
    for i in range(0, len(vet)-1) :
        for j in range(0, len(vet)-1):
            if vet[j] > vet[j + 1]:
                aux = vet[j]
                vet[j] = vet[j + 1]
                vet[j + 1] = aux

        print(str(i+1) + " - passo: " + str(vet))


vet = [5, 4, 6, 2, 7, 4, 0, 3, 8, 1]
vet2 = [50, 40, 30, 20, 10]

bubblesort(vet)
print("")
bubblesort(vet2)
    
