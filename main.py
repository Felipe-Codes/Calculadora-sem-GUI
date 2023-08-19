def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

def power(x, y):
    return x ** y

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return "Erro: Divisão por zero"

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Resto da Divisão (Módulo)")

    choice = input("Digite a opção (1/2/3/4/5/6): ")

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Opção inválida")
        return

    num1_input = input("Digite o primeiro número: ")
    num2_input = input("Digite o segundo número: ")

    if not (num1_input.isnumeric() or num1_input.replace('.', '', 1).isnumeric()):
        print("Erro: O primeiro número não é válido")
        return
    if not (num2_input.isnumeric() or num2_input.replace('.', '', 1).isnumeric()):
        print("Erro: O segundo número não é válido")
        return

    num1 = float(num1_input)
    num2 = float(num2_input)

    if choice == '1':
        print("Resultado:", add(num1, num2))
    elif choice == '2':
        print("Resultado:", subtract(num1, num2))
    elif choice == '3':
        print("Resultado:", multiply(num1, num2))
    elif choice == '4':
        print("Resultado:", divide(num1, num2))
    elif choice == '5':
        print("Resultado:", power(num1, num2))
    elif choice == '6':
        print("Resultado:", modulo(num1, num2))

calculator()
