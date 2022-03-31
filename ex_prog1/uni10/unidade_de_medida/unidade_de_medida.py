#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#UNIDADE DE MEDIDA: convertendo medidas


medida = {'km': 1000, 'hm': 100, 'dam': 10, 'm': 1, 'dm': 0.1, 'cm': 0.01, 'mm': 0.001}

while True:
    lista = input().split()
    if int(lista[0]) + int(lista[2]) == 0: break

    convertido = (int(lista[0]) * medida[lista[1]]) + (int(lista[2]) * medida[lista[3]])
    print(f'{convertido:.2f} m')