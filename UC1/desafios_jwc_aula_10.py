# ===============================================================================
# EMPRESA JWC TECNOLOGIA - PROCESSO SELETIVO: ETAPA DE MATRIZES (AULA 10)
# ===============================================================================
# Instruções: Desenvolva o código Python correspondente para resolver cada um dos
# desafios propostos abaixo. Não utilize bibliotecas externas (como numpy).
# ===============================================================================

# -------------------------------------------------------------------------------
# DESAFIO 1: Validador de Quadrado Mágico 3x3
# -------------------------------------------------------------------------------
# Cenário: A equipa de desenvolvimento da JWC necessita de um algoritmo para 
# validar a mecânica de jogos de lógica baseados em grelhas.

# Requisitos do Programa:
# 1. Solicite ao utilizador que insira os valores para preencher uma matriz 3x3 
#    com números inteiros.
# 2. Crie uma função para verificar se a matriz forma um Quadrado Mágico. 
#    - Para ser um Quadrado Mágico, a soma de cada uma das 3 linhas, de cada uma 
#      das 3 colunas e das 2 diagonais (principal e secundária) deve ser igual.
# 3. Exiba a matriz digitada de forma organizada e mostre a mensagem informando 
#    se ela É ou NÃO É um Quadrado Mágico.

# Código :

 

def verificar_quadrado_magico(matriz):
    """
    Verifica se uma matriz 3x3 é um Quadrado Mágico.
    Retorna True se for um Quadrado Mágico, caso seja o contrário False.
    """
# 1. Soma da primeira linha como referência para comparar com o restante
    soma_referencia = sum(matriz[0])

# 2. Verificar a soma de todas as linhas
# Se a soma de qualquer linha for diferente da referência deve interromper a execução e retorna False.
    for linha in matriz:
        if sum(linha) != soma_referencia:
            return False

# 3. Verificar a soma de todas as colunas 
# O range(3) gera a sequência 0, 1, 2. 
# A cada volta do laço, acessa verticalmente os três elementos da coluna atual e verifica a soma.
    for coluna in range(3):
        soma_coluna = matriz[0][coluna] + matriz[1][coluna] + matriz[2][coluna]
        if soma_coluna != soma_referencia:
            return False

# 4. Verificar a soma da diagonal principal
# Soma os elementos em que os índices de linha e coluna são iguais - [0][0],[1][1] e [2][2]
    soma_diagonal_principal = matriz[0][0] + matriz[1][1] + matriz[2][2]
    if soma_diagonal_principal != soma_referencia:
        return False

# 5. Verificar a soma da diagonal secundária
# Soma os elementos que cruzam a matriz no sentido oposto - topo direito ao fundo esquerdo
    soma_diagonal_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]
    if soma_diagonal_secundaria != soma_referencia:
        return False

# Se passou por todas as validações, é um Quadrado Mágico
    return True

# Responsavel por mostrar os dados no terminal
def exibir_matriz(matriz): # Percorre cada linha da matriz e exibe os elementos de forma organizada
    """Exibe a matriz 3x3 formatada de forma visual organizada."""
    print("\n--- MATRIZ INSERIDA ---")
    for linha in matriz:
        print(f"[ {linha[0]:^3} {linha[1]:^3} {linha[2]:^3} ]") # linha[0]:^3: O especificador de formatação, :^3, centraliza o valor dentro de um espaço de 3 caracteres.
    print("-----------------------")

# Responsavel por executar o programa principal
def main():
    print("=== VALIDADOR DE QUADRADO MÁGICO 3x3 ===")
    matriz = []

    # Leitura dos valores fornecidos pelo usuário para preencher a matriz 3x3
    for i in range(3):
        linha = []
        print(f"\nDigite os elementos da Linha {i + 1}:")
        for j in range(3):
            numero = int(input(f"  Elemento [{i + 1}][{j + 1}]: "))
            linha.append(numero)
        matriz.append(linha)

    # Exibição da matriz
    exibir_matriz(matriz)

    # Validação e exibição do resultado final
    if verificar_quadrado_magico(matriz):
        print("RESULTADO: A matriz É um Quadrado Mágico! ")
    else:
        print("RESULTADO: A matriz NÃO É um Quadrado Mágico.")


# Executa o programa principal
if __name__ == "__main__":
    main()




# -------------------------------------------------------------------------------
# DESAFIO 2: Protótipo de Batalha Naval (Matriz 5x5)
# -------------------------------------------------------------------------------
# Cenário: A divisão de jogos da JWC precisa de prototipar a lógica de acertos e 
# erros num tabuleiro bidimensional para um jogo de Batalha Naval.

# Requisitos do Programa:
# 1. Crie uma matriz 5x5 inicializada com 0s (representando 'água').
# 2. Posicione previamente 3 navios na matriz utilizando o valor 1 em posições 
#    fixas ou aleatórias.
# 3. Implemente um loop de jogadas que:
#    - Solicite ao jogador a linha (0 a 4) e a coluna (0 a 4) do disparo.
#    - Verifique se a jogada acertou na água (0) ou num navio (1).
#    - Exiba o tabuleiro atualizado a cada ronda (mantendo os navios ocultos até 
#      serem atingidos).
# 4. O jogo termina quando todos os navios forem destruídos ou o limite de 
#    tentativas for atingido.

# Código:
import random

# ===============================================================================
# DESAFIO 2: Protótipo de Batalha Naval (Matriz 5x5)
# ===============================================================================

def criar_tabuleiro(tamanho=5):
    """Cria e retorna uma matriz 5x5 preenchida com 0 (água)."""
    return [[0 for _ in range(tamanho)] for _ in range(tamanho)]

def posicionar_navios(tabuleiro, quantidade=3):
    """Posiciona 'quantidade' navios (valor 1) em posições aleatórias da matriz."""
    tamanho = len(tabuleiro)
    navios_posicionados = 0
    
    while navios_posicionados < quantidade:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        
        # Só posiciona se o local ainda for água (0)
        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = 1
            navios_posicionados += 1

def exibir_tabuleiro(tabuleiro_visivel):
    """
    Exibe o tabuleiro para o jogador ocultando posições não reveladas.
    '~' = Água não revelada
    'O' = Disparo na água (Erro)
    'X' = Navio atingido (Acerto)
    """
    print("\n   0  1  2  3  4 (Colunas)")
    print("  -----------------")
    for i, linha in enumerate(tabuleiro_visivel):
        linha_fmt = "  ".join(linha)
        print(f"{i}| {linha_fmt}")
    print("  -----------------")

def main():
    TAMANHO = 5
    TOTAL_NAVIOS = 3
    MAX_TENTATIVAS = 8
    
    # 1. Matriz real (onde ficam os navios secretos: 0 = água, 1 = navio)
    tabuleiro_secreto = criar_tabuleiro(TAMANHO)
    posicionar_navios(tabuleiro_secreto, TOTAL_NAVIOS)
    
    # 2. Matriz visível para o jogador (inicia toda com '~')
    tabuleiro_visivel = [["~" for _ in range(TAMANHO)] for _ in range(TAMANHO)]
    
    navios_restantes = TOTAL_NAVIOS
    tentativas = 0
    
    print("=== BATALHA NAVAL JWC (MATRIZ 5x5) ===")
    print(f"Objetivo: Encontrar os {TOTAL_NAVIOS} navios escondidos.")
    print(f"Você tem {MAX_TENTATIVAS} tentativas!")
    
    # 3. Loop principal de jogadas
    while tentativas < MAX_TENTATIVAS and navios_restantes > 0:
        exibir_tabuleiro(tabuleiro_visivel)
        print(f"\nTentativa {tentativas + 1} de {MAX_TENTATIVAS} | Navios restantes: {navios_restantes}")
        
        # Leitura e validação das coordenadas
        try:
            linha = int(input("Digite a Linha (0 a 4): "))
            coluna = int(input("Digite a Coluna (0 a 4): "))
        except ValueError:
            print(" Entradas inválidas! Digite apenas números inteiros entre 0 e 4.")
            continue
            
        if not (0 <= linha < TAMANHO and 0 <= coluna < TAMANHO):
            print(" Coordenada fora do tabuleiro! Escolha números entre 0 e 4.")
            continue
            
        # Verifica se a posição já foi jogada antes
        if tabuleiro_visivel[linha][coluna] != "~":
            print(" Você já atirou nessa posição! Tente outra coordenada.")
            continue
            
        # Contabiliza a tentativa válida
        tentativas += 1
        
        # Checa acerto ou erro
        if tabuleiro_secreto[linha][coluna] == 1:
            print(" ACERTOU! Um navio foi atingido!")
            tabuleiro_visivel[linha][coluna] = "X"
            navios_restantes -= 1
        else:
            print(" ÁGUA! Nenhum navio nessa posição.")
            tabuleiro_visivel[linha][coluna] = "O"

    # Exibição do tabuleiro final
    exibir_tabuleiro(tabuleiro_visivel)
    
    # Fim de jogo
    if navios_restantes == 0:
        print(f"\n PARABÉNS! Você destruiu todos os {TOTAL_NAVIOS} navios em {tentativas} tentativas!")
    else:
        print("\n FIM DE JOGO! Suas tentativas acabaram.")
        print("Localização dos navios no tabuleiro secreto (1 = Navio):")
        for linha in tabuleiro_secreto:
            print(" ".join(map(str, linha)))

if __name__ == "__main__":
    main()


# -------------------------------------------------------------------------------
# DESAFIO 3: Relatório de Produtividade Semanal (Matriz 4x5)
# -------------------------------------------------------------------------------
# Cenário: A gerência da JWC precisa de monitorizar o desempenho semanal de 4 
# programadores em cada um dos 5 dias úteis da semana.

# Requisitos do Programa:
# 1. Crie uma matriz 4x5 (4 linhas para os programadores: Dev 1 a Dev 4; 
#    5 colunas para os dias: Segunda a Sexta).
# 2. Peça ao utilizador para preencher a matriz com a quantidade de tarefas 
#    concluídas por cada programador em cada dia.
# 3. Exiba a matriz formatada como uma tabela de produtividade.
# 4. Calcule e apresente:
#    - O total de tarefas concluídas por cada programador no final da semana.
#    - Qual foi o dia da semana em que a equipa teve a maior produtividade somada.
# ===============================================================================

#Código:
# ===============================================================================
# DESAFIO 3: Relatório de Produtividade Semanal (Matriz 4x5)
# ===============================================================================

def preencher_matriz(programadores, dias):
    """Lê do usuário a quantidade de tarefas de cada programador em cada dia."""
    matriz = []
    print("=== REGISTO DE TAREFAS SEMANAIS ===\n")
    
    for i, dev in enumerate(programadores):
        linha = []
        print(f"📌 {dev}:")
        for j, dia in enumerate(dias):
            while True:
                try:
                    tarefas = int(input(f"   Tarefas na {dia}: "))
                    if tarefas < 0:
                        print("   ⚠️ Digite um valor maior ou igual a zero.")
                        continue
                    linha.append(tarefas)
                    break
                except ValueError:
                    print("   ⚠️ Entrada inválida! Digite um número inteiro.")
        matriz.append(linha)
        print()
    return matriz


def exibir_relatorio(matriz, programadores, dias):
    """Exibe a matriz formatada em tabela e calcula o total por programador."""
    totais_devs = []
    
    print("\n" + "=" * 65)
    print("=== RELATÓRIO DE PRODUTIVIDADE SEMANALE ===")
    print("=" * 65)
    
    # Cabeçalho da tabela
    cabecalho = f"{'Programador':<15} | " + " | ".join(f"{dia:^7}" for dia in dias) + " | Total"
    print(cabecalho)
    print("-" * len(cabecalho))
    
    # Linhas dos programadores
    for i, dev in enumerate(programadores):
        total_dev = sum(matriz[i])
        totais_devs.append(total_dev)
        
        tarefas_fmt = " | ".join(f"{matriz[i][j]:^7}" for j in range(len(dias)))
        print(f"{dev:<15} | {tarefas_fmt} | {total_dev:^5}")
        
    print("-" * len(cabecalho))
    return totais_devs


def calcular_produtividade_dias(matriz, dias):
    """Calcula a produtividade total da equipe em cada dia e indica o dia mais produtivo."""
    totais_dias = []
    
    for col in range(len(dias)):
        soma_dia = sum(matriz[linha][col] for linha in range(len(matriz)))
        totais_dias.append(soma_dia)
        
    # Encontra o maior valor e o dia correspondente
    maior_produtividade = max(totais_dias)
    indice_maior = totais_dias.index(maior_produtividade)
    dia_mais_produtivo = dias[indice_maior]
    
    return totais_dias, dia_mais_produtivo, maior_produtividade


def main():
    programadores = ["Dev 1", "Dev 2", "Dev 3", "Dev 4"]
    dias = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
    
    # 1. Leitura dos dados
    matriz = preencher_matriz(programadores, dias)
    
    # 2. Exibição do relatório e totais por programador
    totais_devs = exibir_relatorio(matriz, programadores, dias)
    
    # 3. Cálculo do dia de maior produtividade
    totais_dias, dia_top, valor_top = calcular_produtividade_dias(matriz, dias)
    
    # 4. Apresentação dos resultados finais
    print("\n RESUMO DOS RESULTADOS:\n")
    print("1. Total de tarefas concluídas por programador:")
    for dev, total in zip(programadores, totais_devs):
        print(f"   • {dev}: {total} tarefas")
        
    print(f"\n2. Dia de MAIOR produtividade da equipe:")
    print(f"    {dia_top} com um total de {valor_top} tarefas concluídas!")
    print("=" * 65)


if __name__ == "__main__":
    main()