from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.model import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField(' Nome de Usuário', validators=[DataRequired()])
    email = StringField('Digite seu E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Digite sua Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Repita sua Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro e-mail")


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(4, 8)])
    lembrar = BooleanField('Lembrar dados')
    botao_submit_login = SubmitField('Fazer Login')


class FomrEditarPerfil(FlaskForm):
    username = StringField(' Nome de Usuário', validators=[DataRequired()])
    email = StringField('Digite seu E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Curso Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_poerbi = BooleanField('PowerBI Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Apresentações Impressionador')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit_editarperfil = SubmitField('Editar Perfil')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário com esse e-mail!")


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do post', validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField('Seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')