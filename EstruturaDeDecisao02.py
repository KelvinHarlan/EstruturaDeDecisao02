# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('Digite um número (inteiro) positivo ou negativo\n'))

if numero >0:
    print(f'Você escolheu o número {numero}, ele é um número positivo!')
elif numero ==0:
    print(f'Você escolheu o número {numero}, ele é um número Neutro!')
else:
    print(f'Você escolheu o número {numero}, ele é um número Negativo!')
