#Prog1 - UFCG - 23/fev/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#MAIS CONSOANTES: programa que determina o número de consoantes a mais que vogais.

contagem = 0
while True:
    palavra = input()
    contagem += 1

    vogais = 0
    consoantes = 0
    for i in palavra:
        if i in "aeiouAEIOU":
            vogais += 1
        else:
            consoantes += 1
    
    if consoantes > vogais: break

print(contagem)
