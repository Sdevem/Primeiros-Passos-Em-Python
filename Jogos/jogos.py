import forca
import divination

print("***************************")
print("****Escolha o seu Jogo!****")
print("***************************")

print("(1) forca (2) Advinhação")

jogo = int(input("Qual Jogo?"))

if(jogo == 1):
    print("Você escolheu o jogo da forca")
    forca.play()
else:
    print("Você escolheu o jogo de Advinhação")
    divination.play()
    
