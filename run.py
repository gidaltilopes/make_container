from flask import Flask, render_template

app = Flask(__name__)


lista = ('postgres', 'nginx', 'totem')
@app.route('/')
def inicio():
	return render_template('index.html', cabecalho='Meus trabalhos', servicos=lista)



app.run(debug=True)
