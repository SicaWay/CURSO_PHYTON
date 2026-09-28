# ==============================================================================
# DESAFIOS - AULA 7: TESTE DE MESA E PENSAMENTO COMPUTACIONAL
# ==============================================================================

# ==============================================================================
# 🧠 O QUE É UM "TESTE DE MESA"? (LEIA ANTES DE COMEÇAR!)
# ==============================================================================
# Olá, futuro(a) dev! 
# 
# Você já parou para pensar em como o computador executa o seu código? 
# Ele não lê o código todo de uma vez só! O computador executa UMA LINHA DE 
# CADA VEZ, de cima para baixo.
#
# O TESTE DE MESA é um exercício analítico onde VOCÊ finge ser o computador.
# Em vez de apenas apertar o botão "Play" e executar o script na IDE, você 
# acompanha no papel ou na tabela:
#   1. Qual linha está sendo executada.
#   2. Qual o valor exato armazenado em cada variável naquele momento.
#   3. O que realmente vai aparecer escrito na tela do monitor (print).
#
# Por que isso é importante?
# Na vida real de dev, 80% do tempo você estará LENDO e CORRIGINDO códigos que 
# já existem. Saber fazer um Teste de Mesa evita "bugs" e te ajuda a dominar 
# a lógica do programa!


# ==============================================================================
# 📌 EXEMPLO GUIADO (Aprenda como preencher):
# ==============================================================================
# Veja este pequeno trecho de código:
#
#   a = 5
#   b = 2
#   a = a + b
#   print("Resultado:", a)
#
# Como preencher o Teste de Mesa desse exemplo?
#
# 1️⃣ Rastreamento da Memória (Variáveis):
#    - Passo 1: 'a' recebe 5
#    - Passo 2: 'b' recebe 2
#    - Passo 3: 'a' vira 5 + 2 -> 'a' passa a valer 7
#
# 2️⃣ Saída na Tela (O que o print mostra?):
#    Resultado: 7
#
# Fácil, né? Agora é a sua vez! Siga o modelo abaixo em cada desafio.


# ==============================================================================
# DESAFIO 1: Inversão de Valores na Memória (Trocando Sessões)
# ==============================================================================
# Situação: Um script antigo da JWC precisa trocar os IDs de sessão entre dois 
# usuários no banco de dados sem criar uma terceira variável auxiliar.
# Enunciado: Faça o teste de mesa do código abaixo. Acompanhe os valores de 
# 'user1' e 'user2' linha por linha e escreva a saída final do terminal.

# Código (Aberto para visualização direta):
user1 = 10
user2 = 25
user1 = user1 + user2
user2 = user1 - user2
user1 = user1 - user2
print(f"User1: {user1} | User2: {user2}")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA (Preencha as lacunas):
#
# 🔄 EVOLUÇÃO DAS VARIÁVEIS NA MEMÓRIA:
#   - Linha 1 (user1 = 10)          -> user1 vale: 10 | user2 vale: None
#   - Linha 2 (user2 = 25)          -> user1 vale: 10 | user2 vale: 25
#   - Linha 3 (user1 = user1 + user2)-> user1 vale: 35 | user2 vale: 25
#   - Linha 4 (user2 = user1 - user2)-> user1 vale: 35 | user2 vale: 10
#   - Linha 5 (user1 = user1 - user2)-> user1 vale: 25 | user2 vale: 10
#
# 🖥️ SAÍDA NA TELA DO MONITOR (O que o print imprime):
#   User1 = 25 User2= 10


# ==============================================================================
# DESAFIO 2: Autenticação de API (Seguindo as Condicionais)
# ==============================================================================
# Situação: O gateway de autenticação do Senac RJ realiza checagens lógicas 
# com 'if', 'elif' e 'else' antes de liberar o acesso a um aluno.
# Enunciado: Avalie as condições lógicas abaixo e descubra qual bloco de texto 
# será exibido na tela.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO. 
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /) 
# para descomentar.

# Código:
# status = "inativo"
# tentativas = 3
# bloqueado = False
# 
# if tentativas >= 3:
#     bloqueado = True
# 
# if status == "ativo" and not bloqueado:
#     print("Acesso Permitido")
# elif status == "inativo" or bloqueado:
#     print("Acesso Negado: Conta retida")
# else:
#     print("Erro de sistema")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 ESTADO DAS VARIÁVEIS ANTES DOS 'IFs':
#   - status = "inativo"
#   - tentativas = 3
#   - bloqueado = True (Dica: O primeiro 'if tentativas >= 3' alterou essa variável?)
#
# ❓ AVALIAÇÃO DAS CONDIÇÕES:
#   - O 1º 'if' (status == "ativo" e não bloqueado) é Verdadeiro ou Falso? Falso
#   - O 2º 'elif' (status == "inativo" ou bloqueado) é Verdadeiro ou Falso? Verdadeiro
#
# 🖥️ SAÍDA NA TELA DO MONITOR:
Acesso Negado: Conta retedida 
#   ____________________________________________________


# ==============================================================================
# DESAFIO 3: Faturamento de Licenças (Somando no 'for')
# ==============================================================================
# Situação: O sistema financeiro percorre uma lista com as quantidades de 
# licenças vendidas para calcular o faturamento total da empresa.
# Enunciado: Acompanhe a variável acumuladora 'total' em CADA UMA das 4 voltas 
# que o laço 'for' der.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO. 
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /) 
# para descomentar.

# Código:
# vendas = [2, 0, 4, 1]
# preco_licenca = 50
# total = 0
# 
# for qtd in vendas:
#     if qtd > 0:
#         total = total + (qtd * preco_licenca)
# 
# print("Faturamento: R$", total)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 TELA DE RASTREAMENTO DO LAÇO (VOLTA POR VOLTA):
#   - 1ª Volta -> qtd = 2 | É maior que 0? (Sim) | Novo total = 0 + (2 * 50) = 100
#   - 2ª Volta -> qtd = 0 | É maior que 0? (Não) | Novo total = 100 + (0 *50) = 100
#   - 3ª Volta -> qtd = 4 | É maior que 0? (Sim) | Novo total = 100 + (4 * 50) = 100 + 200 = 300
#   - 4ª Volta -> qtd = 1 | É maior que 0? (Sim) | Novo total = 300 + (1 * 50) = 300 + (1 * 50) = 350
#
# 🖥️ SAÍDA NA TELA DO MONITOR:

#   Faturamento: R$ 350


# ==============================================================================
# DESAFIO 4: Paginação de Dados da API (Entendendo o 'while')
# ==============================================================================
# Situação: A API busca os alunos cadastrados no banco de 10 em 10 por página. 
# O laço 'while' roda enquanto ainda existirem registros para buscar.
# Enunciado: Acompanhe o valor de 'registros' e 'pagina' até que a condição do 
# 'while' se torne FALSA e o loop pare.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO. 
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /) 
# para descomentar.

# Código:
# registros = 25
# pagina = 1
# 
# while registros > 0:
#     print(f"Buscando página {pagina}")
#     registros = registros - 10
#     pagina = pagina + 1
# 
# print(f"Fim da busca. Restante: {registros}")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DAS ITERAÇÕES (REPETIÇÕES):
#   - Início: registros = 25 | pagina = 1
#
#   • Volta 1:
#       - O 'print' mostra: "Buscando página ____"
#       - Novo registros (25 - 10) = ____
#       - Nova pagina (1 + 1) = ____
#       - Teste do while: registros (___) > 0? (Sim/Não) ____
#
#   • Volta 2:
#       - O 'print' mostra: "Buscando página ____"
#       - Novo registros (___ - 10) = ____
#       - Nova pagina (___ + 1) = ____
#       - Teste do while: registros (___) > 0? (Sim/Não) ____
#
#   • Volta 3:
#       - O 'print' mostra: "Buscando página ____"
#       - Novo registros (___ - 10) = ____
#       - Nova pagina (___ + 1) = ____
#       - Teste do while: registros (___) > 0? (Sim/Não) ____ (O loop para aqui!)
#
# 🖥️ SAÍDA FINAL NA TELA (Escreva todas as linhas que o monitor vai mostrar):
#   1. _________________________________________________
#   2. _________________________________________________
#   3. _________________________________________________
#   4. _________________________________________________


# ==============================================================================
# DESAFIO 5: Monitoramento de Servidores (Usando 'break' e 'continue')
# ==============================================================================
# Situação: Um script varre uma lista de status de servidores.
# Lembrete Didático:
#   - 'continue': Pula o elemento atual e vai direto para a próxima volta do laço.
#   - 'break': Cancela e ENCERRA o laço imediatamente.
# Enunciado: Acompanhe a leitura da lista e descubra o que será impresso.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO. 
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /) 
# para descomentar.

# Código:
# servidores = ["ok", "alerta", "ok", "critico", "ok"]
# 
# for status in servidores:
#     if status == "alerta":
#         continue
#     if status == "critico":
#         print("Servidor crítico encontrado! Interrompendo...")
#         break
#     print(f"Servidor operando: {status}")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 PASSO A PASSO DA LEITURA DA LISTA:
#   - Item 1 ("ok"): O 'if' de alerta ignora? Sim. Imprime algo? _____________
#   - Item 2 ("alerta"): O 'continue' é acionado? O que acontece? ____________
#   - Item 3 ("ok"): Imprime algo? __________________________________________
#   - Item 4 ("critico"): O 'break' é acionado? O que é impresso? ___________
#   - Item 5 ("ok"): Chega a ser lido? Por quê? ______________________________
#
# 🖥️ SAÍDA EXATA NA TELA DO MONITOR:
#   ____________________________________________________________________
#   ____________________________________________________________________
#   ____________________________________________________________________


# ==============================================================================
# ==============================================================================
# DESAFIO OPCIONAL (PARA ALUNOS QUE QUEREM IR ALÉM)
# ==============================================================================
# ==============================================================================

# ==============================================================================
# DESAFIO 6 (OPCIONAL): Classificador de Tráfego de Rede (Módulo %)
# ==============================================================================
# Lembrete Didático: O operador `%` calcula o RESTO de uma divisão inteira.
# Exemplo: 4 % 2 dá resto 0 (pois 4 é par). 5 % 2 dá resto 1 (pois 5 é ímpar).
# Enunciado: Faça o teste de mesa para i variando de 1 até 5 no 'range(1, 6)'.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO. 
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /) 
# para descomentar.

# Código:
# for i in range(1, 6):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i, "-> Prioridade Máxima")
#     elif i % 2 == 0:
#         print(i, "-> Tráfego Par")
#     elif i % 3 == 0:
#         print(i, "-> Tráfego Múltiplo de 3")
#     else:
#         print(i, "-> Tráfego Normal")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 AVALIAÇÃO DE CADA VALOR DE 'i':
#   - i = 1 -> Qual condição entra? ______ | O que imprime? __________________
#   - i = 2 -> Qual condição entra? ______ | O que imprime? __________________
#   - i = 3 -> Qual condição entra? ______ | O que imprime? __________________
#   - i = 4 -> Qual condição entra? ______ | O que imprime? __________________
#   - i = 5 -> Qual condição entra? ______ | O que imprime? __________________