# Cardapio-BackEnd


## dependências
```Python
Flask >= 2.3.3
Flsk-Cors >= 4.0.0
Flask-Migrate >= 4.0.5
Flask-SQLAlchemy >= 3.1.1
psycopg2-binar >= 2.9.7
python-dotenv >= 1.0.0
```

## como execultar a API
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
``` 

## Execultando as migrações   
```sh
flask db init
flask db migrate
flask db upgrade
```
esses comandos vão criar a tabela na banco de dados

### arquivo `.env`
```
USER=''
HOST=''
PORT=''
PASS=''
DB=''
```

## Rotas da API
* [`GET`]: `/foods` pegar o cardápio de comidas no banco de dados
```json
[
	{
		"id": "057f1729-835a-4f12-93af-b1e6d50b13fb",
		"image": "https://s2.glbimg.com/-skQXghwNBeLCuYy742th0fMiZQ=/e.glbimg.com/og/ed/f/original/2019/12/10/marfrig.jpg",
		"name": "hambúrguer",
		"price": 20
	},
	{
		"id": "e66d102f-175b-4841-a180-1f2ccddffce0",
		"image": "https://i.pinimg.com/originals/71/99/dd/7199dd61697fdda51461eba6e4a9e079.jpg",
		"name": "bolo de chocolate",
		"price": 100
	}
]
```

* [`POST`]: `/save-food` adicionar um novo alimento no cardápio
```json
{
	"name": "bolo de chocolate3",
	"price": 100,
	"image": "https://i.pinimg.com/originals/71/99/dd/7199dd61697fdda51461eba6e4a9e079.jpg"
}
```

* [`DELETE`]: `/delete/food/<food_id>` deletar um alimento no cardápio pelo **ID**

##
> Para esse projeto eu estou usando o **postgresql** como banco de dados.