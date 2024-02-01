from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    tel = db.Column(db.String(10), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites_id = db.relationship('Favorites')

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "tel" : self.tel
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_characters = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters=db.relationship('Characters',lazy=True)
    id_planet = db.Column(db.Integer, db.ForeignKey('planet.id'))
    id_starship = db.Column(db.Integer, db.ForeignKey('starship.id'))
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_characters": self.id_characters,
            "id_planet" : self.id_planet,
            "id_starship" : self.id_starship,
            "user_id" : self.user_id
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_climate = db.Column(db.Integer, nullable=False)
    planet_gravity = db.Column(db.Integer, nullable=False)
    planet_name = db.Column(db.String(250), unique=True, nullable=False)
    planet_population = db.Column(db.Integer, nullable=False)
    planet_terrain = db.Column(db.String(250), nullable=False)
   # id_favorites = db.Column(db.Integer, db.ForeignKey('Favorites.id'), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_climate": self.planet_climate,
            "planet_gravity" : self.planet_gravity,
            "planet_name" : self.planet_name,
            "planet_population" : self.planet_population,
            "planet_terrain" : self.planet_terrain,
          #  "id_favorites" : self.id_favorites
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters_birth_year = db.Column(db.String(20), nullable=False)
    characters_eye = db.Column(db.String(25), nullable=False)
    characters_hair_color = db.Column(db.String(20), nullable=False)
    characters_height = db.Column(db.Integer, nullable=False)
    characters_name = db.Column(db.String(250), nullable=False)
    #id_favorites = db.Column(db.Integer, db.ForeignKey('Favorites.id'), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "characters_birth_year": self.characters_birth_year,
            "characters_eye" : self.characters_eye,
            "characters_hair_color" : self.characters_hair_color,
            "characters_height" : self.characters_height,
            "characters_name" : self.characters_name,
          #  "id_favorites" :self.id_favorites
        }

class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starship_cost_in_Credit = db.Column(db.Integer, nullable=False)
    starship_length = db.Column(db.Integer, nullable=False)
    starship_manufacturer = db.Column(db.String(250), nullable=False)
    starship_model = db.Column(db.String(250), nullable=False)
    starship_name = db.Column(db.String(250), nullable=False)
    #id_favorites = db.Column(db.Integer, db.ForeignKey('Favorites.id'), nullable=False)

    def __repr__(self):
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "starship_cost_in_credit": self.starship_cost_in_credit,
            "starship_length" : self.starship_length,
            "starship_manufacturer" : self.starship_manufacturer,
            "starship_model" : self.starship_model,
            "starship_name" : self.starship_name,
           # "id_favorites" : self.favorites
        }


    