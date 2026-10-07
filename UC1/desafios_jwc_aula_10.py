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
