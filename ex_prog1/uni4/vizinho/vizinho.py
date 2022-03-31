#Prog1 - UFCG - 04/fevereiro/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#Programa que conta ocorrências em que vizinho da direita tem valor igual.

#ENTRADA
valores = input().split()

cont = 0

for x in range(len(valores)-1):        #pega quantidade de elementos mais seus indices -1 (pois ele iria comparar o ultimo indice mais um que não existe!)
    if int(valores[x]) == int(valores[x - 1]): #int para converter em inteiro elemento por elemento e '+1' para comparar com o proximo indice.
        cont += 1
    
print(cont)