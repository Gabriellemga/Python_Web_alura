class ContaBancaria:
    def __init__(self, titular = '', saldo = int, ativo = False):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    @property
    def  titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._titular
    
    @property
    def ativo(self):
        return self._ativo


    
conta1 = ContaBancaria('Maia', 1000)
conta2 = ContaBancaria('Kamala', 2000)
conta3 = ContaBancaria('Alana', 5000)

print(f'Titular da conta 1 {conta1.titular}')
print(f'Titular da conta 2 {conta2.titular}')
print(f'Titular da conta 3 {conta3.titular}')


class ClienteBanco:
    clientes = []
    def __init__(self, nome, cidade, cpf, profissao, telefone ):
        self._nome = nome.title()
        self._cidade = cidade.title()
        self._cpf = cpf
        self._profissao = profissao
        self._telefone = telefone
        ClienteBanco.clientes.append(self)

    @classmethod
    def listar_clientes(cls):
        print('Relação dos Clientes')
        for cliente in cls.clientes:
            print(f'Nome: {cliente._nome}\nCidade: {cliente._cidade}\ncpf: {cliente._cpf}\nProfissão: {cliente._profissao}\nTelefone: {cliente._telefone}')
            print('-'* 20)


cliente1 = ClienteBanco('Kamala', 'Manaus', 12356236514, 'Veterinaria', 11111-222)
cliente2 = ClienteBanco('Juliana', 'Fortaleza', 87598674563, 'Medica', 85467-986)
cliente3 = ClienteBanco('Amanda', 'Natal', 78552478598, 'Engenheira', 85721-457)

ClienteBanco.listar_clientes()