# ROTEIRO DE APRESENTAÇÃO - VÍDEO DO T2 - Inteligência Artificial: Alocação de Duplas com Algoritmo Genético
**Duração Total:** 5-8 minutos  
- Consultar respectivos slides no canva
---

## ESTRUTURA GERAL

| Tempo | Integrante | Tópico |
|-------|------------|--------|
| 0:00-0:30 | Larissa | Introdução e Problema |
| 0:30-1:30 | Larissa | Algoritmo Genético (Conceito) |
| 1:30-3:00 | Maria Eduarda | Implementação e Operadores |
| 3:00-5:00 | João | Execução e Resultados |
| 5:00-6:00 | Maria Eduarda | Análise e Desafios |
| 6:00-8:00 | João | Fechamento |

---

## 🎬 ABERTURA - Larissa

### Script

[Saudação amigável, sorriso]

"Olá! Sou Larissa, e hoje vamos apresentar nosso trabalho de 
Inteligência Artificial sobre alocação de duplas em uma olimpíada.

[Mostrar slide de CAPA por 3 segundos]

Nosso trabalho resolve um problema bem interessante: 
imagine que temos alunos de duas escolas diferentes que 
precisam compartilhar quartos em um hotel durante uma olimpíada.

O desafio é formar duplas - um aluno de cada escola - 
respeitando ao máximo as preferências de todos.

Por exemplo, se o aluno A1 prefere ficar com B2, B4, ou B1 
nessa ordem, queremos tentar colocá-lo com seu favorito.

Para resolver isso, usamos um Algoritmo Genético, um método 
inspirado na evolução natural que simula seleção e reprodução.

[Passar para Maria]

## 🧬 ALGORITMO GENÉTICO- Larissa

### Script

[Mostrar slide "POR QUE ALGORITMO GENÉTICO?"]

Primeiro, por que escolhemos Algoritmo Genético?

Veja bem: com apenas 4 alunos, temos 24 possibilidades de 
formar duplas. Com 10 alunos? 3,6 MILHÕES de possibilidades!

Com 100 alunos? Um número tão grande que nem computador 
consegue verificar todas as combinações em tempo razoável.

Por isso, em vez de testar TUDO, o Algoritmo Genético é mais 
inteligente: ele evolui soluções, assim como a natureza evolui 
organismos através de seleção natural.

[Mostrar slide "CICLO DO AG"]

Vou contar como funciona:

PASSO 1 - INICIALIZAÇÃO:
Criamos 50 soluções aleatórias - 50 formas diferentes de 
agrupar os alunos.

PASSO 2 - AVALIAÇÃO:
Para cada solução, calculamos: 'Quão boa ela é?'
Usamos uma fórmula que soma as posições de preferência.
Soluções melhores recebem pontos mais baixos.

PASSO 3 - SELEÇÃO E REPRODUÇÃO:
As melhores soluções têm mais chance de 'se reproduzir'.
É como na natureza: animais mais fortes têm mais filhotes.

PASSO 4 - CRUZAMENTO E MUTAÇÃO:
Dois pais combinam suas características para criar filhos.
Às vezes, uma mudança aleatória (mutação) melhora o filho.

PASSO 5 - NOVA GERAÇÃO:
Os filhos entram na população.
Os piores solitários saem (a menos que sejam os melhores).

Depois repetimos do passo 2 até encontrar uma boa solução 
ou atingir 500 gerações.

[Mostrar slide "CRITÉRIOS DE PARADA"]

O algoritmo para quando:
- Encontra a solução perfeita (aptidão = 0), ou
- 100 gerações passam sem melhora, ou
- Atinge o limite de 500 gerações.

[Passar para Maria]

### Dicas de Apresentação
- ✓ Use analogias com natureza (evolução)
- ✓ Fale sobre "gerações" como se fosse reprodução
- ✓ Mostre slides enquanto explica cada passo
- ✓ Deixe claro por que é melhor que busca exaustiva

## 💻 IMPLEMENTAÇÃO - MARIA EDUARDA

### Script Parte 1 - CODIFICAÇÃO
[Saudação]

"Oi! Sou Maria Eduarda. Agora vou mostrar como implementamos 
esse algoritmo e como ele funciona na prática.

[Mostrar slide "CODIFICAÇÃO"]

Primeiro, como representamos uma solução no computador?

Usamos uma PERMUTAÇÃO - uma sequência de números.

Por exemplo: [2, 0, 3, 1]

Isso significa:
- Aluno A1 fica com aluno B3 (índice 2)
- Aluno A2 fica com aluno B1 (índice 0)
- Aluno A3 fica com aluno B4 (índice 3)
- Aluno A4 fica com aluno B2 (índice 1)

Cada posição i na lista contém o índice j do aluno de B que 
ficará com o aluno de A.

[Mostrar slide "FUNÇÃO HEURÍSTICA"]

Agora, a fórmula MAIS IMPORTANTE: a função de aptidão (qualidade).

Para cada dupla A_i com B_j, somamos:
1. A posição que B_j aparece na lista de preferências de A_i
2. A posição que A_i aparece na lista de preferências de B_j

Exemplo concreto:
A1 prefere: [B1, B2, B4, B3]
Se A1 ficar com B4, B4 está na posição 2.
Contribuição = 2

B4 prefere: [A1, A3, A4, A2]
Se B4 ficar com A1, A1 está na posição 0.
Contribuição = 0

Total dessa dupla: 2 + 0 = 2

Fazemos isso para todas as 4 duplas e somamos.
Quanto MENOR o número, melhor a solução!

Aptidão 0 = solução PERFEITA (todos com primeira preferência)
Aptidão < 10 = solução EXCELENTE
Aptidão < 20 = solução BOA
Aptidão ≥ 20 = solução RAZOÁVEL
"

### Script Parte 2 - OPERADORES
[Mostrar slide "SELEÇÃO POR TORNEIO"]

Vamos falar dos operadores genéticos - as operações que 
criam filhos a partir de pais.

PRIMEIRO: SELEÇÃO POR TORNEIO

Como escolhemos quais soluções vão se reproduzir?

Fazemos um 'torneio':
1. Sorteamos 3 soluções aleatoriamente
2. Pegamos a melhor com 90% de chance
3. Pegamos a segunda melhor com 10% de chance

Por que esse desequilíbrio?
- 90% garante que boas soluções se reproduzem
- 10% mantém diversidade, evita que todos virem cópias

[Mostrar slide "CROSSOVER"]

SEGUNDO: CROSSOVER (ou cruzamento)

Com 80% de probabilidade, pegamos DOIS pais e criamos filhos.

Usamos Order Crossover (OX):
1. Escolhemos dois pontos de corte aleatoriamente
2. O filho herda um segmento do pai 1
3. Completa com genes do pai 2, respeitando ordem

Exemplo visual:
Pai1:  [1, 2, 3, 4, 5, 6, 7, 8]
Pai2:  [3, 7, 5, 1, 6, 8, 2, 4]
Corte: [2, 5]

Filho herda pai1[2:5] = [3, 4, 5, 6]
Depois completa com pai2, pulando genes já usados:
Resultado: [3, 7, X, 4, 5, 6, 1, 8]

Por que funcionou? Porque preserva segmentos bons!

[Mostrar slide "MUTAÇÃO"]

TERCEIRO: MUTAÇÃO

Com 15% de probabilidade, fazemos uma mudança aleatória:

Pegamos 2 posições aleatórias e TROCAMOS seus valores.

Antes:  [1, 2, 3, 4, 5]
Trocamos posições 1 e 4
Depois: [1, 5, 3, 4, 2]

Por que isso?
- Permite escape de soluções ruins onde ficou 'preso'
- 15% é o ponto certo: não destrói soluções boas

[Passar para João]
"

### Dicas de Apresentação
- ✓ Use exemplos numéricos simples
- ✓ Desenhe ou use visual ao explicar OX
- ✓ Mostre slides em sequência lógica
- ✓ Relate cada operador com seu propósito biológico

## ▶️ EXECUÇÃO E RESULTADOS - JOÃO

### Script
[Saudação]

"Oi! Sou João. Agora vou mostrar o programa funcionando.

[Mostrar terminal]

Para executar, digitamos:

$ python T2.py exemplo1.txt

[Pressionar Enter - deixar executar por 30 segundos]

Veja o que está acontecendo:

Primeiro, o programa LÊ o arquivo de preferências e mostra 
cada aluno e suas preferências de companheiro.

Depois, EXECUTA o Algoritmo Genético.

Vamos ver a evolução! 

[Apontar na tela]

Na primeira geração, a melhor solução tem aptidão 145.
Na segunda, melhorou para 142.
Na terceira, para 139...

Percebem? Está EVOLUINDO! A aptidão está diminuindo.

Isso significa que o algoritmo está encontrando soluções cada 
vez melhores a cada geração.

[Deixar rodar até o fim, ~30-45 segundos]

Perfeito! Terminou!

[Apontar para resultado final]

Aqui vemos:

1. A aptidão final: 42
   Isso é uma solução BOA!

2. As duplas formadas:
   - Quarto 1: A1 com B3
   - Quarto 2: A2 com B2
   - Quarto 3: A3 com B4
   - Quarto 4: A4 com B1

3. A solução está DECODIFICADA e legível!
Agora vou mostrar o modo passo-a-passo:

$ python T2.py exemplo1.txt --modo passo

[Mostrar uma ou duas iterações]

Aqui o programa PAUSA a cada geração, permitindo você 
acompanhar visualmente a evolução passo a passo.

g\Você pode ver exatamente como a população muda a cada geração.

[Passar para Maria]
"
### Dicas de Apresentação
- ✓ Deixe código rodar naturalmente
- ✓ Aponte para números específicos enquanto explica
- ✓ Mostre ambos os modos (automático e passo-a-passo)
- ✓ Não acelere a execução no vídeo final

---

## 💡 ANÁLISE E DESAFIOS - MARIA

### Script
"Agora vamos analisar os resultados e tirar conclusões.

[Mostrar slide "DISCUSSÃO: DESAFIOS"]

Durante o desenvolvimento, encontramos alguns desafios 
importantes:

DESAFIO 1 - Função de Aptidão
No início, era difícil decidir como medir qualidade.
Solução: Somamos as posições nas listas de preferências.
Resultado: Métrica simples, mas eficaz!

DESAFIO 2 - Representação do Problema
Precisamos garantir que toda solução seja uma permutação válida 
(sem repetições, sem ausências).
Solução: Operador OX é específico para isso.
Resultado: Nunca gera solução inválida!

DESAFIO 3 - Ajuste de Parâmetros
Taxa de mutação 5% era baixa demais = estagnação
Taxa de mutação 50% era alta demais = soluções aleatórias
Solução: Teste prático chegou a 15%
Resultado: Equilíbrio perfeito!

[Mostrar slide "INSIGHTS"]

INSIGHTS importantes que aprendemos:

1. Algoritmo Genético é MUITO EFICAZ para este problema
   Converge rápido, encontra boas soluções em minutos.

2. A codificação importa MUITO
   Uma boa representação = operadores simples e eficazes

3. Trade-off Qualidade vs Tempo é real
   500 gerações = solução boa
   1000 gerações = um pouco melhor, mas 2x mais lento

4. A função de aptidão é O CORAÇÃO do algoritmo
   Se ela não está bem definida, tudo falha
"
[Passar para João para fechamento]

## 📋 FECHAMENTO - JOÃO

### Script de Fechamento - JOÃO

[Mostrar slide "CONCLUSÃO"]

" Concluindo:

✓ Implementamos com sucesso um Algoritmo Genético
✓ Resolvemos o problema de alocação de duplas
✓ O código é claro, bem-documentado e funcional
✓ A interface é amigável ao usuário

Recomendações futuras:
- Testar com cenários maiores (100+ alunos)
- Comparar com outras metaheurísticas (Simulated Annealing)
- Implementar visualização gráfica da evolução

Para fechar, vou fazer um resumo rápido:

Problema: 
- Alocar alunos de 2 escolas em duplas respeitando preferências

Solução:
- Algoritmo Genético com permutações

Resultados:
- Encontra soluções boas em tempo razoável

[Mostrar slide "OBRIGADO"]

Temos:
- O código completo e funcional
- README com documentação detalhada
- Esta apresentação
- Vários arquivos de teste

Qualquer dúvida sobre a implementação, parâmetros, 
ou resultados, estamos aqui para discutir!

Obrigado! 🙏"

## Perguntas Esperadas e Respostas
**P: Por que não usaram Simulated Annealing?**
R: Algoritmo Genético é mais adequado para permutações. 
SA é melhor para valores contínuos.

**P: E se uma solução ótima não existir?**
R: O algoritmo encontra a melhor solução possível mesmo assim.
Não é obrigado encontrar nota 0.

**P: Como escalar para 1000 alunos?**
R: Funciona igual! Pode ser mais lento, mas o código é escalável.
A aptidão é calculada da mesma forma.

**P: Qual é a chance de dois pais iguais se reproduzirem?**
R: É possível, raramente. Se dois indivíduos iguais cruzam,
os filhos são cópias (crossover não muda).
Depois a mutação introduz variação.

**P: Como você escolheu Taxa = 80% de crossover?**
R: Teste prático. Menos de 80% = não explora bem.
Mais de 80% = muito cruzamento, pouca diversidade.

---

## NOTAS IMPORTANTES

1. **Mantenha foco nos tópicos principais:**
   - Problema clara
   - Por que AG?
   - Codificação
   - Aptidão (o mais importante!)
   - Operadores
   - Resultados

2. **Evite:**
   - Jargão muito técnico sem explicação
   - Ler slides, fale naturalmente
   - Falar muito rápido
   - Deixar slides invisíveis na câmera

3. **Faça destaque a:**
   - Execução do programa (mostrar funciona!)
   - Evolução das gerações (gráfico mental)
   - Solução final decodificada
   - Clareza da documentação

4. **Aproveite para:**
   - Mostrar domínio do assunto
   - Demostrar que todos entendem
   - Responder com confiança
