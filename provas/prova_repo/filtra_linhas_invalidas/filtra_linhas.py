#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#FILTRA LINHAS INVALIDAS: filtra e exibe sequencias invalidas

num_linha = 1
sequencia = 0
invalidas = 0
while True:
    linha = input()
    linha_aux = linha.split()
    if linha == "fim": break
    
    par = 0
    impar = 0
    for i in linha_aux:
        i =  int(i)
        if i % 2 == 0:
            par += 1
        else:
            impar += 1

    if impar > par:
        print(f'linha {num_linha} inválida: {linha}')
        invalidas += 1
    
    num_linha += 1
    sequencia += 1

print(f'sequências lidas: {sequencia} (inválidas: {invalidas})')