#Prog1 - 30/mar/2022 - UFCG
#Aluno: Felipe da Silva Gangorra - 121111084
#SOMAR SIMÉTRICOS: retorne soma dos valores que ocupam posições simétricas.

def soma_simetricos(valores):

    lista_soma = []
    if len(valores) % 2 != 0:
        for i in range(((len(valores)) // 2) + 1):
            if i == ((len(valores)) // 2):
                lista_soma.append(valores[i])
            else:
                lista_soma.append(valores[i] + valores[-1 - i])

    elif len(valores) % 2 == 0:
        for i in range((len(valores)) // 2):
            lista_soma.append(valores[i] + valores[-1 - i])

    return lista_soma


def test_1():
    assert soma_simetricos([10, 50, 100, 100, 50, 10]) == [20, 100, 200]

def test_2():
    assert soma_simetricos([1, 1, 1, 1]) == [2, 2]

def test_3():
    assert soma_simetricos([0]) == [0]

def test_4():
    assert soma_simetricos([]) == []

def test_5():
    assert soma_simetricos([2, 5, 3, 5, 2]) == [4, 10, 3]

