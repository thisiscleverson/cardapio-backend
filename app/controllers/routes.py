from app import app, db, engine
from flask import jsonify, request, json
from sqlalchemy.orm import sessionmaker
from app.model import Foods
import uuid


@app.route('/foods', methods=["GET"])
def foods_all():
   Session = sessionmaker(bind=engine)
   session = Session()
   #foods = db.session.execute(db.select(Foods)).scalars()
   foods  = Foods.query.all()
   
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
   db.session.commit()

   return jsonify({'message': f'o {data["name"]} foi inserido banco de dados com sucesso!'}), 200