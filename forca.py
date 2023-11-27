def jogar():

      print('*************************** \n'
            'Bom vindo ao jogo da forca! \n'
            '***************************')

      palavra_secreta = 'banana'
      letras_acertadas = ['_','_','_','_','_','_']
      letras_faltando = str(letras_acertadas.count('_'))
      enforcou = False
      acertou = False
      tentativas = 0

      print(letras_acertadas)

      while(not enforcou and not acertou):

            chute = input('Qual letra? ')
            chute = chute.strip()

            if(chute in palavra_secreta):
                  index = 0
                  for letra in palavra_secreta:
                        if(chute.upper() == letra.upper()):
                              letras_acertadas[index] = letra
                        index += 1
            else:
                  tentativas += 1

            enforcou = tentativas == 6

            print(letras_acertadas)
            print(f'Ainda falta acertar {letras_faltando} letras')

      print('Fim do jogo')

if(__name__ == '__main__'):
      jogar()
