from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class FormCriarConta(FlaskForm):
    nome = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Digite seu e-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    repetir_senha = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    manter_conectado = BooleanField('manter conectado')
    botao_submit_login = SubmitField('Fazer Login')
