def geraAptidao(individuo, prefA, prefB):
    aptidao = 0
    for i, j in enumerate(individuo):
        aptidao += prefA[i].index(j)
        aptidao += prefB[j].index(i)
    return aptidao

# Quanto menor a aptidão, melhor. O mínimo é 0 (todos na primeira posição)