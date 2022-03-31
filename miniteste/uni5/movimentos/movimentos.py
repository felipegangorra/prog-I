#Prog1 - UFCG - 24/FEV/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#MOVIMENTOS: determinando posição no tabuleiro.

inicial = input().split()
coluna = int(inicial[0])
linha = int(inicial[1])

cont = 0
while True:
    entrada = input()

    if entrada == 'X': break
    else:
        movimento = entrada.split()
        lado = str(movimento[0])
        numero = int(movimento[1])

        if lado == 'E':
            linha = linha - numero
        if lado == 'D':
            linha = linha + numero
        if lado == 'B':
            coluna = coluna + numero
        if lado == 'C':
            coluna = coluna - numero
        cont += numero

        print(f'> {coluna} {linha}')

print(cont)