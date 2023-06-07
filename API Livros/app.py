from flask import Flask, redirect, request, jsonify

app = Flask(__name__)


livros = [{'id': 0, 'titulo': 'Verity', 'ano': 2020, 'autor': 'Colleen Hoover', 'paginas': 320},
          {'id': 1, 'titulo': 'A paciente silenciosa', 'ano': 2021, 'autor': 'Alex Michaelides', 'paginas': 350}]


@app.route('/')
@app.route('/livros')
def get_all():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def get_by_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return 'Livro não encontrado'


@app.route('/livros', methods=['POST'])
def book_insert():
    req = request.json
    livros.append(req)
    return redirect('/')


@app.route('/livros/<int:id>', methods=['PUT'])
def book_update(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return book_insert()
    return 'Livro não encontrado', 404


@app.route('/livros/<int:id>', methods=['DELETE'])
def book_delete(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return 'Livro deletado com sucesso!'
    return 'Livro não encontrado', 404


app.run(debug=True)
