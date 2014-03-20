from maxima import find_maxima

def test1():
    lista = [1, 2, 1]
    resultado_esperado = [1]
    resultado = find_maxima(lista)
    assert resultado == resultado_esperado


def test2():
    lista = [1, 2, 3, 2, 1]
    resultado_esperado = [2]
    resultado = find_maxima(lista)
    assert resultado == resultado_esperado


def test3():
    lista = [1, 2, 3]
    resultado_esperado = [2]
    resultado = find_maxima(lista)
    assert resultado == resultado_esperado


test1()
test2()
test3()
