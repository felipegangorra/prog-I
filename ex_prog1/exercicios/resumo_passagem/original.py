#Prog1 - 16/FEV/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#RESUMO PASSAGEM: programa que imprima cartões de embarque.

identificador = str(input())
horario = str(input())
assento = str(input())
portao = str(input())
preco_sem_imposto = float(input())
preco_total = float(input())

#porcentagem_de_imposto = ((preco_total - preco_sem_imposto) * 100) / preco_total
porcentagem_de_imposto = preco_total - ((preco_total * preco_sem_imposto) / 100)

print('### Cartão de Embarque ###')
print('Identificador do voo: {}'.format(identificador))
print('Horário: {}'.format(horario))
print('Assento: {}'.format(assento))
print('Portão: {}'.format(portao))
print('Total de Imposto: {}%'.format(porcentagem_de_imposto))
