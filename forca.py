def jogar():

      print(9 * '.**',
            '\n Bem vindo ao jogo da Forca! \n',
            9 * '.**')

      palavra_secreta = 'banana'.upper()
      letras_acertadas = ['_','_','_','_','_','_']
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

      print('Fim do jogo')

if(__name__ == '__main__'):
      jogar()
