class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataques = {
            'mago': 'magia',
            'guerreiro': 'espada',
            'monge': 'artes marciais',
            'ninja': 'shuriken'
        }
        ataque = ataques.get(self.tipo.lower(), 'um ataque desconhecido')
        print(f"o {self.tipo} atacou usando {ataque}")

# Testando a classe
def criar_heroi():
    nome = input("Digite o nome do herói: ")
    idade = int(input("Digite a idade do herói: "))
    tipo = input("Digite o tipo do herói (mago, guerreiro, monge ou ninja): ")
    return Heroi(nome, idade, tipo)

def main():
    heroi = criar_heroi()
    heroi.atacar()

if __name__ == "__main__":
    main()