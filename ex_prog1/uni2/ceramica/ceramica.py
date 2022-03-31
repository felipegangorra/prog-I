#Prog1 - UFCG - 18/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando quantidade de caixas para um determinado espaço.

#Entrada
revestimento = float(input('Capacidade de revestimento? '))

#Visualização
print('\n== Dados do vão a revestir ==')
comprimento = float(input(('Comprimento? ')))
largura = float(input(('Largura? ')))
altura = float(input(('Altura? ')))

#Calculo
area = (2 * ((largura * altura) + (comprimento * altura))) + (comprimento * largura)
caixas = area / revestimento

#Saida
print('\n== Resultados ==')
print(f'Área total a revestir: {area:.1f} m2')
print(f'Número de caixas: {caixas:.0f}')