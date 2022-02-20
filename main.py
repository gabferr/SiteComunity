from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['Gabriel', 'Elias', 'Lucas', 'Ferrandin']

app.config['SECRET_KEY'] = '6e1fb9b48d785e11ff8271df05709849exit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///comunidade.db'

database = SQLAlchemy(app)


@app.route("/")
def inicio():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash('Login feito com sucesso para {}'.format(form_login.email.data), 'alert-success')
        return redirect(url_for('inicio'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash('Conta criada com sucesso para {}'.format(form_criarconta.email.data), 'alert-success')
        return redirect(url_for('inicio'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
