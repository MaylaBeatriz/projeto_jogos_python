import random
print("jogar")

def jogar():

    print("********************************* \n"
          "Bom vindo ao jogo de adivinhação! \n"
          "*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade você quer? \n (1)Fácil (2) Médio (3)Difícil")

    nivel = int(input("Nível desejado: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute =int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        errou_maior = chute > numero_secreto
        errou_menor = chute < numero_secreto

        if(acertou):
            print("Acertô mizerávi! Total de {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(errou_maior):
                print("Errrroou, seu chute foi maior que o secret number.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Total de {} pontos.".format(numero_secreto, pontos))
            elif(errou_menor):
                print("Errrroou, seu chute foi menor que o secret number.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Total de {} pontos.".format(numero_secreto, pontos))

    print("Fim do jogo")
#
# if(__name__ == '__main__'):
#     jogar()
