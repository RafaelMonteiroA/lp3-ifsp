# Ex01 - Escreva um programa em Python que solicita ao usuário um número inteiro e apresenta seu antecessor e sucessor.

numero = int(input("Digite um número: "))
antecessor = numero-1
sucessor = numero+1
print(f"Antecessor de {numero} é {antecessor}, o sucessor é {sucessor}")

# Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

for i in range (3):
    num = int(input(f"Digite o {i+1}º número: "))
    num += num
media = num/i

print(f"A média aritmética é {media}")

# Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

valor_compra = float(input("Digite quanto você gastou nessa compra: "))

if valor_compra < 10.0:
    print(f"Sem desconto, {valor_compra}")
elif valor_compra < 100.0:
    valor_compra -= valor_compra*0.05
    print(f"Valor com desconto = {valor_compra}")
elif valor_compra < 500:
    valor_compra -= valor_compra*0.1
    print(f"Valor com desconto = {valor_compra}")
else:
    valor_compra -= valor_compra*0.15
    print(f"Valor com desconto = {valor_compra}")

# Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.
# Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

identificador = str(input("Digite seu código identificador: "))

def validando_identificador(identificador: str):

    if len(identificador) != 7:
        return False
    if not f"{identificador[0]}{identificador[1]}" == "BR":
        return False
    if not int(identificador[2:6]):
        return False
    if not identificador[len(identificador) - 1] == "X":
        return False

    return True

valido = "ta válido" if validando_identificador(identificador) else "não ta válido"

print (f"Seu código {valido}")

# Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações

comprimento = float(input("Digite o comprimento do aquário: "))
altura = float(input("Digite a altura do aquário: "))
largura = float(input("Digite a largura do aquário: "))
temperatura_desejada = float(input("Digite a temperatura desejada: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente: "))

def get_volume(comprimento, altura, largura):
    return (comprimento*altura*largura)/1000

volume = get_volume(comprimento, altura, largura)

def get_filtragem_ideal(volume):
    return 2*volume, 3*volume

def get_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume*0.05*(temperatura_desejada - temperatura_ambiente)

print(f"Volume: {volume}")
print(f"Filtragem mínima por hora: {get_filtragem_ideal(volume)[0]}Litros por hora a {get_filtragem_ideal(volume)[1]}Litros por hora")
print(f"Potência do termostato necessária: {get_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)}Watts")

# Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora em Python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

def get_IMC(peso, altura):
    return peso/altura**2

imc = get_IMC(peso, altura)

def get_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Excesso de peso"
    elif imc < 35.0:
        return "Obesidade de Classe 1"
    elif imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def get_peso_ideal(peso, altura):
    return peso-(24.9*altura*altura)

peso_ideal = get_peso_ideal(peso, altura)

print(f"IMC: {imc}")
print(f"Classificação: {get_classificacao(imc)}")

if peso_ideal >= 0.0:
    print(f"Você precisa perder {peso_ideal}Kg para atingir seu peso normal")
else:
    print(f"Você precisa ganhar {peso_ideal * -1}Kg para atingir seu peso normal")