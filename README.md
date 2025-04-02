# Calculadora de IMC

## Sobre o projeto
Este projeto é uma aplicação web simples para calcular o Índice de Massa Corporal (IMC). O usuário informa seu peso e altura, e o sistema retorna sua classificação de acordo com a tabela de IMC.

## Tecnologias utilizadas
- Python
- Django
- HTML
- CSS (se aplicável)

## Como executar o projeto

### 1. Clonar o repositório
```sh
 git clone https://github.com/seu-usuario/imc-calculator.git
 cd imc-calculator
```

### 2. Criar e ativar um ambiente virtual (opcional, mas recomendado)
```sh
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

### 3. Instalar as dependências
```sh
pip install -r requirements.txt
```

### 4. Executar a aplicação
```sh
python manage.py runserver
```
Acesse a aplicação em `http://127.0.0.1:8000/`.

## Estrutura do projeto
```
projectIMC/
|---imc/
|    |---IMC/
|    |    |---templates/
|    |    |    |---IMC/
|    |    |    |    |---imc.html
|    |    |---views.py
|    |    |---urls.py
|---manage.py
```

## Funcionalidades
- Entrada de peso e altura pelo usuário.
- Cálculo automático do IMC.
- Exibição da classificação do IMC.

## Melhorias futuras
- Adicionar um design mais atraente com Bootstrap.
- Permitir a entrada de medidas em outras unidades (ex: libras e pés).
- Salvar histórico de IMC do usuário.

## Contribuições
Sinta-se à vontade para contribuir! Você pode abrir uma issue ou enviar um pull request.


