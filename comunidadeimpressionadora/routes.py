from comunidadeimpressionadora import app, database, bcrypt
from flask import render_template, redirect, url_for, request, flash
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta, FomrEditarPerfil
from comunidadeimpressionadora.model import Usuario
from flask_login import login_user, logout_user, current_user, login_required

lista_usuarios = ['Gabriel', 'Elias', 'Lucas', 'Ferrandin']


@app.route("/")
def inicio():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar.data)
            flash('Login feito com sucesso para {}'.format(form_login.email.data), 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('inicio'))
        else:
            flash('Falha no login. e-mail ou senha incorretos ', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_crypt = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_crypt)
        database.session.add(usuario)
        database.session.commit()
        flash('Conta criada com sucesso para {}'.format(form_criarconta.email.data), 'alert-success')
        return redirect(url_for('inicio'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso', 'alert-success')
    return redirect('/')


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)


@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criar_post.html')


@app.route('/perfil/editar')
@login_required
def editar_perfil():
    form = FomrEditarPerfil()
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)