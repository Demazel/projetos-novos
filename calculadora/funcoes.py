def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro, nao posso dividir por zero"
    return num1 / num2

def raiz(num1, num2):
    if num2 < 0:
        return "Erro ao calcular"
    return num1 **(1/num2)

def potencia(num1, num2):
    return num1 ** num2