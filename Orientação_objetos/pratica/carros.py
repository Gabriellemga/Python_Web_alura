class Carro:      
    def __init__(self, modelo, ano, cor ):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
      
    def __str__(self):
        return f' {self.modelo} | {self.ano} | {self.cor}'
    

    
byd = Carro('Dolphin', 'preto', '2025')

print(byd)




