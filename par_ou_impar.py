import random
import time
import os

# função do jogo de par ou ímpar
def par_ou_impar(player, player_choice, pc):
    print("Olá, seja bem vindo ao jogo de par ou ímpar!")
    time.sleep(2)
    print("Você jogará contra o computador, que escolherá um número aleatório entre 0 e 10.")
    time.sleep(3)
    print("Você deve escolher se quer par ou ímpar e um número entre 0 e 10.")
    time.sleep(3)
    print("Vamos começar!")
    time.sleep(2)
    player_choice = input("Escolha se você quer par ou ímpar (p/i): ").lower()
    if player_choice != "p" and player_choice != "i": # Verifica se a escolha do jogador é válida
        raise ValueError("Escolha inválida, digite 'p' para par ou 'i' para ímpar.")
    time.sleep(2)
    player = int(input("Agora, digite um número de 0 a 10: "))
    time.sleep(2)
    pc = random.randint(0,10) 
    print(f"A escolha do computador foi {pc}.")
    time.sleep(2)
    soma = player + pc # Calcula a soma dos valores escolhidos
    print(f"A soma dos valores escplhidos é: {soma}")
    time.sleep(2)
    # Verifica se o jogador venceu ou perdeu
    if (soma % 2 == 0 and player_choice == "p") or (soma % 2 != 0 and player_choice == "i"):
        print("Você venceu! Parabéns!")
        time.sleep(2)
    else:
        print("Você perdeu! Tente novamente.")
        time.sleep(2)
    return player, player_choice, pc

# função para iniciar o jogo
def iniciar_jogo(): 
    print(par_ou_impar)
    time.sleep(2)
    print("Obrigado por jogar!")
while True: # Loop para reiniciar o jogo
    player = 0
    player_choice = ""
    pc = 0
    par_ou_impar(player, player_choice, pc)
    
    continuar = input("Deseja jogar novamente? (s/n) ").lower()
    if continuar != "s":
        print("Obrigado por jogar! Até a próxima!")
        break
    
    time.sleep(2)
    print("Reiniciando o jogo...")
    time.sleep(2)
    print("Vamos lá!")
    time.sleep(2)
    print("Lembre-se que você deve escolher entre par ou ímpar e um número entre 0 e 10.")
    time.sleep(2)
    print("Boa sorte!")
    time.sleep(2)
    os.system('cls') # Limpa a tela do terminal
