import random


print('Qual tema gostaria de jogar?')
print("""    >>> [1]-Nomes
    >>> [2]-Frutas
    >>> [3]-Objetos""")
user_opt = int(input("Digite o número de sua escolha: "))
lista_palavras = list()


if user_opt == 1:
    #read file "nomes.txt"
    with open ('nomes.txt', 'r') as arquivo:
        for nomes in arquivo:
            nomes = nomes.rstrip()
            lista_palavras.append(nomes)


if user_opt ==2:
    #read file "fruta.txt"
    with open ('frutas.txt', 'r') as arquivo:
        for frutas in arquivo:
            frutas = frutas.rstrip()
            lista_palavras.append(frutas)


if user_opt == 3:
    #read file "objetos.txt"
    with open('objetos.txt', 'r') as arquivo:
        for objetos in arquivo:
            objetos = objetos.rstrip()
            lista_palavras.append(objetos)


#storage in a list and random the words
print()
palavra_secreta = random.choice(lista_palavras)
digitadas = list()


#main 
chances = 0
while True:
    print()
    letra = str(input('Digite uma letra: '))
    print(f'-' * 20)

    if len(letra) > 1:
        print('AAHH assim não vale, chute apenas uma letra: ')
        chances += 1
        print(f'Números de chances: {chances}')
        print(f'-' * 20)
        continue

    if chances >= 28:
        print('AAAAHHHHHHH, que pena!!! Você perdeu... :(')
        break

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'Uhuul!! A letra "{letra}" realmente existe na palavra secreta.')
        chances += 1
        print(f'Números de chances: {chances}')
        print(f'-' * 20)
    else:
        print(f'Ahhhh, que pena... A letra "{letra}" não existe na palavra secreta.')
        chances += 1
        print(f'Números de chances: {chances}')
        print(f'-' * 20)
        digitadas.pop()


    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavra_secreta:

        print(f'PARABENSSS!!! VOCÊ GANHOU COM {chances} CHANCES!!!')
        break
    else:
        print(secreto_temporario)

print(f'Palavara secreta: {palavra_secreta}')
