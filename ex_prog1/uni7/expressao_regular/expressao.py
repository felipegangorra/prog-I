#Prog1 - 09/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#EXPRESSÃO REGULAR: verificando se A e B são corretos

def is_substring_expr(str1,str2):
    str2 = str2.split('*')
    primeiro = str2[0]
    segundo = str2[1]

    retorno = False
    for i in range(len(primeiro)):
        if primeiro[i] == str1[i]:
            retorno = True
        else: 
            retorno = False
            break

    if retorno == True:
        segundo = segundo[::-1]
        str1 = str1[::-1]

        for i in range(len(segundo)):
            if segundo[i] == str1[i]:
                retorno = True
            else:
                retorno = False
                break

    return retorno