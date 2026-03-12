print("hello world")

historico = []

while True:
     print("Você desejaria realizar na calculadora?: ")
     print("1- Fazer conta | 2- Ver Histórico | 3- Sair")

     operacao = input("1")
     print("Escolha a operação que vai ser realizada: ")
     print("+ = Adicao | - = Subtracao | * = Multiplicacao | / = Divisao ")

     operacao = input()
          

     if operacao == "+":
          print("Insira o primeiro número: ")
          numero1 = float(input())
          print("Insira o segundo número: ")
          numero2 = float(input())
          print("O resultado da soma será de:")
          resultado = numero1+numero2
          print(resultado)
          historico.append(resultado)

     elif operacao == "-":
          print("Insira o primeiro número: ")
          numero1 = float(input())
          print("Insira o segundo número: ")
          numero2 = float(input())
          print("O resultado da subtração será de: ")
          resultado = numero1-numero2
          print(resultado)
          historico.append(resultado)

     elif operacao == "*":
          print("Insira o primeiro número: ")
          numero1 = float(input())
          print("Insira o segundo número: ")
          numero2 = float(input())
          print("O resultado da subtração será de: ")
          resultado = numero1*numero2
          print(resultado)
          historico.append(resultado)

     elif operacao == "/":
          print("Insira o primeiro número: ")
          numero1 = float(input())
          print("Insira o segundo número: ")
          numero2 = float(input())
          print("O resultado da subtração será de: ")
          resultado = numero1/numero2
          print(resultado)
          historico.append(resultado)

     elif operacao == "5":
          print("Histórico", historico)

     elif operacao == "0":
          print("Processo encerrado...")
          break

    

     
     


