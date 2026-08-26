#!/usr/bin/env python3

def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def mutiplicar(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "erro"
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def raiz(num1, num2):
    if num2 == 0:
        return "erro"
    return num1 ** (1/num2)




# Primeiro numero
while True:
    try:
        num1 = float(input("\nPrimeiro número: "))
        break  
    except ValueError:
        print("Erro: Digite apenas números! Tente novamente.")


# Operação
menu_operacao = """
Escolha a operação aritmética:
- Soma (+) ou (soma)
- Multiplicação (x ou * ou multiplicacao)
- Subtração (-) ou (subtracao)
- Divisão (/) ou (divisao)
- Potência (**) ou (potencia)
- Raiz (v) ou (raiz)
"""

operacoes_aceitas = [
    "soma", "+", 
    "subtracao", "-", 
    "multiplicacao", "x", "*", 
    "divisao", "/", 
    "potencia", "**", 
    "raiz", "v"
]

while True:
    print(menu_operacao)
    operacao = input("Operação: ").lower().strip()
    operacao = operacao.replace("ã", "a").replace("ê", "e").replace("ç", "c")

    if operacao in operacoes_aceitas:
        break  
    else:
        print("\n[ERRO] Operação inválida! Escolha uma opção da lista.\n")


# Segundo numero
while True:
    try:
        num2 = float(input("\nSegundo número: "))
        break  
    except ValueError:
        print("Erro: Digite apenas números! Tente novamente.")


# Calculo
if operacao == "soma" or operacao == "+":
    resposta = soma(num1, num2)
elif operacao == "subtracao" or operacao == "-":
    resposta = subtrair(num1, num2)
elif operacao == "multiplicacao" or operacao == "x" or operacao == "*":
    resposta = mutiplicar(num1, num2)
elif operacao == "divisao" or operacao == "/":
    resposta = divisao(num1, num2)
elif operacao == "potencia" or operacao == "**":
    resposta = potencia(num1, num2)
elif operacao == "raiz" or operacao == "v":
    resposta = raiz(num1, num2)


# Resposta
if resposta == "erro":
    print("\nErro: Não é possível dividir por zero ou usar índice zero na raiz.")
elif isinstance(resposta, (int, float)):
    if float(resposta).is_integer():
        print(f"\nSua resposta é {int(resposta)}")
    else:
        print(f"\nSua resposta é {float(resposta):.2f}")
