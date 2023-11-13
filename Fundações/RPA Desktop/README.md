# RPA Desktop
Funcionalidades de automação em Desktop com busca de imagem, abertura de programa com maximização de tela, envio de cliques e teclas.

## Funcionamento


## Configurações


## Arquivos
### main.py
Utiliza das funções dos outros arquivos para o funcionamento do programa.
> Passa o endereço do arquivo que vai ser utilizado para preenchimento e o caminho do Fakturama
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/8ef6ee4d-ef04-453e-a479-a3a5bea7c57b)

### fakturama.py
Arquivo referente as funções do Fakturama, abertura do aplicativo e cadastramento de produtos com um arquivo eccel.
> #### Imports
>
> Utiliza as bibliotecas PyAutoGui, pandas, psutil e o arquivo *navigation.py*
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/50fb53bb-c62d-4f5a-9303-94d53dde39e0)

> #### Classe Fakturama
> Função de abrir o aplicativo.
>
> > *open*: envia o comando de abrir o aplicativo e verifica se ele foi aberto.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/c353d633-235b-4cca-8e55-a6604bbae34c)
> 
> #### Classe FNew
> Funções de adição e cadastro ao Fakturama.
>
> > *products_spreadsheet*: recebe um arquivo xlsx, cria um "data frame" do mesmo, clica no botão new product e preenche os campos.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/72a8bb8a-9986-4614-952c-326abf651991)



### navigation.py
Arquivo de navegação, funções para obter posição de imagem na tela e maximizar e minimizar uma janela.
> #### Imports
>
> Utiliza as bibliotecas PyAutoGui, sys e time.
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/9ce6b3f7-60d1-437c-9c8c-ea04ef8700ae)

> #### Classe Desktop
> Funções de navegação do Desktop.
> 
> > *max* e *min*: maximiza e minimiza a janela em foco.
> > 
> >  ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/a312a3f0-f27c-4d7e-ae82-47f1711f8c35)
>
> #### Screen
> Funções de navegação da tela.
>
> > *try_locate_image*: recebe de parâmetro um caminho de uma imagem na pasta assets/images e uma quantidade de tentativas (opcional, caso não receba nada considera 5). Faz a busca da imagem na tela 5 vezes, caso localize, retorna a posição, caso não seja possível retorna um print do da tela como erro.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/321af632-5fe0-4e2d-b8cd-e48622d8b9fa)



