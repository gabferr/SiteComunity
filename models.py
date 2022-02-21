from main import database
from datetime import datetime


class Usuario(database.Model, 'extend_existing=True'):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, nullable=False, default='default.jpg')
    post = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, default='Usuario não informado', nullable=False)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.Foreignkey('usuario.id'), nullable=False)
