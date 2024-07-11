import random 

nome = input("Qual seu nome?: ")
player_escolha = input("Digite sua escolha (pedra, papel, tesoura): ")
computador_escolha = random.choice(["pedra","papel", "tesoura"])

regras_de_vitoria = {
    "pedrapapel" : "papel", 
    "pedratesoura" : "pedra", 
    "papelpedra" : "papel", 
    "papeltesoura" : "tesoura", 
    "tesourapedra" : "pedra", 
    "tesourapapel" : "tesoura"

}

def cpu_escolha():
    print("O cpu escolheu", computador_escolha)

resultado = player_escolha + computador_escolha
vencedor = regras_de_vitoria.get(resultado)

if player_escolha == vencedor:
    print(f"{nome} Venceu!!")
    cpu_escolha()
elif computador_escolha == vencedor:
    print("CPU Venceu!")
    cpu_escolha()
else:
    print("EMPATE!!")
    cpu_escolha()

