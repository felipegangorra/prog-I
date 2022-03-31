#Prog1 - UFCG - 19/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Calculando o valor do iptu com respectivos descontos.

#ENTRADA
area = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))

#CÁLCULO
iptu = area * aliquota + 35

desconto1 = iptu - ((iptu * 25) / 100)
desconto2 = iptu - ((iptu * 5) / 100)
desconto3 = iptu - ((iptu * 0) / 100)

parcela2 = desconto2 / 6
parcela3 = desconto3 / 10

#SAIDA
print(f'IPTU: R$ {iptu:.2f}\n')
print('Pagamento:')
print(f'1. Quota única. R$ {desconto1:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {desconto2:.2f}\n   6 x R$ {parcela2:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {desconto3:.2f}\n   10 x R$ {parcela3:.2f}')