opcao = ''
while opcao != 0:
  opcao = int(input("1 - sacar \n2 - extraton \n0 - sair\n "))

  if opcao == 1:
    print("sacando")
  elif opcao == 2:
    print("exibindo extrato ")

print("fim....")

num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))

----------------------------------------------------------------------------------------------------

ope = -24

while ope != 5:
  ope = int(input("[1] Adição\n[2] Subitração\n[3] Multiplicação\n[4] Divisão\n[5] Sair\n"))
  match ope:
    case 1:
      result = num1 + num2
      print(result)
    case 2:
      result = num1 - num2
      print(result)
    case 3:
      result = num1 * num2
      print(result)
    case 4:
      result = num1/num2
      print(result)
    case 5:
      print("FIM")
    case _:
      ope = 5
      print("opção invalida...FIM")


--------------------------------------------------------------------
i = 0
maior = 0
menor = 'w'

while i != 9:
  num = float(input("digite um numero: "))
  if menor == 'w':
    menor = num
  if num >= maior:
    maior = num
  if num < menor:
    num = menor

  i = i + 1

print(maior)
print(menor)


---------------------------------------------------------------------
i = 0
maior = 0
menor = 0

while i != 5:
  num = float(input("digite um numero: "))
  if i == 0:
    maior=num
    menor=num
  else:
    if num > maior:
      maior = num
    if num < menor:
      num = menor

  i = i + 1

print(maior)
print(menor)
