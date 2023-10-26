
# Introdução
Aprendendo a configurar o ambiente com Virtual Environment, ajustandos caminhos do Chrome e selecionando e preenchendo elementos no Site RPA Challenge.

## Criação do Virtual Environment

### Passo a Passo
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

> Baixaar e importar as bibliotecas
> ***pip install selenium, pip install pandas***
>
> <img src="https://user-images.githubusercontent.com/105756006/278388424-f2051e4f-3e13-4986-b13f-984ae06a760d.png" width="300" height="91">

> Definir os caminhos do Chrome e Chromedriver:
> 
> `chrome_options = webdriver.ChromeOptions()`
> `chrome_options.add_argument("--start-maximized")`
>  
> `chrome_options.binary_location =  ("C:/Users/eduardo_aran/Documents/Cruso Python/ExerciciosIntro/2modulo/chrome-win64/chrome.exe")`
> 
> `chrome_driver_path =  ("C:/Users/eduardo_aran/Documents/Cruso Python/ExerciciosIntro/2modulo/chromedriver-win64/chromedriver.exe")`
> 
> `service_options = webdriver.ChromeService(executable_path=chrome_driver_path) `
>  `driver = webdriver.Chrome(options=chrome_options,service=service_options)`
> 
> <img src="https://user-images.githubusercontent.com/105756006/278388461-7f5f2372-c708-476f-bd09-219c27206dc5.png">

## Selecionando e preenchendo
### Selector
Para selecionar e preencher elementos dentro do RPA Challenge (site de testes de RPA), foram utilizadas funções da biblioteca Selenium

> Definindo variável *Site* com o URL e definindo o driver
> `site = "http://rpachallenge.com/"
driver.get(site)`
>
> <img src="https://user-images.githubusercontent.com/105756006/278464409-8390ba41-8366-4388-bd9b-df260dc56d78.png">


> Utiliza-se a função find_element By para achar um determinado elemento dentro do site, nesse caso sendo utilizado o **XPATH** para encontrar.
> `selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]')
selector.send_keys("Rua Gralha Azul, 45")`
>
> <img src="https://user-images.githubusercontent.com/105756006/278465306-2d9e0832-bbee-4cae-af5b-0fbda94d2c45.png" width="380" height="160"><img src="https://user-images.githubusercontent.com/105756006/278465215-5b2aac3d-f34e-43ad-b037-b44519406536.png" width="380" height="115">
> <img src="https://user-images.githubusercontent.com/105756006/278464735-de75c0d7-438f-487f-b91f-2e61ba5a2317.png">







