import random
def jogar():

      imprime_mensagem_abertura()

      arquivo = open('palavras.txt', 'r')
      palavras = []
      for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
      arquivo.close()

      numero = random.randrange(0, len(palavras))
      palavra_secreta = palavras[numero].upper()
      letras_acertadas = ['_' for letra in palavra_secreta]
      tentativas = 0

      print(f'\n Palavra Secreta: \n {letras_acertadas}')

      while(True):

            chute = input('\n Tente uma letra: ')
            chute = chute.strip().upper()

            if(chute in palavra_secreta):
                  index = 0
                  for letra in palavra_secreta:
                        if(chute == letra):
                              letras_acertadas[index] = letra
                        index += 1
            else:
                  tentativas += 1
                  print(f'Restam {6 - tentativas} tentativas.')

            print(letras_acertadas)

            if('_' not in letras_acertadas):
                  print('Você ganhou!')
                  break
            elif (tentativas == 6):
                  print('Você perdeu!')
                  break

      print(f'A Palavra Secreta era {palavra_secreta}! \nFim do jogo')

if(__name__ == '__main__'):
      jogar()

def imprime_mensagem_abertura():
      print(9 * '.**',
            '\nBem vindo ao jogo da Forca!\n',
            9 * '.**')