### Exercício 01
Escreva uma função que recebe uma lista e um valor e retorna uma sub-lista apenas com os elementos menores do que o valor fornecido.

### Exercício 02
Escreva uma função que calcula a multiplicação de duas listas.

### Exercício 03
Construa uma função que recebe uma lista a a ordena com o algoritmo Bubble sort.

> *Bubble sort é um algoritmo muito simples. Ele começa no início da lista e compara os dois primeiros elementos. Se o primeiro for maior do que o segundo, eles são trocados. Esse processo se repete para cada par subsequente, até o final da lista. Depois o algoritmo volta ao início da lista e recomeça o processo, repetindo-o até não haver mais trocas. Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo bubble sort.*

### Exercício 04

Desenvolva uma aplicação que funciona como um jogo de adivinhação onde o usuário tem 10 tentativas de acertar um número gerado aleatoriamente através das dicas fornecidas. Para o desenvolvimento, siga as orientações a seguir.

a) Crie uma função que gera um número aleatório inteiro entre 0 e 100. Este valor deve ser retornado e armazenado em uma variável. Utilize a função `randint()`.
```python
import random
print(random.randint(3, 9))
```

b) Crie uma função que avalia se o número é igual, maior ou menor que o número gerado randomicamente. A função deve receber o número randômico e dentro dela pedir para o usuário digitar um número. Após avaliar deve retornar 0 se forem iguais, -1 se o valor digitado foi MENOR e 1 se o valor digitado foi MAIOR.

c) Para construir a dinâmica do jogo use a função de sorteio de número criada e a função de avaliação de valor. O jogador tem no máximo 10 tentativas para acertar o número; Se o jogador não acertou o número e ainda tem tentativas, a aplicação deve informar se o número digital é MAIOR ou MENOR que o número sorteado e pede uma nova digitação de número correspondente a uma nova tentativa, sempre chamando a função criada; Se o usuário acertar o número sorteado, o jogo termina; Se o jogador digitar o número 0 significa que ele está desistindo dessa partida. A desistência representa perda da partida.
