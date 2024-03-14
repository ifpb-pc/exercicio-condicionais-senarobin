def q1():
    """
    1. Escreva um programa que solicita um número ao usuário e determina se 
    é positivo, negativo ou zero. 
    """
    n = int(input("Digite um numero"))
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("zero")

def q2():
    """
    2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário 
    um número e imprima se ele é par ou ímpar.
    """
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        print('par')
    else:
        print('ímpar')
def q3():
    """
    3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois 
    números e uma operação (+, -, *, /) e imprima o resultado dessa operação.
    """
    n = float(input('Digite um número: '))
    n_dois = float(input('Digite outro número: '))

    op = input('Digite uma operação. Ex.: +, -, *, /: ')

    if op == '+':
        print(n + n_dois)
    elif op == '-':
        print(n - n_dois)
    elif op == '*':
        print(n * n_dois)
    elif op == '/':
        print(n / n_dois)

def q4():
    """
    4. Maior de Três Números: Escreva um programa que solicita três números 
    ao usuário e imprima o maior dentre eles.
    """
    n = float(input('Digite um número: '))
    n_dois = float(input('Digite outro número: '))
    n_tres = float(input('Digite mais um número: '))

    if n > n_dois and n > n_tres:
        print(n)
    elif n_dois > n and n_dois > n_tres:
        print(n_dois)
    else:
        print(n_tres)


def q5():
    """
    5. Classificação de Idade: Peça a idade do usuário e imprima a classificação
    em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
    """
    idade = int(input('Digite sua idade: '))

    if idade >= 0 and idade <= 12:
        print('Criança')
    elif idade >= 13 and idade <= 19:
        print('Adolescente')
    elif idade >= 20 and idade <= 59:
        print('Adulto')
    elif idade > 60:
        print('Idoso')

def q6():
    """
    6. Verificação de Triângulo: Peça ao usuário o comprimento de três 
    lados e verifique se eles podem formar um triângulo. Se sim, determine 
    se é um triângulo equilátero, isósceles ou escaleno.
    """
    medida_um = int(input('Digite o primeiro comprimento: '))
    medida_dois = int(input('Digite o segundo comprimento: '))
    medida_tres = int(input('Digite o terceiro comprimento: '))

    if medida_um + medida_dois < medida_tres or medida_dois + medida_tres < medida_um or medida_um + medida_tres < medida_dois:
        print('Inválido')
    else:
        if medida_um == medida_dois == medida_tres:
            print('Equilátero')
        elif medida_um == medida_dois != medida_tres or medida_um == medida_tres != medida_dois or medida_dois == medida_tres != medida_um:
            print('Isósceles')
        elif medida_um != medida_dois != medida_tres:
            print('Escaleno')

def q7():
    """
    7. Conversão de Notas: Escreva um programa que converte uma nota 
    de 0 a 100 em uma escala de conceitos: 
    A (90-100), B (80-89), C (70-79), D (60-69), E (50-59).e F (0-49)
    """
    nota = float(input('Digite sua nota de 0 a 100: '))

    if nota >= 90 and nota <=100:
        print('A')
    elif nota >= 80 and nota <= 89:
        print('B') 
    elif nota >= 70 and nota <= 79:
        print('C')
    elif nota >= 60 and nota <= 69:
        print('D') 
    elif nota >= 50 and nota <= 59:
        print('E')
    elif nota >= 0 and nota <= 49:
        print('F') 
def q8():
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    nome_user = input('Digite seu nome de usuário: ')
    senha = int(input('Digite sua senha: '))

    if nome_user == 'admin' and senha == 12345:
        print('Acesso concedido')
    else:
        print('Acesso negado')
def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obesa ou Muito obesa.
    """
    altura = float(input('Qual é a sua altura: '))
    peso = float(input('Qual o seu peso: '))

    imc = peso / (altura**2)

    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc and imc <= 24.9:
        print('Peso normal')
    elif 25 <= imc and imc <= 29.9:
        print('Sobrepeso')
    elif 30 <= imc and imc <= 34.9:
        print('Obeso')
    elif 35 <= imc and imc <= 40: 
        print('Muito obeso')


def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """
    ano = int(input('Digite um ano: '))

    if ano % 4 == 0 and ano % 100 != 0:
        print('bissexto')
    elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        print('bissexto')
    else:
        print('não')