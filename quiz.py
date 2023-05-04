print("Seja muito bem vindo ao Quiz do Sarmento!")
answer_user = input("Você deseja começar? (Sim/Não)")

if answer_user != "Sim":
    quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) EA \n (C) Activision \n (D) Ubisoft \n" )
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual o nome do ultimo Grand Theft Auto (GTA) produzido? \n (A) GTA San Andreas \n (B) GTA V \n (C) GTA IV \n (D) GTA Vice City \n" )
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual personagem do game GTA V tinha um cachorro? \n (A) Lamar \n (B) Trevor \n (C) Michael \n (D) Franklin \n" )
answer_3 = input("Resposta: ")

if answer_3 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual a cor do famoso carro do Trevor? \n (A) Verde \n (B) Vermelho \n (C) Amarelo \n (D) Preto \n" )
answer_4 = input("Resposta: ")

if answer_4 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual a data de lançamento do game GTA V? \n (A) 17 de setembro de 2015 \n (B) 17 de setembro de 2012 \n (C) 17 de setembro de 2013 \n (D) 17 de setembro de 2014 \n" )
answer_5 = input("Resposta: ")

if answer_5 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")
    

print(f"Fim do Quiz... Pontuação: {score}/5 ")



