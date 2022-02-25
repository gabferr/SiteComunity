from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.model import Usuario


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
    botao_submit_editarperfil = SubmitField('Editar Perfil')