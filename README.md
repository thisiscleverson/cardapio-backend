

### como execultar a api
```sh
flask --app app/ run --debug
``` 

### criando as migrations
* criando pasta para as migrations
```sh
flask --app app/ db init 
```

* criando a primeira migration
```sh
flask --app app/ db migrate -m "initial migrate."
```
você pode usar esse mesmo comando para gerar uma nova versão

* criando a tabela diretamente no banco de dados
```sh
flask --app app/ db upgrade
```
esse comando vai criar a tabela na banco de dados

### criar um arquivo `.env`
```
USER=''
HOST=''
PORT=''
PASS=''
DB=''
```