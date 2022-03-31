#Prog1 - 28/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#BUBBLESORT: tornando código funcional

def bubblesort(dados): 
    
    while True:
        swapped = False
        for i in range(len(dados) -1):
            if dados[i] > dados[i + 1]:
                aux = dados[i]
                dados[i] = dados[i + 1]
                dados[i + 1] = aux
                swapped = True
        if not swapped: break