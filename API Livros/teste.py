livros = [{'id': 0, 'titulo': 'Verity', 'ano': 2020, 'autor': 'Colleen Hoover', 'paginas': 320},
          {'id': 1, 'titulo': 'A paciente silenciosa', 'ano': 2021, 'autor': 'Alex Michaelides', 'paginas': 350}]


id = 1
for livro in livros:
    if livro['id'] == id:
        print(livro)