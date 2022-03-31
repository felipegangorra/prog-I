#Prog1 - 23/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#MAIS VELHO PRIMEIRO: colocando em ordem!

def idosos_inicio(fila):
    ordem = 0
    for i in range(len(fila)):
        if fila[i] >= 60:
            guardado = fila[ordem]

            fila[ordem] = fila[i]
            fila[i] = guardado

            ordem += 1