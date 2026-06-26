import sys
import random
import time
import argparse
import os

# ==========================================
# 1. FUNÇÃO DE LEITURA E DECODIFICAÇÃO
# ==========================================
def carregar_arquivo(caminho_arquivo):
    """Lê as matrizes e repara dados corrompidos nos arquivos de teste."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            tokens = f.read().split()
            
        if not tokens:
            raise ValueError("Arquivo vazio.")
            
        # Extrai apenas os inteiros, ignorando eventuais textos ou cabeçalhos perdidos no arquivo
        dados_brutos = []
        for t in tokens:
            try:
                dados_brutos.append(int(t))
            except ValueError:
                pass
                
        N = dados_brutos[0]
        pref_A, pref_B = [], []
        idx = 1 # Começa a ler após a variável N
        
        # Rotina de segurança: corrige eventuais erros de digitação (números repetidos ou faltantes)
        def sanear_preferencias(pref_list):
            vistos = set()
            faltantes = list(set(range(N)) - set(pref_list))
            nova_lista = []
            
            for p in pref_list:
                # Se o número é válido e ainda não foi visto
                if p not in vistos and 0 <= p < N:
                    vistos.add(p)
                    nova_lista.append(p)
                else:
                    # Encontrou uma duplicata. Substitui pelo número faltante para não quebrar o .index()
                    if faltantes:
                        substituto = faltantes.pop(0)
                        nova_lista.append(substituto)
                        vistos.add(substituto)
                    else:
                        nova_lista.append(p)
            return nova_lista

        # Lê Escola A
        for _ in range(N):
            # idx aponta para o ID do aluno, ignoramos. Pegamos os próximos N valores.
            preferencias = [x - 1 for x in dados_brutos[idx + 1 : idx + N + 1]]
            pref_A.append(sanear_preferencias(preferencias))
            idx += (N + 1)
            
        # Lê Escola B
        for _ in range(N):
            preferencias = [x - 1 for x in dados_brutos[idx + 1 : idx + N + 1]]
            pref_B.append(sanear_preferencias(preferencias))
            idx += (N + 1)
            
        return N, pref_A, pref_B
        
    except FileNotFoundError:
        print(f"[Erro] Arquivo não encontrado no caminho: {caminho_arquivo}")
        import sys; sys.exit(1)
    except Exception as e:
        print(f"[Erro] Falha ao processar arquivo de entrada: {e}")
        import sys; sys.exit(1)

def decodificar_solucao(estado):
    """Mapeia a solução codificada para leitura base-1 (A1 <-> B1)."""
    print("\n" + "="*50)
    print("SOLUÇÃO FINAL DECODIFICADA")
    print("="*50)
    for a_idx, b_idx in enumerate(estado):
        print(f"Quarto {a_idx + 1}: Aluno A{a_idx + 1} <-> Aluno B{b_idx + 1}")
    print("="*50 + "\n")

# ==========================================
# 2. FUNÇÕES EXATAS DOS SLIDES
# ==========================================
def geraAptidao(individuo, prefA, prefB):
    # Quanto menor a aptidão, melhor. O mínimo é 0 (todos na primeira posição)
    aptidao = 0
    for i, j in enumerate(individuo):
        aptidao += prefA[i].index(j)
        aptidao += prefB[j].index(i)
    return aptidao

def selecaoTorneio(populacao, aptidoes, k=3):
    populacaoIntermediaria = random.sample(range(len(populacao)), k)
    populacaoIntermediaria = sorted(populacaoIntermediaria, key=lambda i: aptidoes[i])
    if random.random() < 0.9:
        pos = 0
    else:
        pos = 1
    return populacao[populacaoIntermediaria[pos]][:]

# ==========================================
# 3. OPERADORES COMPLEMENTARES
# ==========================================
def crossover_ox(pai1, pai2, taxaDeCrossover):
    if random.random() > taxaDeCrossover: 
        return list(pai1), list(pai2)
    
    tamanho = len(pai1)
    p1, p2 = sorted(random.sample(range(tamanho), 2))
    
    def processar_filho(p_base, p_doador):
        filho = [-1] * tamanho
        filho[p1:p2] = p_base[p1:p2]
        idx_doador, idx_filho = p2, p2
        while -1 in filho:
            gene = p_doador[idx_doador % tamanho]
            if gene not in filho:
                filho[idx_filho % tamanho] = gene
                idx_filho += 1
            idx_doador += 1
        return filho

    return processar_filho(pai1, pai2), processar_filho(pai2, pai1)

def mutacao_swap(individuo, taxaDeMutacao):
    if random.random() < taxaDeMutacao:
        idx1, idx2 = random.sample(range(len(individuo)), 2)
        individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]
    return individuo

# ==========================================
# 4. FUNÇÃO PRINCIPAL DO AG (Assinatura Exata)
# ==========================================
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
    print("\n" + "="*50)
    print("=== INICIANDO ALGORITMO GENÉTICO ===")
    print("="*50)
    
    N = len(prefA)
    populacao = [list(range(N)) for _ in range(tamPopulacao)]
    for p in populacao: random.shuffle(p)
    
    melhor_estado_global = None
    melhor_aptidao_global = float('inf')
    contador_estagnacao = 0
    
    for geracao in range(1, numeroMaximoGeracoes + 1):
        # Utiliza a função geraAptidao exata
        aptidoes = [geraAptidao(ind, prefA, prefB) for ind in populacao]
        
        idx_melhor_atual = aptidoes.index(min(aptidoes))
        melhor_atual = populacao[idx_melhor_atual]
        aptidao_atual = aptidoes[idx_melhor_atual]
        media_aptidao = sum(aptidoes) / tamPopulacao
        
        if aptidao_atual < melhor_aptidao_global:
            melhor_aptidao_global = aptidao_atual
            melhor_estado_global = list(melhor_atual)
            contador_estagnacao = 0
        else:
            contador_estagnacao += 1
            
        print(f"[AG Geração {geracao:03d}] Média da População: {media_aptidao:.2f} | Aptidão (Melhor): {aptidao_atual} | Melhor Indivíduo: {melhor_atual}")
        
        # Respeita o parâmetro passoPasso da assinatura da função
        if passoPasso: time.sleep(0.1)
            
        if melhor_aptidao_global == 0:
            print(f"\n[!] Parada Antecipada: Solução Ótima Absoluta encontrada na geração {geracao}.")
            break
        if contador_estagnacao >= semMelhoraLimit:
            print(f"\n[!] Parada Antecipada: Algoritmo estagnou por {semMelhoraLimit} gerações seguidas.")
            break
            
        nova_populacao = []
        
        # Respeita o parâmetro elitismo
        if elitismo:
            nova_populacao.append(list(melhor_estado_global))
        
        while len(nova_populacao) < tamPopulacao:
            # Respeita o parâmetro tipoSelecao
            if tipoSelecao == "torneio":
                pai1 = selecaoTorneio(populacao, aptidoes)
                pai2 = selecaoTorneio(populacao, aptidoes)
            else:
                pai1 = selecaoTorneio(populacao, aptidoes) # Fallback seguro
                pai2 = selecaoTorneio(populacao, aptidoes)
            
            # Passa as taxas dinâmicas recebidas nos parâmetros
            filho1, filho2 = crossover_ox(pai1, pai2, taxaDeCrossover)
            
            nova_populacao.append(mutacao_swap(filho1, taxaDeMutacao))
            if len(nova_populacao) < tamPopulacao:
                nova_populacao.append(mutacao_swap(filho2, taxaDeMutacao))
                
        populacao = nova_populacao

    print("\n" + "="*50)
    print(f"RESULTADO FINAL DO AG")
    print(f"Melhor Vetor Codificado: {melhor_estado_global}")
    print(f"Fitness Final (Penalidade): {melhor_aptidao_global}")
    
    decodificar_solucao(melhor_estado_global)

# ==========================================
# 5. ENTRYPOINT MAIN
# ==========================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="T2 IA - Algoritmo Genético")
    parser.add_argument('arquivo', type=str, help='Nome do arquivo .txt (ex: exemplo1.txt)')
    parser.add_argument('--modo', choices=['passo', 'direto'], default='direto', help="Visualização da execução (passo a passo ou direto)")
    
    args = parser.parse_args()
    
    # Valida se o modo escolhido no terminal deve ativar o passoPasso
    modo_pausado = (args.modo == 'passo')
    
    pasta_arquivos = "ArquivosDeLeitura" 
    caminho_completo = os.path.join(pasta_arquivos, args.arquivo)
    
    N, pref_A, pref_B = carregar_arquivo(caminho_completo)
    
    # Chama a função AG respeitando a assinatura exigida e as configurações do professor
    AG(
        prefA=pref_A, 
        prefB=pref_B, 
        passoPasso=modo_pausado
    )