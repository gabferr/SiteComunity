from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField(' Nome de Usuário', validators=[DataRequired()])
    email = StringField('Digite seu E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Digite sua Senha', validators=[DataRequired(), Length(4, 8)])
    confirmacao = PasswordField('Repita sua Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(4, 8)])
    lembrar = BooleanField('Lembrar dados')
    botao_submit_login = SubmitField('Fazer Login')

