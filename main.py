from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/agenda')
def agenda():
    return render_template('agenda.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/relatorio')
def relatorio():
    return render_template('relatorio.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


app.run(debug=True)

