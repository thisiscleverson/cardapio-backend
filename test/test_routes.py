import json
import pytest
from app import app


@pytest.fixture()
def client():
   app.config['TESTING'] = True
   with app.test_client() as client:
      yield client


def test_request_return_404(client):
   assert client.get("/").status_code == 404 


def test_foods_request_return_200(client):
   response = client.get('/foods')
   assert response.status_code == 200


def test_foods_is_dict(client):
   response = client.get('/foods')
   data = json.loads(response.data)
   assert type(data[0]) is dict


def test_save_food_post_return_200(client):

   headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
   }

   data = {
      "name": "Pastel",
	   "price": 9,
	   "image": "https://uploads.bemparana.com.br/upload/image/blogpost/tb2/blogpost_827897_img1_pastel-poro.jpg"
   }

   dataJson = json.dumps(data)
   response = client.post('/save-food', data=json.dumps(data), headers=headers)
   
   assert response.status_code == 200


def test_delete_food_return_200(client):

   response = client.get('/foods')
   data = json.loads(response.data)

   food_id = data[len(data) - 1]["id"] # Retrieve the ID of the last item that was saved in the database.

   response = client.delete(f'/delete/food/{food_id}')

   assert response.status_code is 200