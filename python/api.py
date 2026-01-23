#"CRIANDO UM API EM PYTHON"
#1. Objetivo - criar uma api  de  dispinibilidade a consulta , criacao ,  edicao , exclusao de livros
#2. Url base - http://127.0.0.1:5000/
#3. Metodos - get , post , put , delete
#4. Biblioteca - flask

from flask import Flask, request, jsonify
import flask

app = Flask(__name__)


livros = [
    {
        'id' : 1 , 
        'titulo' : 'O Senhor dos Aneis' , 
        'autor' : 'JRR Tolkien' ,
        'ano' : 1954 ,
        'genero' : 'Fantasia' 
    },
    {
        'id' : 2 , 
        'titulo' : 'O Hobbit' , 
        'autor' : 'JRR Tolkien' ,
        'ano' : 1937 ,
        'genero' : 'Fantasia'
    },
    {
        'id' : 3 , 
        'titulo' : 'Harry Potter e a Pedra Filosofal' , 
        'autor' : 'JRR Tolkien' ,
        'ano' : 1997 ,
        'genero' : 'Fantasia'
    },
]
# Consulta todos os livros
@app.route('/livros', methods=['GET'])
def consulta_livros():
    return jsonify(livros)

# Consulta um livro pelo id
@app.route('/livros/<int:id>', methods=['GET'])
def consulta_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'mensagem' : 'livro nao encontrado'})

#editar um livro 
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livro['titulo'] = request.json['titulo']
            livro['autor'] = request.json['autor']
            livro['ano'] = request.json['ano']
            livro['genero'] = request.json['genero']
            return jsonify(livro)
    return jsonify({'mensagem' : 'livro nao encontrado'})

#criar um livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = {
        'id' : len(livros) + 1,
        'titulo' : request.json['titulo'],
        'autor' : request.json['autor'],
        'ano' : request.json['ano'],
        'genero' : request.json['genero']
    }
    livros.append(novo_livro)
    return jsonify(novo_livro)

#excluir um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return jsonify({'mensagem' : 'livro excluido'})
    return jsonify({'mensagem' : 'livro nao encontrado'})

app.run(port = 5000 , host = '127.0.0.1' , debug = True)