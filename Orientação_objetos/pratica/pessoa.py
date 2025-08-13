##refatorando uma função

class Pessoa:
    pessoas = []
    def __init__(self, nome = '', idade = int, profissao = ''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f' {self._nome}|{self._idade}|{self._profissao}'
    
    
    def anivesario(self):
        self._idade += 1

    @property
    def saudacao(self):
      return f'Olá, sou {self._nome}! Trabalho como {self._profissao}.'
    

    def listar_pessoas():
        print('Informações iniciais:\n')
        for pessoa in Pessoa.pessoas:
            print(f'Olá, eu sou {pessoa._nome} e tenho {pessoa._idade} anos e minha profissão é {pessoa._profissao}.\n')
        
        print('Informações pós aniversário:\n')
        for pessoa in Pessoa.pessoas:
            pessoa._idade += 1
            print(f'Olá, eu sou {pessoa._nome} e tenho {pessoa._idade} anos e minha profissão é {pessoa._profissao}.\n')
    
    

pessoa1 = Pessoa(nome='Anabel', idade = 25, profissao = 'Engenheira')
pessoa2 = Pessoa(nome='Juliete', idade = 30, profissao = 'Desenvolvedor')
pessoa3 = Pessoa(nome='kamala', idade = 28,  profissao = 'Veterinária')

Pessoa.listar_pessoas()

