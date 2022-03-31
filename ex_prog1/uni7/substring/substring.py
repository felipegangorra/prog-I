#Prog1 - 16/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084   
#SUBSTRING: verificando se uma string está em outra string

def is_sub(i, maior, menor):
    for i in range(1, len(menor)):
        if menor[i] == maior[i + 1]:
            if (i == len(menor) - 1):
                return True
            continue
        else: break

    return False


def is_substring(str1, str2):
    for i in range(len(str1)):
        if (str1[i] == str2[0]):
            if is_sub(i, str1, str2):
                return True
            else:
                continue
            
    return False