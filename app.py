from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/acompanhamento')
def acompanhamento():
    return render_template('acompanhamento.html')

@app.route('/gestao')
def gestao():
    return render_template('gestao.html')

@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/controle')
def controle():
    return render_template('controle.html')

if __name__ == '__main__':
    app.run(debug=True)
