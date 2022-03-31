#Prog1 - 04/fevereiro/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#Escreva um programa que verifica se um elemento está contido em uma lista de inteiros.

#ENTRADA    

inteiro = int(input())
sequencia = str(input())

lista = sequencia.split()               #transformar string em uma lista
cont = 0                                #contagem começa de 0

for x in lista:
    valor = int(x)                         #converter string em inteiro!
    if inteiro == valor:
        cont += 1                              #contar mais um caso tenha o valor igual
    
if cont != 0:                                   #se a contagem for diferente de zero então há o número dentro da lista!
    print('sim')
else:
    print('não')