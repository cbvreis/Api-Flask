## Running the app

Primeiramente, devemos criar o virtualenv e ativar:

```
virtualenv -p python3 venv
source venv/bin/activate
```

Posterior ao comando acima, rodar a instalação das bibliotecas

```
pip install -r requirements.txt
```


Rodar o arquivo para iniciar 

```
python run.py
```
## Hello World
A aplicação funciona com autenticação JWT, portanto inicialmente deverá solicitar o token utilizando a requisição:
http://0.0.0.0:5000/v1/authenticate, após o recimento do token, a requisição deverá ser feita da seguinte forma: http://0.0.0.0:5000/v1?token=INSIRA_O_TOKEN.

Após a requsição, o retorno deverá ser: {"message": "Hello Nome_Usuario"}

## Tipos de retorno:
### 401 - Quando o toke é inválido, incorreto ou expirou
```
{
  "data": [], 
  "message": "token is invalid or expired"
}
```

### 401 - Quando não existe token:
```
{
  "data": [], 
  "message": "token is missing"
}
```
### 401 - Usuário não autorizado:
```
{
  'message': 'could not verify', 
  'WWW-Authenticate': 'Basic auth="Login required"'
}
```
### 401 - Usuário e senha incorretos:
```
{ 
  'message': 'user not found', 
  'data': []
}
  
```

### 200 - Retorno com sucesso:
```
{
    "exp": "Fri, 11 Jun 2021 02:29:37 GMT",
    "message": "Validated successfully",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ik5FT19BU1NJU1QiLCJleHAiOjE2MjMzNzg1Nzd9.B3gs3ioBQQis7oWCQeqkZDeTo0gwS3rP1l_49oOsSlI"
}
  
```
