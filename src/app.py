"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, Characters, Starship, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users)

@app.route('/user', methods=['POST'])
def handle_addUser():
    request_body=request.get_json()
    new_user = User(email=request_body['email'],name=request_body['name'],tel=request_body['tel'])    
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user,'user successfully created'), 200

@app.route('/characters', methods=['GET'])
def getAllCharacters():
    characters = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))
    return jsonify(all_characters)

@app.route('/characters/<int:id>',methods=['GET'])
def getEachCharacter(id):
    character = Characters.query.get(id)
    return jsonify(character.serialize()), 200

@app.route('/characters/<int:id>',methods=['DELETE'])
def deleteCharacter(id):
    character = Characters.query.get(id)
    db.session.delete(character)
    db.session.commit()
    return jsonify(character,'successfully deleted'), 200

@app.route('/characters',methods=['POST'])
def addCharacter():
    request_body= request.get_json()
    character=Characters(
        characters_birth_year=request_body['characters_birth_year'],
        characters_eye=request_body['characters_eye'],
        characters_hair_color=request_body['characters_hair_color'],
        characters_height=request_body['characters_height'],
        characters_name=request_body['characters_name']
    )
    db.session.add(character)
    db.session.commit()
    return jsonify(character.serialize())

@app.route('/planet', methods=['GET'])
def getAllPlanets():
    planet = Planet.query.all()
    all_planet = list(map(lambda x: x.serialize(), planet))
    return jsonify(all_planet)

@app.route('/planet/<int:id>',methods=['GET'])
def getEachPlanet(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200

@app.route('/planet/<int:id>',methods=['DELETE'])
def deletePlanet(id):
    planet = Planet.query.get(id)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(planet,'successfully deleted'), 200

@app.route('/planet',methods=['POST'])
def addPlanet():
    request_body= request.get_json()
    planet=Planet(
        planet_climate=request_body['planet_climate'],
        planet_gravity=request_body['planet_gravity'],
        planet_name=request_body['planet_name'],
        planet_population=request_body['planet_population'],
        planet_terrain=request_body['planet_terrain']
    )
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize())

@app.route('/starship', methods=['GET'])
def getAllStarship():
    starship = Starship.query.all()
    all_starship = list(map(lambda x: x.serialize(), starship))
    return jsonify(all_starship)

@app.route('/starship/<int:id>',methods=['GET'])
def getEachStarship(id):
    starship = Starship.query.get(id)
    return jsonify(starship.serialize()), 200

@app.route('/starship/<int:id>',methods=['DELETE'])
def deleteStarship(id):
    starship = Starship.query.get(id)
    db.session.delete(starship)
    db.session.commit()
    return jsonify(starship,'successfully deleted'), 200


@app.route('/starship',methods=['POST'])
def addStarship():
    request_body= request.get_json()
    starship=Starship(
        starship_cost_in_Credit=request_body['cost_in_credit'],
        starship_length=request_body['starship_length'],
        starship_manufacturer=request_body['starship_manufacturer'],
        starship_model=request_body['starship_model'],
        starship_name=request_body['starship_name']
    )
    db.session.add(starship)
    db.session.commit()
    return jsonify(starship.serialize())


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
