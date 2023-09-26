import uuid
from app import app
from flask import jsonify, request, json
from app.db.schema import Foods
from app.db.config_db import db
from sqlalchemy import select



@app.route('/foods', methods=["GET"])
def foods_all():
   foods = Foods.query.all()
   
   response = []
   for food in foods:
      response.append({
         "id": food.id,
         "name" : food.name,
         "price": food.price,
         "image": food.image
      })

   return jsonify(response), 200


@app.route('/save-food', methods=["POST"])
def save_food():
   data = request.get_json()

   food = Foods(
      id    = str(uuid.uuid4()),
      name  = data['name'],
      price = data['price'],
      image = data['image']
   )
   
   db.session.add(food)

   try:
      db.session.commit()
   except Exception as error:
      print(error)
      return jsonify({'message': f'Não foi possovel adiconar o {data["name"]} no banco de dados. Verifique se o registro não é registrado.'}), 400

   return jsonify({'message': f'o {data["name"]} foi inserido banco de dados com sucesso!'}), 200


@app.route('/delete/food/<food_id>', methods=["DELETE"])
def delete_food(food_id: str):
   query = Foods.query.filter_by(id=food_id)
   exists = db.session.query(Foods.id).filter_by(id=food_id).first() is not None

   if exists == True:
      food  = query.first()
      query.delete()
      db.session.commit()
      return jsonify({"message": f'O {food.name} foi deletado com sucesso!'}), 200   
   else:
      return jsonify({"Message":"Registro não encontrado no banco de dados!"}), 404
