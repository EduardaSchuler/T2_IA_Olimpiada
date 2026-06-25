# CHECKLIST FINAL T2 - Inteligência Artificial: Alocação de Duplas com Algoritmo Genético

## ✅ CHECKLIST PRÉ-APRESENTAÇÃO

### Código (Tecnicamente)
- [x] T2.py executa sem erros
- [x] Genetico.py está completo
- [x] exemplo1.txt está acessível
- [x] Python 3 está instalado
- [x] Nenhuma biblioteca externa necessária
- [x] Testou modo automático?
- [x] Testou modo passo-a-passo?
- [x] Testou com parâmetros customizados?

### Documentação
- [x] README.md foi revisado?
- [x] Roteiro memorizado ou anotado?
- [x] Conhece cada exemplo de cálculo?
- [x] Guia de testes foi lido?
- [x] Sabe responder perguntas comuns?

### Apresentação (Slides)
- [x] Baixou a apresentação?
- [x] Testou em computador de apresentação?
- [x] Todos os slides aparecem?
- [x] Slides têm boa formatação?
- [x] Consegue navegar rapidamente?

### Vídeo
- [ ] Roteiro foi praticado?
- [ ] Todos 3 integrantes sabem sua parte?
- [ ] Câmera e áudio testados?
- [ ] Iluminação adequada?
- [ ] Fundo limpo e neutro?
- [ ] Ensaio completo feito?
- [ ] Tempo está entre 5-8 minutos?
- [ ] Arquivo foi salvo?
- [ ] Arquivo foi enviado/armazenado?

### Compreensão
- [x] Entendo o problema (olimpíada)?
- [x] Entendo por que usar AG?
- [x] Consigo explicar codificação?
- [x] Consigo calcular aptidão manualmente?
- [x] Entendo cada operador (seleção, crossover, mutação)?
- [x] Consigo explicar critérios de parada?
- [x] Consigo ler resultado final?
- [x] Consigo responder sobre parâmetros?

## TÓPICOS SOLICITADOS PELA PROFESSORA

Cada tópico está coberto em:

### 1. Leitura do Arquivo (0,5 pts)
- ✅ Testado em **GUIA_TESTES.md** (Teste 1)
- ✅ Explicado em **README.md** (Seção 4)
- ✅ Validado em **T2.py** (função `lerArquivo()`)

### 2. Implementação do AG (1,5 pts)
- ✅ Codificação: **Genetico.py** (função `geraAptidao()`)
- ✅ Operadores: **Genetico.py** (4 funções)
- ✅ Ciclo: **Genetico.py** (função `AG()`)
- ✅ Explicado em **README.md** (Seção 4)
- ✅ Demonstrado em **ROTEIRO_APRESENTACAO.md**

### 3. Função Heurística (2,0 pts)
- ✅ Implementada em **Genetico.py** (`geraAptidao()`)
- ✅ Explicada em **README.md** (Seção 5)
- ✅ Exemplificada em **EXEMPLOS_CALCULO_APTIDAO.md**
- ✅ Apresentação slide 6-8

### 4. Execução - Modos de Exibição (2,0 pts)
- ✅ Modo automático: **T2.py** (`executarModoAutomatico()`)
- ✅ Modo passo-a-passo: **T2.py** (`executarModoPassoAPasso()`)
- ✅ Testado em **GUIA_TESTES.md** (Testes 2 e 4)
- ✅ Demostrado em **ROTEIRO_APRESENTACAO.md**
- ✅ Argumentos aceitos via linha de comando

### 5. Relatório em PPT (2,0 pts)
- ✅ **Apresentacao_T2_IA_AG.pptx** (23 slides)
- ✅ Codificação: Slides 5-6
- ✅ Heurística: Slides 6-8
- ✅ Operadores: Slides 9-11
- ✅ Parâmetros: Slide 14
- ✅ Critérios de parada: Slide 13
- ✅ Testes e resultados: Slides 15-17
- ✅ Discussão: Slides 19-20

### 6. Testes (0,5 pts cada, máx 2.0)
- ✅ Procedimento em **GUIA_TESTES.md**
- ✅ Critérios de aceitação definidos
- ✅ Possíveis erros documentados

# 📦 RESUMO DE ENTREGA

## 📊 ESTATÍSTICAS

  Código Python:              ~430 linhas
  Documentação:               ~2800 linhas
  Roteiro de Apresentação:    ~600 linhas
  Guia de Testes:             ~500 linhas
  Exemplos Práticos:          ~350 linhas
  
  Tamanho Total:              168 KB
  Tempo de Leitura:           ~2-3 horas
  Tempo de Estudo:            ~4-5 horas

## TÓPICOS ATENDIDOS
  ✅ 0,5 pts - Leitura do arquivo
  ✅ 1,5 pts - Implementação do ciclo do AG
  ✅ 2,0 pts - Função heurística
  ✅ 2,0 pts - Execução (modos de exibição)
  ✅ 2,0 pts - Relatório em formato PPT
  ✅ 0,5-2,0 pts - Testes

## PASSO A PASSO
1. COMECE AQUI:
   → Abra "Sumário do Projeto"
   → Siga as instruções passo-a-passo

2. ESTUDE AGORA:
   → Leia "README.md"
   → Execute "python T2.py exemplo1.txt"

3. TESTE TUDO:
   → Execute testes em "GUIA_TESTES.md"
   → Verifique "CHECKLIST_FINAL.md"

Vocês têm:
- ✅ Código funcionando
- ✅ Documentação detalhada
- ✅ Exemplos práticos
- ✅ Guia de testes
- ✅ Roteiro de apresentação
- ✅ Slides profissionais
- ✅ Checklist e cronograma


## SUPORTE A ERROS
Se algo não funcionar:

### Erro: "ModuleNotFoundError: No module named 'Genetico'"
- Solução: Certifique-se que Genetico.py está no mesmo diretório

### Erro: "FileNotFoundError: exemplo1.txt"
- Solução: Execute da pasta certa, ou especifique caminho completo
- `python T2.py /caminho/completo/exemplo1.txt`

### Erro: "SyntaxError"
- Solução: Verificar se não tem caracteres especiais no código
- Use editor que preserve encoding UTF-8

### Programa muito lento
- Solução: Reduzir --pop ou --ger
- `python T2.py exemplo1.txt --pop 30 --ger 200`
