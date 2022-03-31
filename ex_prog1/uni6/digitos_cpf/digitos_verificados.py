#Prog1 - UFCG - 2/mar/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#Dígitos Verificados do CPF

def calcula_digitos_verificacao(cpf):

    lista = []
    d1_lista = []
    d2_lista = []
    d1 = 0
    d2 = 0

    if d1 == 0:
        x = 0
        num = 2
        soma = 0

        for i in range(len(cpf.split())):
            for i in cpf:
                lista.append(int(i))
                d1_lista = lista[::-1]

            for i in d1_lista:
                x = i * num
                soma += x
                num += 1

            d1 = (10 * soma) % 11
            if d1 == 10:
                d1 = 0

    if d2 == 0:
        x = 0
        num = 2
        soma = 0

        #DIGITO 2
        d2_lista = lista.append(d1)
        d2_lista = lista[::-1]

        for i in d2_lista:
            x = i * num
            soma += x
            num += 1

        d2 = (10 * soma) % 11
        if d2 == 10:
            d2 = 0

    resultado = str(d1) + str(d2)
    return resultado

    