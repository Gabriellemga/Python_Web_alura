##Mão na massa: classe música

class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')



jazz = Musica('Feeling Good', 'Nina Simone', 3)

bossa_nova = Musica('Garota de Ipanema', 'Tom Jobim', 4)

heavy_metal = Musica('Nothing Else Matters', 'Metallica', 6)

Musica.listar_musicas()


