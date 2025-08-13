class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)


    def __str__(self):
        return f'Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

livro1 = Livro('Orgulho e Preconceito','Jane Austen', 1813)
livro2 = Livro('Solaris','Stanislaw Lem', 1961)
livro3 = Livro('Fundação', 'Isac Asimov', 1951)


print(livro1)
livro1.emprestar()
print(f'Status : {livro1.disponivel}')
print(livro2)
livro2.emprestar()
print(f'Status : {livro2.disponivel}')

