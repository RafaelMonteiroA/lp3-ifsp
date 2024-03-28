# Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
import random

num = int(input("Digite um número de 1 a 100: "))
numSorteado = int(random.uniform(1,100))

if num == numSorteado:
    print("Parabénsssss!!!!! A chance disso acontecer era 1/100")
else:
    print(f"que pena, você escolheu {num}, mas o sorteado foi {numSorteado}")

# Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

tabuada = int(input("Digite um número para mostrar a tabuada do 1 ao 10: "))
for i in range(10):
    print(f"{tabuada} x {i+1} = {tabuada*(i+1)}")

# Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

frase = input("Digite uma frase: ")
vogais = 0
consoantes = 0
numerais = 0
espacos = 0

for letras in frase:
    match letras:
        case "a" | "e" | "i" | "o" | "u":
            vogais += 1
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            numerais += 1
        case " ":
            espacos += 1
        case _:
            consoantes += 1

print(f"vogais: {vogais}\nconsoantes: {consoantes}\nnumerais: {numerais}\nespaços: {espacos}")

# Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor.
Latorre = 0
Luk = 0
Motta = 0
Nulo = 0

print("Eleição Presidencial\n1 = Domingos Latorre\n2 = Luk Cho Man\n3 = Leonardo Motta")
for i in range(20):
    int = int(input(f"Voto {i+1}: "))
    match int:
        case 1:
            Latorre += 1
        case 2: 
            Luk += 1
        case 3:
            Motta += 1
        case _:
            Nulo += 1
    del int

if Latorre > Motta and Luk:
    print(f"Latorrreee presidenteeee!!!\nLatorre: {Latorre} votos\nLuk: {Luk} votos\nMotta: {Motta} votos\nNulo: {Nulo}")
elif Luk > Latorre and Motta:
    print(f"Lukkkkkkkk presidenteeee!!!\nLatorre: {Latorre} votos\nLuk: {Luk} votos\nMotta: {Motta} votos\nNulo: {Nulo}")
elif Motta > Luk and Latorre:
    print(f"Motttaaaaa presidenteeee!!!\nLatorre: {Latorre} votos\nLuk: {Luk} votos\nMotta: {Motta} votos\nNulo: {Nulo}")
else:
    print(f"Melhor refazer a votação!\nLatorre: {Latorre} votos\nLuk: {Luk} votos\nMotta: {Motta} votos\nNulo: {Nulo}")

# Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

frase = input("Digite uma frase sem pontuações: ")
frase = frase.replace(" ", "") and frase.lower()
palindromo = frase[::-1]

if frase == palindromo:
    print("é palindromoooooooo!!!")
else:
    print("não ééééé infelizmente.")

# Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns
    
nota = int(input("Digite a nota do aluno: "))

if nota < 60:
    print("Que feioooo, tirou F")
elif nota < 70:
    print("Tirou D, foi quase.")
elif nota < 80:
    print("Tirou C, ta na média")
elif nota < 90:
    print("Tirou B, ta quaseee lá")
else:
    print("Parabénssss!!!! Tirou A")

# Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

palavra = "Abacate"
letras_inseridas = []
chances = 7
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_inseridas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_inseridas.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True

    for letra in palavra:
        if letra.lower() not in letras_inseridas:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Manja muito de forca!! você ganhou, a palavra é: {palavra}")
else:
    print(f"Errrrouuuuuuuu!!! a palavra era: {palavra}")

# Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário.

def contar_palavras(texto):
    contagem_palavras = {}
    
    for palavra in texto:
        contagem_palavras[palavra] = texto.count(palavra)

    return contagem_palavras

texto = input("Digite uma frase: ")
print(contar_palavras(texto))
 
