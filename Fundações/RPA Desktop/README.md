# RPA Desktop
Funcionalidades de automação em Desktop com busca de imagem, abertura de programa com maximização de tela, envio de cliques e teclas.

## Funcionamento

## Configurações

## Arquivos
### main.py
### fakturama.py
Arquivo referente as funções do Fakturama


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
> > *max* e *min*: Maximiza e minimiza a janela em foco.
> > 
> >  ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/a312a3f0-f27c-4d7e-ae82-47f1711f8c35)

> #### Screen
> Funções de navegação da tela.
>
> > *try_locate_image*: recebe de parâmetro um caminho de uma imagem na pasta assets/images e uma quantidade de tentativas (opcional, caso não receba nada considera 5). Faz a busca da imagem na tela 5 vezes, caso localize, retorna a posição, caso não seja possível retorna um print do da tela como erro.
> >
> >  ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/90672a1f-31a8-498d-99aa-a751236baf4f)


