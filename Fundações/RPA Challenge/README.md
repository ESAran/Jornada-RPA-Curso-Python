# RPA Challenge
Versão final com interface, busca de dados na web e preenchimento de formulário. Construção base feita em sala de aula, mantendo a estrutura e incrementando algumas funcionalidades.

## Funcionamento

## Configurações

## Arquivos
### gui.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/gui.py)

### challenge.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/challenge.py)

### fake_data.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/fake_data.py)

### file_manipulation.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/file_manipulation.py)

### navigation.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/navigation.py)
Arquivo de navegação, funções do site para obter o driver e navegação na página com 3 classes.
> #### Imports:
> 
> Utilização da biblioteca Selenium para navegar na Web.
> 
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/0d99b444-cd1f-4284-acad-660ebd5bd1c8)

> #### Classe Browser:
> 
>  Possui a função chrome_browser que recebe um site por parâmetro e retorna o driver que será usado posteriormente pela biblioteca Selenium.
> > *chrome_browser*
> > 
> >  ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/88b0b62f-c0a9-486b-a825-c4dfd4d630a3)

> #### Classe PageObjects:
> 
> Possui as funções de iniciar(recebendo driver por parâmetro) e executar(recebendo driver e linha) o challenge, juntamente com a função de executar o fake_data
>
> > *Inicia Challenge:* Clica no botão de **Start** da tela inicial do RPA Challenge.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/bc28d17f-0854-482f-abf5-c5cf6eeb38c0)
