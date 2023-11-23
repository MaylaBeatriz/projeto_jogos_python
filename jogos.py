import forca as batata
import adivinhacao

print("BATATATA")
def escolhe_jogo():
    print("***************** \n"
          "Escolha seu jogo! \n"
          "*****************")

    print("(1)Forca (2)Adivinhação")
    jogo = int(input("Qual jogo você quer? "))

    if(jogo == 1):
        print("Jogando Forca")
        batata.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == '__main__'):
    print("__main__")
    escolhe_jogo()
