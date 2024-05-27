import os
from random import choice

palavra_secreta = ['hylos', 'aurora', 'valir', 'gord', 'grock', 'estes', 'harley', 'kadita', 'badang', 'eldora', 'miya', 'cyclops', 'lesley', 'lolita', 'angela', 'saber', 'karrie', 'xborg', 'layla', 'bruno', 'jawhead', 'lancelot', 'zilong', 'akai', 'clint', 'yi-sun-shin', 'lapu-lapu', 'alucard', 'franco', 'hilda', 'odette', 'change', 'gusion', 'gatotkaca', 'freya', 'minsitthar', 'rafaela', 'tigreal', 'kaja', 'alice', 'argus', 'karina', 'helcurt', 'moskov', 'aldous', 'bane', 'balmond']
palavra_secreta_final = choice(palavra_secreta)
letras_acertadas = ''
numero_tentativas = 0
dica = 'É um personagem do mobile legends'
while True:
    print(dica)
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue
    
    if letra_digitada in palavra_secreta_final:
        letras_acertadas += letra_digitada
    palavra_formada = ''
    for letra_secreta in palavra_secreta_final:
        
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print("Palavra formada:", palavra_formada)
    if numero_tentativas < 20:
        if palavra_formada == palavra_secreta_final:
            os.system('cls')

            print("PARABÉNS, VOCÊ GANHOU!")
            print("A palavra secreta era:", palavra_secreta_final)
            print("Tentativas: ", numero_tentativas)
            letras_acertadas = ''
            numero_tentativas = 0
            palavra_secreta_final = choice(palavra_secreta)
            
    else:
        os.system('cls')
        print(f"Você excedeu o limite de 20 tentativas: {numero_tentativas}")
        print("Tente novamente!")
        letras_acertadas = ''
        numero_tentativas = 0
        palavra_secreta_final = choice(palavra_secreta)
