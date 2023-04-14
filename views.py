from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models import Agenda, Setor, Servico, Funcionario


@app.route('/funcionarios')   # listagem de funcionarios cadastrados
def funcionarios():
    lista_funcionarios = Funcionario.query.order_by(Funcionario.funcionario_id)
    return render_template('funcionarios.html', titulo='Funcionários', func=lista_funcionarios)


@app.route('/novofuncionario')  # Formulário para o cadastro de novos funcionários
def novofuncionario():
    return render_template('novofuncionario.html', titulo='Cadastro de Novo Funcionário')


@app.route('/criarnovofuncionario', methods=['Post', ])  # metodo POST aqui salva as informações inseridas no BD
def criarnovofuncionario():
    nome = request.form['nome_funcionario']
    cargo = request.form['novoCargo']
    email = request.form['funcionarioEmail']
    login = request.form['funcionarioLogin']
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


@app.route('/editarfuncionario/<int:id>')
def editarfuncionario(id):
    funcionario = Funcionario.query.filter_by(funcionario_id=id).first()
    return render_template('editar_funcionario.html', titulo='editando funcionário', func=funcionario)


@app.route('/atualizarfuncionario', methods=['POST', ])  # metodo POST aqui salva as informações inseridas no BD
def atualizarfuncionario():
    funcionario = Funcionario.query.filter_by(funcionario_id=request.form['id']).first()
    funcionario.funcionario_nome = request.form['Nome']
    funcionario.funcionario_cargo = request.form['Cargo']
    funcionario.funcionario_email = request.form['Email']
    funcionario.funcionario_login = request.form['Login']
    funcionario.funcionario_senha = request.form['Senha']

    db.session.add(funcionario)
    db.session.commit()
    return redirect(url_for('funcionarios'))


@app.route('/setores')  # listagem de setores
def setores():
    lista_setores = Setor.query.order_by(Setor.setor_id)
    return render_template('setores.html', titulo='Salas/Setores',  lista_setores=lista_setores)


@app.route('/novosetor')  # formulário de cadastro de novo setor
def novo_setor():
    return render_template('novosetor.html', titulo='Novo Setor')


@app.route('/cadastrarsetor', methods=['POST', ])  # metodo POST aqui salva as informações inseridas no BD
def cadastrarsetor():
    nome = request.form['novo_setor']
    setor = Setor.query.filter_by(setor_nome=nome).first()

    if setor:
        flash('Setor Existente')
        return redirect(url_for('setores'))

    novo_setor = Setor(setor_nome=nome)

    db.session.add(novo_setor)
    db.session.commit()

    return redirect(url_for('setores'))


@app.route('/editarsetor/<int:id>')
def editarsetor(id):
    setor = Setor.query.filter_by(setor_id=id).first()
    return render_template('editar_setor.html', titulo='editando setor', setor=setor)


@app.route('/atualizarsetor', methods=['POST', ])
def atualizarsetor():
    setor = Setor.query.filter_by(setor_id=request.form['id']).first()
    setor.setor_nome = request.form['setor_nome']

    db.session.add(setor)
    db.session.commit()

    return redirect(url_for('setores'))


@app.route('/servicos')  # listagem dos serviços
def servicos():
    lista_servicos = Servico.query.order_by(Servico.servico_id)
    return render_template('servicos.html', titulo='Serviços', lista_servicos=lista_servicos)


@app.route('/novoservico')  # formulário de cadastrar novo serviço
def novoservico():
    return render_template('novoservico.html', titulo='Novo Serviço')


@app.route('/cadastrarservico', methods=['POST', ])  # metodo POST aqui salva as informações inseridas no BD
def cadastrarservico():
    nome = request.form['novo_servico']
    servico = Servico.query.filter_by(servico_nome=nome).first()

    if servico:
        flash('Serviço Existente')
        return redirect(url_for('servicos'))

    novo_servico = Servico(servico_nome=nome)

    db.session.add(novo_servico)
    db.session.commit()

    return redirect(url_for('servicos'))


@app.route('/editarservico/<int:id>')
def editarservico(id):
    servico = Servico.query.filter_by(servico_id=id).first()
    return render_template('editar_servico.html', titulo='editando Serviço', servico=servico)


@app.route('/atualizarservico', methods=['POST', ])
def atualizarservico():
    servico = Servico.query.filter_by(servico_id=request.form['id']).first()
    servico.servico_nome = request.form['servico_nome']

    db.session.add(servico)
    db.session.commit()

    return redirect(url_for('servicos'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/')
def home():
    return redirect(url_for('homepage'))


@app.route('/listagem')
def listagem():
    return render_template('listagem.html')


@app.route('/autenticar', methods=['POST', ])
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