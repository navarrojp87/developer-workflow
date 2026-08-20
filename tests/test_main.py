from src.main import sumar, restar, multiplicar

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 4) == 12
