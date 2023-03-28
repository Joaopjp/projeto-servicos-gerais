from main import db

class Agenda(db.Model):
    agenda_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agenda_data_programada = db.Column(db.Date(), nullable=False)
    agenda_hora_programada = db.Column(db.Time(), nullable=False)
    agenda_observacao = db.Column(db.String(1024), nullable=False)
    agenda_data_realizada = db.Column(db.Date(), nullable=True)
    agenda_hora_realizada = db.Column(db.Time(255), nullable=False)
    agenda_status = db.Column(db.String(255), nullable=False)
    setor_id_fk = db.Column(db.String(255), nullable=False)
    funcionario_id_fk = db.Column(db.String(255), nullable=False)
    servico_id_fk = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Setor(db.Model):
    setor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    setor_nome = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Servico(db.Model):
    servico_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    servico_nome = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Funcionario(db.Model):
    funcionario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    funcionario_nome = db.Column(db.String(255), nullable=False)
    funcionario_cargo = db.Column(db.String(255), nullable=False)
    funcionario_email = db.Column(db.String(255), nullable=False)
    funcionario_login = db.Column(db.String(255), nullable=False)
    funcionario_senha = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
