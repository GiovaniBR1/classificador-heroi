# Passo 1: Declarar variáveis
nome = ""
xp = 0

# Laço de repetição para permitir múltiplas entradas
while True:
    # Passo 2: Entrada de dados
    nome = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de XP do herói: "))

    # Passo 3: Estrutura de decisão para determinar o nível do herói
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # Passo 4: Exibir a mensagem final
    print(f"O Herói de nome {nome} está no nível de {nivel}.")