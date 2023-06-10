import random 

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1 
    pontos = 1000


    print("Escolha o Nivel de dificuldade")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Defina um nível: "))
    if (nivel == 1):
        total_de_tentativas = 15

    elif (nivel == 2):
        total_de_tentativas = 10

    else:
        (nivel == 3)
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = input("Digite um número de 1 e 100: ")
        print("Você digitou: ", chute)
        chute = int(chute)

        if(chute < 1 or chute > 100 ):
            print("Você deve digitar um número entre 1 e 100 !")
            continue 

        acertou = (numero_secreto == chute)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Você acertou! e fez {} pontos !".format(pontos))
            break
        else:

            if(maior):
                print("Você errou! O numero escolhido foi maior do que o numero secreto!")
            elif(menor):
                print("Você errou! O numero escolhido foi menor do que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()