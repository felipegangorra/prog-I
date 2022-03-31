#Prog1 - 16/FEV/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#RESUMO PASSAGEM: programa que imprima cartões de embarque.

#ENTRADA
identificador = input()
horario = input()
assento = input()
portao = input()
preco_sem_imposto = float(input())
preco_total = float(input())

#CÁLCULO
total_imposto = ((preco_total - preco_sem_imposto) * 100) / preco_total

#SAÍDA
print('### Cartão de Embarque ###')
print(f'Identificador do voo: {identificador}')
print(f'Horário: {horario}')
print(f'Assento: {assento}')
print(f'Portão: {portao}')
print(f'Total de Imposto: {total_imposto:.1f}%')