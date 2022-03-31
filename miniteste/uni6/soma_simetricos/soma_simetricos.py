#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#Soma simétricos

def soma_simetricos(valores):
    segunda = []

    if len(valores) % 2 != 0:
        for i in range(((len(valores)) // 2) + 1):
            if i == ((len(valores)) // 2):
                segunda.append(valores[i])
            else:
                segunda.append(valores[i] + valores[-1 - i])

    elif len(valores) % 2 == 0:
        for i in range((len(valores)) // 2):
            segunda.append(valores[i] + valores[-1 - i])

    return segunda