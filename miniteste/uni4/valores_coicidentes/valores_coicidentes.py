#Prog1 - UFCG - 17/FEV/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#Calculando valores coicidentes

lista_01 = input().split()
lista_02 = input().split()

if len(lista_01) and len(lista_02) > 0:
    if len(lista_01) > len(lista_02):
        contagem = len(lista_02)
    else: 
        contagem = len(lista_01)

    cont = 0
    for i in range(contagem):
        if int(lista_01[i]) == int(lista_02[i]):
            print(f"i = {i}: {lista_01[i]}") 
            cont += 1

    quantidade = (cont * 100) / (len(lista_01) + len(lista_02))

    print(f"Valores coincidentes: {cont} ({quantidade:.0f}%)")
    