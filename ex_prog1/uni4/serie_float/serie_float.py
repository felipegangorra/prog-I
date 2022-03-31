#Prog1 - UFCG - 22/dezembro/2021
#Aluno: Felipe Gangorra - 121111084
#Imprimindo números em sequência.

valor = 15.2                    #valor inicial da serie
tamanho = ((-5.8) - 15.2) // (-1.5) + 1     #cálculo: contagem de elementos (15)

for x in range(int(tamanho)):               #converte para int pois renga só aceita int
    print(f'{valor:.1f}')                   #printa o valor
    valor -= 1.5                            #pega o valor e subtrai -1.5, depois continua o laço!

