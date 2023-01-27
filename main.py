from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import TIME

app = Flask(__name__)

app.secret_key = 'alura'


app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '123456jp',
        servidor = 'localhost',
        database = 'jogoteca'
    )

db = SQLAlchemy(app)


class Agenda(db.Model):
    agenda_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agenda_data_programada = db.Column(db.Date, nullable=False)
    agenda_hora_programada = db.Column(db.Time(), nullable=False)
    agenda_observacao = db.Column(db.String(1024), nullable=False)
    agenda_data_realizada = db.Column(db.Date, nullable=True)
    agenda_hora_realizada = db.Column(db.String(255), nullable=False)
    agenda_status = db.Column(db.String(255), nullable=False)
    setor_id_fk = db.Column(db.String(255), nullable=False)
    funcionario_id_fk = db.Column(db.String(255), nullable=False)
    servico_id_fk = db.Column(db.String(255), nullable=False)


class Setor(db.Model):
    setor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    setor_nome = db.Column(db.String(255), nullable=False)


class Servico(db.Model):
    servico_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    servico_nome = db.Column(db.String(300), nullable=False)


class Funcionario(db.Model):
    funcionario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funcionario_nome = db.Column(db.String(255), nullable=False)
    funcionario_cargo = db.Column(db.String(255), nullable=False)
    funcionario_email = db.Column(db.String(255), nullable=False)
    funcionario_login = db.Column(db.String(255), nullable=False)
    funcionario_senha = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


# lista de setores
setor_departamento1 = SetorDepartamento('Banheiro Masculino', 'Producao')
setor_departamento2 = SetorDepartamento('Banheiro Feminino', 'Producao')
setor_departamento3 = SetorDepartamento('Producao', 'Producao')
setor_departamento4 = SetorDepartamento('Sala Paris', 'Sala Reunião')
setor_departamento5 = SetorDepartamento('Sala de Treinamento', 'Sala Reunião')
setor_departamento6 = SetorDepartamento('Sala Madrid', 'Sala Reunião')
setor_departamento7 = SetorDepartamento('Sala Beijing', 'Sala Reunião')
lista_setores = [setor_departamento1, setor_departamento2, setor_departamento3, setor_departamento4, setor_departamento5, setor_departamento6, setor_departamento7]


@app.route('/funcionarios')
def funcionarios():
    FuncionarioDepartamento1 = FuncionarioDepartamento('Eliana Domiciano', 'Administrativo')
    FuncionarioDepartamento2 = FuncionarioDepartamento('Marlene Covelo', 'Administrativo')
    FuncionarioDepartamento3 = FuncionarioDepartamento('João Pedro', 'TI')
    FuncionarioDepartamento4 = FuncionarioDepartamento('Michele Fernandes', 'Almoxarifado')
    FuncionarioDepartamento5 = FuncionarioDepartamento('Fernando Lau', 'Diretoria')
    FuncionarioDepartamento6 = FuncionarioDepartamento('Livia Bueno', 'Administrativo')
    lista_funcionario = [FuncionarioDepartamento1, FuncionarioDepartamento2, FuncionarioDepartamento3, FuncionarioDepartamento4, FuncionarioDepartamento5, FuncionarioDepartamento6]
    return render_template('funcionarios.html', titulo='Funcionários', novofuncionario=lista_funcionario)


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
    return render_template('setores.html', titulo='Salas/Setores', l_setores=lista_setores)


@app.route('/servicos')
def servicos():
    servico1 = Servico('Limpeza da Sala')
    servico2 = Servico('Limpeza do Ar Condicionado')
    servico3 = Servico('Organização dos Materiais de Limpeza')
    servico4 = Servico('Recolhimento dos Lixos')
    lista_servicos = [servico1, servico2, servico3, servico4]
    return render_template('servicos.html', titulo='Serviços', servicos=lista_servicos)


app.run(debug=True)
