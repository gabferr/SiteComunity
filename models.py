from main import database
from datetime import datetime


class Usuario(database.Model):
    id = database.Column(database.Integer, Primaty_key=True)
    username = database.Column(database.String, nulabble=False)
    email = database.Column(database.String, nulabble=False, unique=True)
    senha = database.Column(database.String, nulabble=False)
    foto_perfil = database.Column(database.String, default='default.jpg', nulabble=False)


class Post(database.Model):
    id = database.Column(database.Integer, Primaty_key=True)
    titulo = database.Column(database.String, nulabble=False)
    corpo = database.Column(database.String, nulabble=False)
    data_criacao = database.Column(database.DateTime, nulabble=False, default=datetime.utcnow)
