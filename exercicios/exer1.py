def calcularTotalGol(gols):
    total = 0
    for gol in gols:
        total += gol
    return total

def calcularMediaGol(gols):
    total = calcularTotalGol(gols)
    return total / len(gols)

def encontrarArtilheiros(jogadores, gols):
    maior = gols[0]
    for gol in gols:
        if gol > maior:
            maior = gol

    artilheiros = []
    for i in range(len(jogadores)):
        if gols[i] == maior:
            artilheiros.append(jogadores[i])
    return artilheiros

def mostrarRelatorio(jogadores, gols):
    for i in range(len(jogadores)):
        print(jogadores[i], "-", gols[i], "gols")
    total = calcularTotalGol(gols)
    media = calcularMediaGol(gols)
    artilheiros = encontrarArtilheiros(jogadores, gols)
    print("Total de gols:", total)
    print("Média de gols:", media)
    print("Jogadores acima da média:")
    for i in range(len(jogadores)):
        if gols[i] > media:
            print(jogadores[i])
    if len(artilheiros) > 1:
        print("Empate na artilharia entre:", artilheiros)
    else:
        print("Artilheiro:", artilheiros[0])
jogadores = ["Lucas", "Gabriel", "Rafael", "Pedro", "André"]
gols = [4, 7, 2, 7, 5]

mostrarRelatorio(jogadores, gols)