# RPA Challenge
Versão final com interface, busca de dados na web e preenchimento de formulário. Construção base feita em sala de aula, mantendo a estrutura e incrementando algumas funcionalidades.

## Funcionamento
### Tela Inicial
> Possui as funções de recolher dados da Web ou executar o Challenge com o arquivo desejado.
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/1a1ee96c-f003-4bab-813d-00cd999a637c)


## Configurações
### Criação do ambiente virtual
A Criação do Virtual Environment não é extremamente necessária para rodar as aplicações, porém limita as bibliotecas àquele ambiente, então é uma maneira de isolar as instalações.

https://docs.python.org/pt-br/3/library/venv.html

> Criar o ambiente no console: 
> ***python -m venv venv***
> 
> <img src="https://user-images.githubusercontent.com/105756006/278388278-f4793fa8-314a-477d-911a-c90e4d137fb7.png" width="232" height="18.7">

> Ativar o ambiente com o script:
> ***venv/Scripts(Bin para mac/linux)/Activate***
>
> <img src="https://user-images.githubusercontent.com/105756006/278388312-a1b9f065-3b6d-42a9-9e13-c90bc9e2368f.png" width="443" height="29.5">

> Selecionar interpretador:
> **[ctrl] + [shift] + P > Select Interpreter > venv**
>
> <img src="https://user-images.githubusercontent.com/105756006/278388336-90e26927-9d80-4ef9-a481-72083c6cf646.png" width="443" height="111.5"><img src="https://user-images.githubusercontent.com/105756006/278388365-2817d987-e523-4976-af4c-0299bdedb3a5.png" width="443" height="113">

### Instalação da biblioteca
Para utilização do software, com o comando *pip install (nome da biblioteca)*
> #### Selenium [📄](https://selenium-python.readthedocs.io/): para automação Web.
> #### Pandas [📄](https://pandas.pydata.org/): para análise e manipulação de Dados.
> #### PyAutoGUI [📄](https://pyautogui.readthedocs.io/en/latest/): para interface gráfica.
> #### Outras: é possível que o programa peça algumas outras instalações para funcionamento das duas bibliotecas anteriores
## Arquivos
### gui.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/gui.py)
Controle de interface gráfica, funcionando como arquivo gatilho para rodar o programa através da função *tela_inicial*
> #### Imports
> Funções dos arquivos *challenge* e *fake_data* para dar o "start" nas funções do programa, juntamente com a biblioteca PyAutoGUI para interface gráfica do programa.
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/ab221f74-4c3a-4de4-a4ee-5e7e69ec0b19)
>
> #### Telas
>  Telas do programa e suas funções
> 
> > *tela_inicial:* A tela inicial é dividida em 3 seções com os textos para estilização, que contém os botões que vão executar as etapas do projeto.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/24d826c8-e5d6-45b8-8b54-1641783d8f12)
>
> > *tela_challenge:* corresponde à tela que vai solicitar qual arquivo vai ser utilizado para preencher os dados.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/4e533b3f-8318-4163-8fc0-181e6f92f4e9)
> >
> > *tela_result:* demonstra o resultado do RPA Challenge.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/1f46e2e9-99de-49e9-94ed-442b42637829)





### challenge.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/challenge.py)
Chama e utiliza as funções para rodar o preenchimento e funcionamento do Challenge em si, restornando o resultado que será exibido na tela posteriormente
> #### Imports
> Funções dos arquivos *navigation* e *file_manipulation* com utilização da Selenium para obtenção de elemento e time para setar espera.
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/9a7bbbf3-0eb0-4024-9456-07d462f5b000)



### fake_data.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/fake_data.py)
Possui a função fake_data para obtenção de dados gerados na Web aleatoriamente para preencher o RPA Challenge.
> #### Imports
>
> Funções dos arquivos *navigation* e *file_manipulation*.
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/6d32e131-4570-4f0b-837f-04fc2c4bc2d2)

> #### Funções
>
> *fake_data:* tem as variáveis de site e caminho do arquivo, obtém o driver e utiliza das funções dos outros scripts para criar o csv que será importado ao RPA Challenge.
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/b16ea966-2aff-4758-8697-9218d9acaea1)

### file_manipulation.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/file_manipulation.py)
Manipulação de arquivo, leitura e criação de CSV/XLSX
> #### Imports
>
> Utilização de pandas, csv e os.
>
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/920ef1b7-4e19-471b-840a-cff36c493e62)

> #### Funções
> O arquivo não tem uma classe definida, mas consta com duas funções.
>
> > *le_dados_challenge:* Faz a leitura de um arquivo CSV/XLSX, salvando as células em variáveis e retornando um vetor que será usado para preencher os campos posteriormente.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/fe731ebb-c699-4149-939d-7497e6b8594f)
> >
> > *cria_csv e escreve_csv:* Cria e adiciona linhas ao CSV
> > 
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/c7c17e3e-758c-4329-9604-387d5779aa61)




### navigation.py [📄](https://github.com/ESAran/Jornada-RPA-Curso-Python/blob/main/Funda%C3%A7%C3%B5es/RPA%20Challenge/navigation.py)
Arquivo de navegação, funções do site para obter o driver e navegação na página com 3 classes.
> #### Imports
> 
> Utilização da biblioteca Selenium para navegar na Web.
> 
> ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/0d99b444-cd1f-4284-acad-660ebd5bd1c8)

> #### Classe Browser
> 
>  Possui a função chrome_browser que recebe um site por parâmetro e retorna o driver que será usado posteriormente pela biblioteca Selenium.
> > *chrome_browser*
> > 
> >  ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/2e1899db-6094-4635-b253-daf89f2443b1)


> #### Classe PageObjects
> 
> Possui as funções de iniciar(recebendo driver por parâmetro) e executar(recebendo driver e linha) o challenge, juntamente com a função de executar o fake_data.
>
> > *inicia_challenge:* Clica no botão de **Start** da tela inicial do RPA Challenge.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/bc28d17f-0854-482f-abf5-c5cf6eeb38c0)
> >
> > *executa_challenge:* Idêntifica por **XPATH** os caminhos dos campos à serem preenchidos e envia as informações do vetor "row" recebido por parâmetro.
> > 
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/2e9ced32-1fd5-42de-b342-10b0b0db8d5b)
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/1ffed725-3a96-48b5-bc60-e23dd9a469b9)
> >
> > *executa_fake_data:* Busca por **XPATH** os elementos da página e retorna em um vetor, para posteriormente ser salvo em um csv.
> >
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/12709dae-524d-4653-b9e9-19b0006bd78d)
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/2e84599e-9fa0-47de-aefa-271c3ae69eda)

> #### Classe Waits
>
> Possui funções para aguardar um elemento na tela.
>
> > ![image](https://github.com/ESAran/Jornada-RPA-Curso-Python/assets/105756006/d93557a1-3b12-4781-b04b-ed2d5afe265c)





