#Prog1 - UFCG - 14/fevereiro/2022
#Aluno: Felipe da Silva Gangorra - 121111084   
#calculando dois ultimos valores de uma sequencia

numero = int(input())
lista = []
soma_media = 0


for i in range(numero):
    numero = int(input())
    lista.append(numero)

for i in lista:
    soma_media += i

media = int(soma_media / len(lista))

cont = 0
soma = 0

for i in range(len(lista)-1,0,-1):
    if cont >= 1:break
    elif lista[i] >= media:
        soma += lista[i]
        cont += 1
    else:
        soma += lista[i]
    
print(soma)


        