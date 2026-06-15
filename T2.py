from Genetico import (
    popula,
    ordena,
    getMediaAptidao,
    selecaoTorneio,
    selecaoRodaDaRoleta,
    crossover,
    mutacao,
    novaGeracao,
    AG,
    geraAptidao,
)


def lerArquivo(caminho):
    with open(caminho, "r") as f:
        linhas = [l.strip() for l in f if l.strip()]

    n = int(linhas[0])

    prefA = []
    for i in range(1, n + 1):
        valores = linhas[i].split()
        prefA.append([int(x) - 1 for x in valores[1:]])

    prefB = []
    for i in range(n + 1, 2 * n + 1):
        valores = linhas[i].split()
        prefB.append([int(x) - 1 for x in valores[1:]])

    return n, prefA, prefB


def imprimirPreferencias(n, prefA, prefB):
    print(f"Número de duplas: {n}\n")

    print("Preferências da Escola A:")
    for i, prefs in enumerate(prefA):
        ordem = " > ".join(f"B{j+1}" for j in prefs)
        print(f"  A{i+1}: {ordem}")

    print("\nPreferências da Escola B:")
    for j, prefs in enumerate(prefB):
        ordem = " > ".join(f"A{i+1}" for i in prefs)
        print(f"  B{j+1}: {ordem}")


import sys
import os

caminho = sys.argv[1] if len(sys.argv) > 1 else os.path.join("ArquivosDeLeitura", "exemplo1.txt")

print("TESTE: lerArquivo")
n, prefA, prefB = lerArquivo(caminho)
imprimirPreferencias(n, prefA, prefB)


print("\nTESTE: popula")
populacao = popula(5, n)
for i, ind in enumerate(populacao):
    print(f"  Individuo {i}: {[j+1 for j in ind]}")


print("\nTESTE: geraAptidao")
aptidoes = [geraAptidao(ind, prefA, prefB) for ind in populacao]
for i, (ind, apt) in enumerate(zip(populacao, aptidoes)):
    print(f"  Individuo {i}: {[j+1 for j in ind]} -> aptidao: {apt}")


print("\nTESTE: ordena")
populacao, aptidoes = ordena(populacao, aptidoes)
for i, (ind, apt) in enumerate(zip(populacao, aptidoes)):
    print(f"  [{i}] {[j+1 for j in ind]} -> aptidao: {apt}")
print(
    f"  Melhor: {aptidoes[0]} | Média: {getMediaAptidao(aptidoes):.2f} | Pior: {aptidoes[-1]}"
)


print("\nTESTE: selecaoTorneio")
for _ in range(3):
    selecionado = selecaoTorneio(populacao, aptidoes)
    print(f"  Selecionado: {[j+1 for j in selecionado]}")


print("\nTESTE: selecaoRodaDaRoleta")
for _ in range(3):
    selecionado = selecaoRodaDaRoleta(populacao, aptidoes)
    print(f"  Selecionado: {[j+1 for j in selecionado]}")


print("\nTESTE: crossover")
pai1 = populacao[0]
pai2 = populacao[1]
filhos = crossover(pai1, pai2)
print(f"  Pai1:   {[j+1 for j in pai1]}")
print(f"  Pai2:   {[j+1 for j in pai2]}")
print(f"  Filho1: {[j+1 for j in filhos[0]]}")
print(f"  Filho2: {[j+1 for j in filhos[1]]}")


print("\nTESTE: mutacao")
ind = populacao[0][:]
print(f"  Antes:  {[j+1 for j in ind]}")
ind = mutacao(ind, 1.0)
print(f"  Depois: {[j+1 for j in ind]}")


print("\nTESTE: novaGeracao")
populacao, aptidoes = novaGeracao(
    populacao, aptidoes, prefA, prefB, 0.8, 0.15, True, "torneio"
)
print(
    f"  Melhor: {aptidoes[0]} | Média: {getMediaAptidao(aptidoes):.2f} | Pior: {aptidoes[-1]}"
)


print("\nTESTE: AG (10 gerações)")
melhorIndividuo, melhorAptidao, historico = AG(
    prefA, prefB, tamPopulacao=10, numeroMaximoGeracoes=10, passoPasso=False
)
print(f"\n  Melhor individuo: {[j+1 for j in melhorIndividuo]}")
print(f"  Melhor aptidao:   {melhorAptidao}")