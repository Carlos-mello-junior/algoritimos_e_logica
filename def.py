def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def mult(num1, num2):
    return num1 * num2

def interface():
    while True:       
        print('1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Sair')
        op = float(input('escolha uma opção: '))
        if op == 5:
            print('Saindo...')
            break
        num1 = float(input('numero 1: '))
        num2 = float(input('numero 2: '))

        match op: 
            case 1:
                print('A soma é: ', soma(num1, num2))
            case 2:
                print('A subtração é: ', sub(num1, num2))
            case 3:
                print('A divisão é: ', div(num1, num2))
            case 4:
                print('A multiplicação é: ', mult(num1, num2))

interface()