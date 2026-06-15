import random
from Fitness import geraAptidao


def popula(tamPopulacao, n):
    populacao = []
    base = list(range(n))
    for _ in range(tamPopulacao):
        individuo = base[:]
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao


def ordena(populacao, aptidoes):
    pares = sorted(zip(aptidoes, populacao), key=lambda x: x[0])
    aptidoesOrd = [p[0] for p in pares]
    populacaoOrd = [p[1] for p in pares]
    return populacaoOrd, aptidoesOrd


def getMediaAptidao(aptidoes):
    return sum(aptidoes) / len(aptidoes)


def selecaoTorneio(populacao, aptidoes, k=3):
    populacaoIntermediaria = random.sample(range(len(populacao)), k)
    populacaoIntermediaria = sorted(populacaoIntermediaria, key=lambda i: aptidoes[i])
    if random.random() < 0.9:
        pos = 0
    else:
        pos = 1
    return populacao[populacaoIntermediaria[pos]][:]


def selecaoRodaDaRoleta(populacao, aptidoes):
    maxAptidao = max(aptidoes)
    individuosTemp = [maxAptidao - apt + 1 for apt in aptidoes]
    aptidaoAcumulada = sum(individuosTemp)

    ponteiro = random.random() * aptidaoAcumulada
    acumulado = 0
    for i, apt in enumerate(individuosTemp):
        acumulado += apt
        if acumulado >= ponteiro:
            return populacao[i][:]
    return populacao[-1][:]


def crossover(pai1, pai2):
    n = len(pai1)
    pontoCorte = sorted(random.sample(range(n), 2))
    a, b = pontoCorte[0], pontoCorte[1]

    def ox(p1, p2):
        filho = [None] * n
        filho[a : b + 1] = p1[a : b + 1]
        segmento = set(p1[a : b + 1])
        pos = (b + 1) % n
        for gene in p2[b + 1 :] + p2[: b + 1]:
            if gene not in segmento:
                filho[pos] = gene
                pos = (pos + 1) % n
        return filho

    filhos = [ox(pai1, pai2), ox(pai2, pai1)]
    return filhos


def mutacao(individuo, taxaDeMutacao):
    if random.random() < taxaDeMutacao:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo


def novaGeracao(populacao, aptidoes, prefA, prefB, taxaDeCrossover, taxaDeMutacao, elitismo, tipoSelecao):
    tamPopulacao = len(populacao)
    novaPopulacao = []

    if elitismo:
        novaPopulacao.append(populacao[0][:])

    while len(novaPopulacao) < tamPopulacao:
        pais = [None, None]

        if tipoSelecao == "torneio":
            pais[0] = selecaoTorneio(populacao, aptidoes)
            pais[1] = selecaoTorneio(populacao, aptidoes)
        else:
            pais[0] = selecaoRodaDaRoleta(populacao, aptidoes)
            pais[1] = selecaoRodaDaRoleta(populacao, aptidoes)

        if random.random() <= taxaDeCrossover:
            filhos = crossover(pais[0], pais[1])
        else:
            filhos = [pais[0][:], pais[1][:]]

        filhos[0] = mutacao(filhos[0], taxaDeMutacao)
        filhos[1] = mutacao(filhos[1], taxaDeMutacao)

        novaPopulacao.append(filhos[0])
        if len(novaPopulacao) < tamPopulacao:
            novaPopulacao.append(filhos[1])

    novasAptidoes = [geraAptidao(ind, prefA, prefB) for ind in novaPopulacao]
    novaPopulacao, novasAptidoes = ordena(novaPopulacao, novasAptidoes)
    return novaPopulacao, novasAptidoes


def AG(
    prefA,
    prefB,
    tamPopulacao=50,
    numeroMaximoGeracoes=500,
    taxaDeCrossover=0.8,
    taxaDeMutacao=0.15,
    elitismo=True,
    tipoSelecao="torneio",
    semMelhoraLimit=100,
    passoPasso=False,
):
    n = len(prefA)
    populacao = popula(tamPopulacao, n)
    aptidoes = [geraAptidao(ind, prefA, prefB) for ind in populacao]
    populacao, aptidoes = ordena(populacao, aptidoes)

    melhorIndividuo = populacao[0][:]
    melhorAptidao = aptidoes[0]

    historico = [(melhorAptidao, getMediaAptidao(aptidoes), aptidoes[-1])]

    geracao = 1
    semMelhora = 0

    _log(geracao, aptidoes)
    if passoPasso:
        input("  [Enter para continuar...]")

    while geracao < numeroMaximoGeracoes:
        geracao += 1

        populacao, aptidoes = novaGeracao(
            populacao,
            aptidoes,
            prefA,
            prefB,
            taxaDeCrossover,
            taxaDeMutacao,
            elitismo,
            tipoSelecao,
        )

        historico.append((aptidoes[0], getMediaAptidao(aptidoes), aptidoes[-1]))

        if aptidoes[0] < melhorAptidao:
            melhorAptidao = aptidoes[0]
            melhorIndividuo = populacao[0][:]
            semMelhora = 0
        else:
            semMelhora += 1

        _log(geracao, aptidoes)
        if passoPasso:
            input("  [Enter para continuar...]")

        if melhorAptidao == 0:
            print("  SOLUÇÃO ÓTIMA ENCONTRADA!")
            break

        if semMelhora >= semMelhoraLimit:
            print(f"  Parado por {semMelhoraLimit} gerações sem melhora.")
            break

    return melhorIndividuo, melhorAptidao, historico


def _log(geracao, aptidoes):
    med = getMediaAptidao(aptidoes)
    pior = aptidoes[-1]
    print(
        f"  Geração {geracao:4d} | Melhor: {aptidoes[0]:4d} | Média: {med:6.2f} | Pior: {pior:4d}"
    )