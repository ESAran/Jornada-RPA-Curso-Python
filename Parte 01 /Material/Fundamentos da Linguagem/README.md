## Fundamentos da Linguagem

### Tipos de dados
Python é uma linguagem *tipada dinamicamente*, ou seja, não é necessário declarar uma variável e definir o tipo de seu dado. O tipo de dado será definido em tempo de execução de acordo com o valor atribuído para aquela variável.

A linguagem apresenta os tipos comuns de dados apresentados na tabela a seguir:

|Python | O que significa
|:---:|:---|
| int| Valores inteiros: …, -2, -1, 0, 1, 2, 3 |
| float     | Valores com ponto flutuante: 1.3, 2.3872 |  
| string    | Textos: python considera texto tudo que estiver entre aspas (simples ou duplas)        |
| bool     | Valores booleanos: True, False |

Pode-se usar a função embutida [`type()`](https://docs.python.org/pt-br/3/library/functions.html#type) para verificar o tipo de dado de um valor qualquer. Rode a célula abaixo para visualizar um exemplo:
|função | resultado
|:---:|:---|
| type(45)| **int** |

### Atribuição de valores

O sinal de igual (`=`) atribui um valor a uma variável. Pense em uma variável simplesmente como algo que pode variar ou cujo valor poder mudar.

Por exemplo, podemos declarar `nome = 'Maria'` e, se precisar utilizar este nome no futuro, ao invés de digitá-lo novamente, podemos simplesmente chamar a variável `nome`.

Nomes de variáveis podem ser qualquer coisa que nós quiseremos, mas existem algumas regras e convenções para serem seguidas:

- Eles devem começar apenas com letras ou traço baixo (underscore: `_`) e podem conter letras, *underscore* e números;
- Os nomes são `case sensitives`. Ou seja, `Ano` é diferente de `ano`. Em geral, em Python, usamos os nomes das variáveis todos em minúsculas e com underscore para separar palavras quando necessário.
- Use nomes de variáveis que sejam descritivos e sigam estas convenções do mundo Python. Por exemplo, é melhor usar `ano_nascimento` do que `AnoNascimento` ou `AnNasc`.

Para saber mais sobre o assunto, você pode conferir este texto do [site The Hello World Program](https://thehelloworldprogram.com/python/python-variable-assignment-statements-rules-conventions-naming/) ou [esta explicação do Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3).
