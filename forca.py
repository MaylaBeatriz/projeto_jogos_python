import random
def jogar():

      imprime_mensagem_abertura()

      palavra_secreta = carrega_palavra_secreta()

      letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

      print(f'\n Palavra Secreta: \n {letras_acertadas}')

      tentativas = 0

      while(True):

            chute = pede_chute()

            if(chute in palavra_secreta):
                  marca_chute_correto(palavra_secreta, chute, letras_acertadas)
            else:
                  tentativas += 1
                  desenha_forca(tentativas)
                  print(f'Restam {7 - tentativas} tentativas.')

            print(letras_acertadas)

            if('_' not in letras_acertadas):
                  imprime_mensagem_vencedor()
                  break
            elif (tentativas == 7):
                  imprime_mensagem_perdedor(palavra_secreta)
                  break

def imprime_mensagem_abertura():
      print(9 * '.**',
            '\nBem vindo ao jogo da Forca!\n',
            9 * '.**')
def carrega_palavra_secreta():
      # alimentando a lista palavras[] a partir de um arquivo de texto
      arquivo = open('palavras.txt', 'r')
      palavras = []
      for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
      arquivo.close()

      # escolhendo a palavra_secreta usando o random
      numero = random.randrange(0, len(palavras))
      palavra_secreta = palavras[numero].upper()
      return palavra_secreta

def inicializa_letras_acertadas(palavra):
      return ['_' for letra in palavra]

def pede_chute():
      chute = input('\n Tente uma letra: ')
      chute = chute.strip().upper()
      return chute
def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
      index = 0
      for letra in palavra_secreta:
            if (chute == letra):
                  letras_acertadas[index] = letra
            index += 1

def imprime_mensagem_vencedor():
      print("Parabéns, você ganhou!")
      print("       ___________      ")
      print("      '._==_==_=_.'     ")
      print("      .-\\:      /-.    ")
      print("     | (|:.     |) |    ")
      print("      '-|:.     |-'     ")
      print("        \\::.    /      ")
      print("         '::. .'        ")
      print("           ) (          ")
      print("         _.' '._        ")
      print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
      print("Puxa, você foi enforcado!")
      print("A palavra era {}".format(palavra_secreta))
      print("    _______________         ")
      print("   /               \\       ")
      print("  /                 \\      ")
      print("//                   \\/\\  ")
      print("\\|   XXXX     XXXX   | /   ")
      print(" |   XXXX     XXXX   |/     ")
      print(" |   XXX       XXX   |      ")
      print(" |                   |      ")
      print(" \\__      XXX      __/     ")
      print("   |\\     XXX     /|       ")
      print("   | |           | |        ")
      print("   | I I I I I I I |        ")
      print("   |  I I I I I I  |        ")
      print("   \\_             _/       ")
      print("     \\_         _/         ")
      print("       \\_______/           ")

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
      jogar()
