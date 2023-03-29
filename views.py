from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Agenda, Setor, Servico, Funcionario


@app.route('/funcionarios')
def funcionarios():
    lista_funcionarios = Funcionario.query.order_by(Funcionario.funcionario_id)
    return render_template('funcionarios.html', titulo='Funcionários', func=lista_funcionarios)


@app.route('/novofuncionario')
def novofuncionario():
    return render_template('novofuncionario.html', titulo='Cadastro de Novo Funcionário')


@app.route('/criarnovofuncionario', methods=['Post', ])
def criarnovofuncionario():
    nome = request.form['nome_funcionario']
    cargo = request.form['novoCargo']
    email = request.form['funcionarioEmail']
    login= request.form['funcionarioLogin']
    senha = request.form['funcionarioSenha']

    funcionario = Funcionario.query.filter_by(funcionario_nome=nome).first()

    if funcionario:
        flash('funcionário existente')
        return redirect(url_for('funcionarios'))

    novo_funcionario = Funcionario(funcionario_nome=nome, funcionario_cargo=cargo, funcionario_email=email,
                                   funcionario_login=login, funcionario_senha=senha)

    db.session.add(novo_funcionario)
    db.session.commit()

    return redirect(url_for('funcionarios'))


@app.route('/setores')
def setores():
    return render_template('setores.html', titulo='Salas/Setores', l_setores=lista_setores)


@app.route('/novosetor')
def novo_setor():
    return render_template('novosetor.html', titulo='Novo Setor')


@app.route('/cadastrarsetor', methods=['POST',])
def cadastrarsetor():
    novo_setor=request.form['novo_setor']
    departamento=request.form['departamento']
    salas=SetorDepartamento(novo_setor, departamento)
    lista_setores.append(salas)
    return redirect('/setores')


@app.route('/servicos')
def servicos():
    return render_template('servicos.html', titulo='Serviços', servicos=lista_servicos)


@app.route('/novoservico')
def novoservico():
    return render_template('novoservico.html', titulo='Novo Serviço')


@app.route('/cadastrarservico', methods=['POST',])
def cadastrarservico():
    novo_servico=request.form['novo_servico']
    Novo_Servico=Servico(novo_servico)
    lista_servicos.append(Novo_Servico)
    return redirect('/servicos')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/')
def home():
    return redirect(url_for('homepage'))


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'brtoken@1234!' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuario logado com sucesso!')
        return redirect('/homepage')
    else:
        flash('Usuario não logado!')
        return redirect('/login')


@app.route('/homepage_cadastro')
def homepage_cadastro():
    return render_template('/homepage_cadastro.html')