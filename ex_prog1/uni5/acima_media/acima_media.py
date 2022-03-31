#Prog1 - UFCG - 2/mar/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#ACIMA DA MÉDIA:calculando meses acima da média de ocorrências.

media_geral = float(input())
sequencia = ""

while True:
    dados = input().split()
    
    if  dados[0] == 'fim': break
    
    ocorrencias = 0
    for i in dados:
        ocorrencias += int(i)
    media = (ocorrencias / len(dados)) 
    
    if (media * 2) < media_geral: break
    
    if media > media_geral:
        for i in range(len(dados)):
            if i == (len(dados)-1):
                sequencia += dados[i] + "\n"
            else:
                sequencia += dados[i] + " "

print(sequencia, end = "")