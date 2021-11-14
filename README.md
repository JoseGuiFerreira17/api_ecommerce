# API E-commerce

API para gerenciamento de catálogo de produtos do e-commerce

## Documentação

A documentação para uso desta API se encontra no arquivo DOC.md

## Como desenvolver?

1. Clone o repositório
```console
git clone https://github.com/JoseGuiFerreira17/ecommerce.git
```
2. Entre na pasta do mesmo
```console
cd ecommerce
```
3. Crie um virtualenv com Python 3
```console
python3 -m venv venv
```
4. Ative o virtualenv
```console
source .env/bin/activate
```
5. Instale as dependências
```console
pip install -r requirements.txt
```
6. Copie o ENV_SAMPLE para um novo arquivo chamado .env e depois o abra e mude os valores das variáveis caso seja necessário

7. Execute as migrations
```console
python manage.py migrate
```
8. Execute os testes
```console
python manage.py test
```
9. Crie um superusuário
```console
python manage.py createsuperuser
```
10. Execute a aplicação
```console
python manage.py runserver
```


## Após isso execute os seguintes passos:
1. Abra a sua url_base/admin/ (ex.: http://127.0.0.1:8000/admin)
2. Acesse com os dados do super usuário
3. Vá em 'DJANGO OAUTH TOOLKIT', em 'Applications' clique em 'Adicionar'
4. Ná pagina de adição de 'Applications', em 'Client type' selecione a opção 'Confidential'
5. Em 'Authorization grant type' selecione a opção 'Resource owner password-based'
6. Guarde os valores gerados em 'Client id' e em 'Client secret', eles serão usados na autenticação da API, e a forma de usar deve ser consultada no arquivo DOC.md

