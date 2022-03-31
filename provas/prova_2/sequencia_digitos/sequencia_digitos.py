#Prog1 - 21/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#SEQUENCIA DE DIGITOS: verificando sequencia até parada

lista = (input())
limite = int(input())

soma = 0
num = 0
impar = 0
criterio = " "
while True:
    valor = int(lista[num])
    soma += valor
    num += 1

    if valor % 2 != 0:
        impar += 1
    if impar >= 6:
        criterio = ('6 ímpares')
        break
    elif soma > limite:
        criterio = ('limite')
        break
    elif num == len(lista):
        criterio = ('final da sequência')
        break

print(f'soma: {soma}')
print(f'números lidos: {num} de {len(lista)}')
print(f'critério de parada: {criterio}')


