#Prog1 - 16/FEV/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#LUCRO MENSAL: leia duas listas com receitas e despesas e veja o lucro.

receitas = []
despesas = []
MES = ["jan", "fev", "mar", "abr",
        "mai", "jun", "jul", "ago",
        "set", "out", "nov", "dez" ]

for i in range(12):         #12 pois são 12 meses
    linha = input().split()
    receita = float(linha[0]) #pega o 1 valor da entrada(linha)
    despesa = float(linha[1])  #pega o segundo
    receitas.append(receita)        #add valor na lista
    despesas.append(despesa)          #add valor na lista

lucros = []

for i in range(12):                 #add
    lucros.append(receitas[i] - despesas[i])

for i in range(12):
    print(f'{MES[i]} {lucros[i]:4.1f}')