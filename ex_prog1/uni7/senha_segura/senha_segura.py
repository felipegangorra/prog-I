#Prog1 - 23/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#SENHA SEGURA: verificando se o num na é par na posição par, e ímpar na...

def senha_segura(senha):
    valor = []
    for i in senha:
        i = int(i)
        if (i % 2) == 0:
            valor.append('par')
        else:
            valor.append('impar')

    verificador = 0
    for i in range(len(valor)-1, -1, -1):
        if valor[i] == valor[i - 1]:
            verificador += 1
        else:
            continue

    if verificador == 0:
        return("Senha segura")
    else:
        return("Senha insegura")