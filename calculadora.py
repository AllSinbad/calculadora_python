def soma(n1, n2):
    return n1 + n2
     

def subt(n1, n2):
    return n1 - n2
     

def mult(n1, n2):
    return n1 * n2
     

def div(n1, n2):
    return n1 / n2
     
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

while True:
    operacao = int(input("""
Escolha uma operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair

Operação escolhida: """))
    match operacao:
        case 1:
            print(f"O resultado foi: {soma(n1=num1, n2=num2)}")
        case 2:
            print(f"O resultado foi: {subt(n1=num1, n2=num2)}")
        case 3:
            print(f"O resultado foi: {mult(n1=num1, n2=num2)}")
        case 4:
            print(f"O resultado foi: {div(n1=num1, n2=num2)}")
        case _:
            print("Opção inválida")
    
        