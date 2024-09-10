# Resident-Api-Test: Projeto para automação de testes referente a api de residents

![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s---dy84CM3--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/ls1nn7bpt6xfxtm6vbam.png)

Esse projeto tem como finalidade de realizar testes automatizados da api de residents.

## Instalação

[Python](https://www.python.org/downloads/)

[Pipenv](https://pipenv.pypa.io/en/latest/)

Instalar as dependências do pacote.

```bash
pipenv install
```

Conexão com o banco de dados deve ser feito dentro do arquivo connection.py localizado na pasta db na raiz do projeto.

```bash
con = psycopg2.connect(host='localhost', database='database',
user='user', password='password')
```
Dentro no arquivo config.py poderá ser configurado algumas informações referente a API que será automatizada como por ex:

```bash
BASE_URI = 'http://localhost:3000'
```

Para utilizar os dados dentro de config.py, basta fazer o import da variável.

```bash
from config import BASE_URI
```

### Rodando o projeto

Para rodar o projeto é necessário rodar o seguinte comando primeiro para ativar o pipenv:

```bash
pipenv shell
```

Comando para rodar os testes no terminal:

```bash
pytest --mocha

pytest
```

Para gerar um html, o comando é:

```bash
pytest --html=report.html    
```

