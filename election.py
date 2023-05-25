
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidatos  = {"inácio":13,"Jair":17,"henrique":98,"michel":15}

#print(candidatos.get("inácio")) #get: insert the key, and you'll be returned the value
#print(candidatos["inácio"])
eleitores = []
def voto():
    print("--------Votação Iniciada------------")
    nome = input("Digite seu Nome: ")
    idade = input("Digite sua Idade: ")
    candidatoNumero = input("Digite o numero do seu Candidato: ")
    for i,k in candidatos:
        if candidatos[i][0] == candidatoNumero:
            candidatoNome = candidatos[i]
            confirma = input("Candidato: {}\n Número: {}\n Deseja confirmar Voto? 'True' para confirmar e 'False' para limpar".format(candidatoNome,candidatoNumero))

voto()