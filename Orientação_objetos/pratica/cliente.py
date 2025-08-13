class Cliente:
     def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
	 
     def __str__(self):
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone}'

cliente_1 = Cliente('Juliana', '25', 'ju@gmail.com', '99686-5214')
cliente_2 = Cliente('Ana', '20', 'ana@gmail.com', '99686-0000')
cliente_3 = Cliente('Bob', '28', 'bob@gmail.com', '99600-8714')
	
print(cliente_1)
print(cliente_2)
print(cliente_3)