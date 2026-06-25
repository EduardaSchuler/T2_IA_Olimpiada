# EXEMPLOS PRÁTICOS DE CÁLCULO DE APTIDÃO

## 📊 Exemplo 1: Cálculo Simples (2 Alunos)

### Dados
```
Preferências:

Escola A:
  A1 prefere: [B1, B2]
  
Escola B:
  B1 prefere: [A2, A1]
  B2 prefere: [A1, A2]
```

### Solução Codificada
```
Individuo = [1, 0]

Significado:
  A1 ↔ B2 (índice 1)
  A2 ↔ B1 (índice 0)
```

### Cálculo de Aptidão Passo-a-Passo

**DUPLA 1: A1 ↔ B2**

Pergunta 1: Qual posição B2 tem na lista de preferências de A1?
```
A1 prefere: [B1, B2]
            [0,  1]  ← índices
B2 está na posição 1
Contribuição de A1: 1
```

Pergunta 2: Qual posição A1 tem na lista de preferências de B2?
```
B2 prefere: [A1, A2]
            [0,  1]  ← índices
A1 está na posição 0
Contribuição de B2: 0
```

Subtotal dupla 1: 1 + 0 = **1**

---

**DUPLA 2: A2 ↔ B1**

Pergunta 1: Qual posição B1 tem na lista de preferências de A2?
```
A2 prefere: [B2, B1]
            [0,  1]  ← índices
B1 está na posição 1
Contribuição de A2: 1
```

Pergunta 2: Qual posição A2 tem na lista de preferências de B1?
```
B1 prefere: [A2, A1]
            [0,  1]  ← índices
A2 está na posição 0
Contribuição de B1: 0
```

Subtotal dupla 2: 1 + 0 = **1**

---

### Resultado Final
```
Aptidão Total = 1 + 1 = 2

Interpretação: Solução EXCELENTE (aptidão < 10)
```

---

## 📊 Exemplo 2: Cálculo com 4 Alunos (Como no Projeto)

### Dados do exemplo1.txt
```
Preferências:

Escola A:
  A1 prefere: B1 > B2 > B4 > B3  (índices: [0, 1, 3, 2])
  A2 prefere: B2 > B3 > B1 > B4  (índices: [1, 2, 0, 3])
  A3 prefere: B4 > B1 > B3 > B2  (índices: [3, 0, 2, 1])
  A4 prefere: B3 > B1 > B2 > B4  (índices: [2, 0, 1, 3])

Escola B:
  B1 prefere: A3 > A2 > A4 > A1  (índices: [2, 1, 3, 0])
  B2 prefere: A3 > A2 > A4 > A1  (índices: [2, 1, 3, 0])
  B3 prefere: A2 > A4 > A3 > A1  (índices: [1, 3, 2, 0])
  B4 prefere: A1 > A3 > A4 > A2  (índices: [0, 2, 3, 1])
```

### Solução Proposta
```
Individuo = [2, 0, 3, 1]

Significado:
  Posição 0: A1 ↔ B3 (índice 2)
  Posição 1: A2 ↔ B1 (índice 0)
  Posição 2: A3 ↔ B4 (índice 3)
  Posição 3: A4 ↔ B2 (índice 1)
```

### Cálculo Completo

**DUPLA 1: A1 ↔ B3**

```
A1 prefere: [B1, B2, B4, B3]  com índices [0, 1, 3, 2]
            B3 está na posição 3
            Contribuição A1 = 3

B3 prefere: [A2, A4, A3, A1]  com índices [1, 3, 2, 0]
            A1 está na posição 3
            Contribuição B3 = 3

Subtotal: 3 + 3 = 6
```

**DUPLA 2: A2 ↔ B1**

```
A2 prefere: [B2, B3, B1, B4]  com índices [1, 2, 0, 3]
            B1 está na posição 2
            Contribuição A2 = 2

B1 prefere: [A3, A2, A4, A1]  com índices [2, 1, 3, 0]
            A2 está na posição 1
            Contribuição B1 = 1

Subtotal: 2 + 1 = 3
```

**DUPLA 3: A3 ↔ B4**

```
A3 prefere: [B4, B1, B3, B2]  com índices [3, 0, 2, 1]
            B4 está na posição 0
            Contribuição A3 = 0 ⭐ (1ª preferência!)

B4 prefere: [A1, A3, A4, A2]  com índices [0, 2, 3, 1]
            A3 está na posição 1
            Contribuição B4 = 1

Subtotal: 0 + 1 = 1
```

**DUPLA 4: A4 ↔ B2**

```
A4 prefere: [B3, B1, B2, B4]  com índices [2, 0, 1, 3]
            B2 está na posição 2
            Contribuição A4 = 2

B2 prefere: [A3, A2, A4, A1]  com índices [2, 1, 3, 0]
            A4 está na posição 2
            Contribuição B2 = 2

Subtotal: 2 + 2 = 4
```

### Resultado Final

```
Aptidão Total = 6 + 3 + 1 + 4 = 14

Interpretação: Solução EXCELENTE (aptidão < 20) ⭐
```

---

## 🎯 Análise da Solução

### Pontos Bons
```
A3 ↔ B4: A3 ficou com PRIMEIRA preferência! (posição 0)
A2 ↔ B1: Ficou com SEGUNDA-TERCEIRA preferência (posição 2)
```

### Pontos Ruins
```
A1 ↔ B3: A1 ficou com ÚLTIMA preferência (posição 3) 😞
A4 ↔ B2: A4 ficou com TERCEIRA preferência (posição 2)
```

### Por que não é perfeita?
Porque nem sempre é possível agradar a todos. Se:
- A1 quer B1, mas B1 quer A3
- Alguém tem que ficar insatisfeito!

---

## 📈 Exemplo 3: Comparando Duas Soluções

### Solução 1
```
Individuo = [0, 1, 2, 3]
A1 ↔ B1, A2 ↔ B2, A3 ↔ B3, A4 ↔ B4
```

Cálculo (resumido):
```
A1-B1: 0 + 0 = 0 ⭐ (ambos primeira preferência!)
A2-B2: 0 + 0 = 0 ⭐ (ambos primeira preferência!)
A3-B3: 2 + 2 = 4
A4-B4: 3 + 1 = 4

Aptidão Total = 0 + 0 + 4 + 4 = 8 EXCELENTE! ⭐⭐⭐
```

### Solução 2
```
Individuo = [1, 2, 3, 0]
A1 ↔ B2, A2 ↔ B3, A3 ↔ B4, A4 ↔ B1
```

Cálculo (resumido):
```
A1-B2: 1 + 1 = 2
A2-B3: 1 + 0 = 1
A3-B4: 0 + 1 = 1
A4-B1: 1 + 3 = 4

Aptidão Total = 2 + 1 + 1 + 4 = 8 EXCELENTE! ⭐⭐⭐
```

### Conclusão
Ambas têm mesma aptidão! Mas composição diferente.
O AG poderia aceitar qualquer uma.

---

## 🔄 Exemplo 4: Visualizando Evolução

### Gerações Sucessivas

**Geração 1:**
```
Indivíduo A: [0, 1, 2, 3]  → Aptidão: 145
Indivíduo B: [2, 3, 1, 0]  → Aptidão: 168
Indivíduo C: [1, 0, 3, 2]  → Aptidão: 152
...
Melhor: 145, Pior: 210, Média: 167.5
```

**Geração 10:**
```
Indivíduo A: [1, 2, 0, 3]  → Aptidão: 72
Indivíduo B: [0, 1, 3, 2]  → Aptidão: 65
Indivíduo C: [2, 0, 3, 1]  → Aptidão: 68
...
Melhor: 65, Pior: 98, Média: 75.5
```

**Geração 50:**
```
Indivíduo A: [0, 1, 2, 3]  → Aptidão: 8
Indivíduo B: [1, 2, 0, 3]  → Aptidão: 9
Indivíduo C: [0, 1, 3, 2]  → Aptidão: 12
...
Melhor: 8, Pior: 28, Média: 12.3
```

### Interpretação
```
Gen 1  → Gen 10  → Gen 50
145       65        8
↓         ↓         ↓
[melhorando!]
```

## Respostas a Perguntas Comuns

**P: Por que B3 não aparece na posição?**
R: Porque no individuo [2, 0, 3, 1]:
- Posição 0 tem valor 2 → B3 (índice 2 = 3º aluno)
- Posição 1 tem valor 0 → B1 (índice 0 = 1º aluno)
Entendo? Não confundir posição com índice!

**P: E se a aptidão desse negativa?**
R: Não pode! As posições são sempre ≥ 0.
Mínimo absoluto é 0 (solução perfeita).

**P: Qual é a aptidão máxima possível?**
R: Teoricamente n² (se ficasse o oposto de tudo).
Para 4 alunos: 16 é máximo.
Mas na prática, AG muda antes de ficar tão ruim.

**P: Como o algoritmo "sabe" que 8 é melhor que 145?**
R: Porque 8 < 145!
O AG ordena por aptidão e prefere valores menores.
Simples assim!

## 📊 Tabela Rápida de Referência

Para usar durante apresentação:

```
APTIDÃO          INTERPRETAÇÃO           EMOJIS
─────────────────────────────────────────────────
0                Solução Perfeita        ⭐⭐⭐
1-9              Excelente               ⭐⭐
10-19            Boa                     ⭐
20-49            Razoável                ✓
50+              Ruim (típica geração 1) 😞
```
