
import keyboard
import time
import random

duracao = 120
pontos = 0

perguntas = [
    ["5 + 7", 12],
    ["15 - 8", 7],
    ["6 x 4", 24],
    ["36 / 6", 6],
    ["9 * 7", 63],
    ["45 + 28", 73],
    ["100 - 37", 63],
    ["12 * 8", 96],
    ["144 ÷ 12", 12],
    ["25 * 4", 100],
    ["125 + 275", 400],
    ["250 - 85", 165],
    ["15 * 13", 195],
    ["225 ÷ 15", 15],
    ["32 * 11", 352],
    ["17 + 26", 43],
    ["81 ÷ 9", 9],
    ["14 * 14", 196],
    ["500 - 237", 263],
    ["19 * 12", 228],
]

nome = input("Qual é seu nome? ")
modo = input("Qual modo voce quer: classico ou infinito? ").lower()

if modo == "classico":
    print("gabriel: boa tarde", nome)
    keyboard.wait("space")

    print("gabriel: lembrou do dever, né?")
    keyboard.wait("space")

    print("bento: a professora está chegando")
    keyboard.wait("space")

    print("professora: boa tarde")
    keyboard.wait("space")

    print("todos: boa tarde")
    input("Escreva uma saudação: ")
    keyboard.wait("space")

    print("professora: tinha dever?")
    keyboard.wait("space")

    print("todos: sim")
    keyboard.wait("space")

    print("Você esqueceu o dever, vai ter que fazer agora!")
    keyboard.wait("space")

    pontos = 0

    for rodada in range(5):
        pergunta = random.choice(perguntas)
        resposta = input(f"Resolva: {pergunta[0]} = ")

        if resposta.strip().isdigit() and int(resposta.strip()) == pergunta[1]:
            print("Acertou!")
            pontos += 1
        else:
            print("Errou!")

    if random.randint(1,5) == 1:
        print("sua lapis quebrou a ponta!")
        print("aperte 10 vezes o espaço")

    for rodada in range(10):
        keyboard.wait("space")
        print(f"{rodada + 1}/10")
        print("lapis apontado")

        

    print("\nModo clássico concluído!")
    print(f"Fim do dever! Pontos: {pontos}/5")

    if pontos >= 4:
        print("professora: que dever bom", nome)
        print("voce: obrigado, professora")

elif modo == "infinito":
    opcao = input("Escolha o tempo: ")

    minutos = int(input("Quantos minutos quer jogar? "))
    duracao = minutos

    pontos = 0
    inicio = time.time()

    while time.time() - inicio < duracao:
        pergunta = random.choice(perguntas)
        resposta = input(f"Resolva: {pergunta[0]} = ")

        if time.time() - inicio >= duracao:
            break

        if resposta.strip().isdigit() and int(resposta.strip()) == pergunta[1]:
            print("Acertou!")
            pontos += 1
        else:
            print("Errou!")

    print("\nTempo esgotado!")
    print(f"Fim do dever! Pontos: {pontos}")

    if time.time() - inicio >= duracao and pontos >= 4:
        print("professora: que dever bom", nome)
        print("voce: obrigado, professora")

else:
    print("Modo inválido! Digite classico ou infinito.")
