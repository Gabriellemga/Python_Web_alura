from livro import Livro


livro_biblioteca = Livro('Orgulho e Preconceito','Jane Austen', 1813)
print(f"Antes de emprestar : Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro_biblioteca.disponivel}")

livro_ano_publicacao = 1813
livro_disponivel = Livro.verificar_disponibilidade(livro_ano_publicacao)
print(f'Os livros publicados em {livro_ano_publicacao} disponiveis: {livro_disponivel}')