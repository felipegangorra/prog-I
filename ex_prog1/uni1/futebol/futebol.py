#Programação 1 - UFCG - 15/dezembro/2021
#Aluno: Felipe da Silva Gangorra
#Calculando área de acordo com a medição de campos de futebol. 3 entradas!

area1 = float(input())
area2 = float(input())
area3 = float(input())

campo1 = area1 / 4000
campo2 = area2 / 4000
campo3 = area3 / 4000
media = (campo1 + campo2 + campo3) / 3

print(f'{campo1:.2f}')
print(f'{campo2:.2f}')
print(f'{campo3:.2f}')
print(f'{media:.2f}')