import random


def play():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secrety_number = random.randrange(1, 101)
    print(secrety_number)
    rouds = 1

    score = 1000

    print("Qual o nível de dificuldade")
    print("(1) fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível "))

    if(nivel == 1):
        total_attempts = 20
    elif(nivel == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for rodada in range(1, total_attempts + 1):

        print("tentativa {} de  {}".format(rodada, total_attempts))

        kick_str = input("digite um valor numerico entre 1 e 100: ")

        kick_number = int(kick_str)

        if(kick_number < 1):
            print("O valor não poder ser menor que 1")
            continue

        if(kick_number > 100):
            print("O valor não poder ser maior que 100")
            continue

        print("Você digitou: ", kick_str)

        hit = secrety_number == kick_number

        bigger = kick_number > secrety_number
        smaller = kick_number < secrety_number

        rouds = rouds + 1

        if(hit):
            print("Vocẽ acertou sua pontuação foi {}".format(score))
            break
        else:
            if(bigger):
                print("Você errou, seu numero foi maior que o numero secreto")
            elif(smaller):
                print("Você errou, seu numero foi menor que o numero secreto")
            score_fail = abs(secrety_number - kick_number)
            score = score - score_fail

    print("Game over")


if(__name__ == "__main__"):
    play()
