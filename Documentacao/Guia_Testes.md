# GUIA DE TESTES E VALIDAÇÃO
## T2 - Inteligência Artificial: Alocação de Duplas com Algoritmo Genético

**Data:** Junho de 2024  
**Autores:** João, Larissa, Maria Eduarda

## 🎯 Objetivo dos Testes

Demonstrar que o programa:
1. ✓ Lê arquivo de entrada corretamente
2. ✓ Implementa o AG com todos os componentes
3. ✓ Calcula aptidão corretamente
4. ✓ Evolui a população adequadamente
5. ✓ Exibe resultados de forma legível
6. ✓ Funciona em diferentes modos

---

## 📋 TESTE 1: Leitura do Arquivo

### Comando
```bash
python T2.py exemplo1.txt
```

### O que Procurar
✓ Arquivo é lido corretamente
✓ Preferências são exibidas (A1, A2, ..., B1, B2, ...)
✓ Número de duplas está correto (4)
✓ Formato das preferências faz sentido (A1 prefere B1 > B2 > ...)

### Saída Esperada
```
============================================================
PREFERÊNCIAS DOS ALUNOS (Total: 4 duplas)
============================================================

📋 ESCOLA A - Preferências por aluno:
   A1: B1 > B2 > B4 > B3
   A2: B2 > B3 > B1 > B4
   A3: B4 > B1 > B3 > B2
   A4: B3 > B1 > B2 > B4

📋 ESCOLA B - Preferências por aluno:
   B1: A3 > A2 > A4 > A1
   B2: A3 > A2 > A4 > A1
   B3: A2 > A4 > A3 > A1
   B4: A1 > A3 > A4 > A2
```

### Validação
- [ ] Todas as 4 preferências de A aparecem?
- [ ] Todas as 4 preferências de B aparecem?
- [ ] Não há erros de formatação?
- [ ] O arquivo foi realmente lido?

### Possíveis Erros e Soluções
**Erro:** `FileNotFoundError: exemplo1.txt não encontrado`
- Solução: Executar de dentro da pasta correta
  ```bash
  cd /caminho/para/T2_IA_Olimpiada
  python T2.py exemplo1.txt
  ```

**Erro:** Valores negativos ou índices fora do intervalo
- Solução: Arquivo está corrompido, restaurar exemplo1.txt

---

## 📊 TESTE 2: Execução do AG (Modo Automático)

### Comando
```bash
python T2.py exemplo1.txt --modo auto
```

### O que Procurar
✓ O algoritmo começa a rodar (vê "Geração 1")
✓ Aptidão melhora ao longo das gerações
✓ Algoritmo para em algum momento
✓ Saída final tem duplas formadas

### Saída Esperada (Trecho)
```
⚙️  Executando Algoritmo Genético...
   Tamanho da População: 50
   Máximo de Gerações: 500
   Taxa de Crossover: 0.8 (80%)
   Taxa de Mutação: 0.15 (15%)
   Seleção: Torneio

  Geração    1 | Melhor:   145 | Média: 167.50 | Pior:   210
  Geração    2 | Melhor:   142 | Média: 160.30 | Pior:   205
  Geração    3 | Melhor:   139 | Média: 155.20 | Pior:   198
  ...
  Geração   50 | Melhor:    45 | Média:  62.10 | Pior:   108
```

### Validação
- [ ] Números aparecem em ordem (Gen 1, 2, 3, ...)?
- [ ] Coluna "Melhor" tende a diminuir?
- [ ] Coluna "Pior" também diminui (população evolui)?
- [ ] Não há erro de divisão por zero ou exceção?

### Interpretação dos Números
```
Geração 1:
- Melhor = 145    (melhor indivíduo tem aptidão 145)
- Média = 167.50  (população tem aptidão média 167.50)
- Pior = 210      (pior indivíduo tem aptidão 210)
  
Geração 50:
- Melhor = 45     (MELHOROU! 145 → 45)
- Média = 62.10   (população melhorou)
- Pior = 108      (até o pior melhorou)
```

### Possíveis Erros
**Erro:** `ValueError: list.index(x): x not in list`
- Causa: Função de aptidão recebeu gene não esperado
- Solução: Revisar operador de cruzamento

**Erro:** `IndexError: list index out of range`
- Causa: Acesso a posição inválida na população
- Solução: Revisar ordenação ou seleção

**Erro:** Aptidão não melhora nunca
- Causa: Taxa de mutação muito alta ou AG preso em mínimo local
- Solução: Aumentar número de gerações (--ger 1000)

## 🔍 TESTE 3: Verificação de Solução Final
### Comando
```bash
python T2.py exemplo1.txt
```

### Saída Esperada
```
📊 Qualidade da Solução (Aptidão): 42
   ✓ BOA! (Boa qualidade)

🤝 DUPLAS FORMADAS:
   Quarto 1: A1 ↔ B3
   Quarto 2: A2 ↔ B2
   Quarto 3: A3 ↔ B4
   Quarto 4: A4 ↔ B1

📝 Solução Codificada: [3, 2, 4, 1]
```

### Validação Manual
**Verificar 1: Todos alocados?**
```
A1: ↔ B3 ✓
A2: ↔ B2 ✓
A3: ↔ B4 ✓
A4: ↔ B1 ✓

Contagem: 4/4 alunos ✓
```

**Verificar 2: Ninguém repetido?**
```
Alunos B aparecem: B3, B2, B4, B1
São todos diferentes? SIM ✓

É uma permutação válida? SIM ✓
```

**Verificar 3: Aptidão está correta?**

Usando as preferências:
```
A1 prefere: B1(0) > B2(1) > B4(3) > B3(2)
B3 prefere: A2(1) > A4(3) > A3(2) > A1(0)

Se A1 ↔ B3:
  Posição de B3 em pref de A1: 3 (4ª posição)
  Posição de A1 em pref de B3: 3 (4ª posição)
  Subtotal: 3 + 3 = 6

[Fazer o mesmo para A2-B2, A3-B4, A4-B1]
[Somar tudo]
Total calculado = deve bater com valor exibido
```

### Possíveis Erros

**Erro:** Solução não é uma permutação (aluno repetido)
- Causa: Operador de cruzamento não preserva permutação
- Solução: Revisar Order Crossover

**Erro:** Aptidão calculada está errada
- Causa: Erro na função `geraAptidao()`
- Solução: Testar com exemplo manual

**Erro:** Nenhuma dupla é mostrada
- Causa: População não foi avaliada
- Solução: Verificar loop principal do AG

---

## ⏳ TESTE 4: Modo Passo a Passo
### Comando
```bash
python T2.py exemplo1.txt --modo passo
```

### O que Procurar
✓ Exibe preferências (como antes)
✓ Mostra "Geração 1" e pausa
✓ Teclado semafu pode avançar (Enter)
✓ Mostra cada geração sequencialmente

### Procedimento
1. Execute comando acima
2. Veja preferências
3. Pressione Enter para Gen 1
4. Pressione Enter para Gen 2
5. Repita 3-4 vezes para ver evolução
6. Pressione Ctrl+C para parar

### Validação
- [ ] Pausa a cada geração?
- [ ] Números mudam entre gerações?
- [ ] Aptidão melhora com o tempo?
- [ ] Pode pausar/retomar facilmente?

### Propósito Pedagógico
Este modo é ótimo para **entender visualmente** como o AG evolui:
- Vê cada passo da evolução
- Entende que não é instantâneo
- Aprecia a "luta" por melhor solução

---

## TESTE 5: Parâmetros Customizados

### Teste 5a: População Maior
```bash
python T2.py exemplo1.txt --pop 100 --ger 500
```

**Esperado:**
- Mais diversidade (100 indivíduos vs 50)
- Potencialmente melhor solução
- Um pouco mais lento

**Validação:**
- [ ] Executa sem erro?
- [ ] Exibe "Tamanho da População: 100"?
- [ ] Termina com aptidão melhor que 50?

### Teste 5b: Mais Gerações
```bash
python T2.py exemplo1.txt --ger 1000
```

**Esperado:**
- Mais tempo para convergir
- Potencialmente melhor solução
- Significativamente mais lento

**Validação:**
- [ ] Executa 1000 gerações?
- [ ] Exibe "Máximo de Gerações: 1000"?
- [ ] Melhora de aptidão em relação a 500?

### Teste 5c: População e Gerações
```bash
python T2.py exemplo1.txt --pop 200 --ger 2000
```

**Esperado:**
- Melhor solução
- Muito mais lento (5-10 segundos)
- Convergência clara

**Validação:**
- [ ] Ambos parâmetros foram aceitos?
- [ ] Executa até o final?
- [ ] Melhora significativa na aptidão?

---

## 📈 TESTE 6: Análise de Convergência

### Objetivo
Demonstrar que o AG **realmente converge** a soluções boas.

### Procedimento
1. Execute 3 vezes o mesmo arquivo:
   ```bash
   python T2.py exemplo1.txt
   python T2.py exemplo1.txt
   python T2.py exemplo1.txt
   ```

2. Anote as 3 aptidões finais
3. Considere a média

### Esperado
```
Execução 1: Aptidão final = 42
Execução 2: Aptidão final = 45
Execução 3: Aptidão final = 41
Média: 42.67

Todas próximas, sem grande variação ✓
```

### Por que é importante?
- Se um dia dá 42, outro dia dá 200 = instável
- Se sempre dá algo próximo a 42 = algoritmo é robusto
- Variação pequena é normal (aleatório)

### Validação
- [ ] Aptidões finais são similares (±10%)?
- [ ] Não há outliers (um resultado muito pior)?
- [ ] Algoritmo é robusto?

---

## 🔐 TESTE 7: Validade da Saída

### Checklist Final
Executar uma vez mais e verificar:

```
✓ Leitura do arquivo completa
✓ Preferências exibidas corretamente
✓ AG executa sem exceções
✓ Histórico de gerações aparece
✓ Solução final é uma permutação válida
✓ Aptidão é número não-negativo
✓ Duplas estão decodificadas
✓ Mensagens estão formatadas
```

### Cada Critério Vale:

| Critério | Pontos | Verificado |
|----------|--------|-----------|
| Leitura arquivo | 0.5 | [ ] |
| Implementação AG | 1.5 | [ ] |
| Função heurística | 2.0 | [ ] |
| Execução/Modos | 2.0 | [ ] |
| Apresentação | 2.0 | [ ] |
| Teste arquivo | 0.5 | [ ] |
| **TOTAL** | **10.0** | |

---

## 🚀 TESTE 8: Escalabilidade

### Teste com Mais Alunos (OPCIONAL)

Se tiver tempo, criar arquivo `teste_grande.txt`:

```
10
1 2 3 4 5 6 7 8 9 10
2 3 4 5 6 7 8 9 10 1
...
(10 linhas de preferências de A)

1 2 3 4 5 6 7 8 9 10
2 3 4 5 6 7 8 9 10 1
...
(10 linhas de preferências de B)
```

### Execução
```bash
python T2.py teste_grande.txt
```

### Validação
- [ ] Executa para 10 alunos?
- [ ] Tempo razoável (<30 segundos)?
- [ ] Solução é permutação válida?
- [ ] Forma 10 duplas diferentes?

---
## 🎓 APRESENTAÇÃO DOS TESTES

### O que Mostrar (Max 5 minutos)

1. **Leitura**
   - Execute `python T2.py exemplo1.txt`
   - Aponte as preferências na saída
   - "Veem? A1 prefere B1, depois B2..."

2. **Algoritmo Rodando**
   - Deixar rodar até a metade
   - Aponte números: "Geração 1 = aptidão 145, Geração 25 = aptidão 60"
   - "Veem a convergência? Está melhorando!"

3. **Resultado Final**
   - Mostre as duplas formadas
   - "A1 com B3, A2 com B2, etc"
   - Calcule UMA dupla manualmente: "A1 preferia B1, ficou com B3..."

4. **Modo Passo-a-Passo**
   - Mostre que é possível visualizar cada geração
   - Avance 2-3 gerações

## 📝 Respostas Esperadas a Perguntas
**P: Como você verifica que o resultado está correto?**
R: Verificamos 3 coisas:
1. É uma permutação (sem repetição, sem falta)
2. Todas as duplas estão presentes
3. A aptidão bate quando calculamos manualmente

**P: E se o algoritmo encontrar solução ótima (aptidão=0)?**
R: Para imediatamente, exibe solução e encerra.

**P: Por que às vezes pega 100 gerações, às vezes 50?**
R: Depende da aleatoriedade. Às vezes converge rápido, 
às vezes leva mais. Critério "100 ger sem melhora" protege.

**P: O código funciona para qualquer número de alunos?**
R: Sim! Apenas mude o arquivo de entrada.
Testamos com 4, funciona com 10+.

**P: Como você escolheu taxa mutação = 15%?**
R: Teste prático. Abaixo de 10% = estagna.
Acima de 20% = muito aleatório.
15% foi o ponto ideal.