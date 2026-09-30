# ==============================================================================
# DESAFIOS - AULA 8: FUNÇÕES E PASSAGEM DE PARÂMETROS[span_0](start_span)[span_0](end_span)
# ==============================================================================
# ==============================================================================
# 🧠 O QUE SÃO "FUNÇÕES" E "PARÂMETROS"? (LEIA ANTES DE COMEÇAR!)[span_1](start_span)[span_1](end_span)
# ==============================================================================
# Olá, futuro(a) dev!
#
# Você já percebeu que copiar e colar o mesmo código várias vezes é ruim?
# Para resolver isso, utilizamos a modularização de sistemas através das FUNÇÕES[span_2](start_span)[span_2](end_span).
# Uma função é um bloco de código isolado que só roda quando é invocado[span_3](start_span)[span_3](end_span).
#
# Pense na função como uma máquina:
# 1. Você insere dados nela -> Esses são os PARÂMETROS (ou argumentos)[span_4](start_span)[span_4](end_span).
# 2. A máquina processa tudo -> Esse é o bloco de código interno.
# 3. Sai um resultado -> Esse é o seu RETORNO (return)[span_5](start_span)[span_5](end_span).
#
# O TESTE DE MESA em funções exige que você preste atenção para onde o
# valor está indo (quando a função é chamada) e o que ela devolve para
# o fluxo principal do programa.
# ==============================================================================
# 📌 EXEMPLO GUIADO (Aprenda como preencher):
# ==============================================================================
# Veja este pequeno trecho de código:
#
# def somar(a, b):
#     resultado = a + b
#     return resultado
#
# total = somar(5, 3)
# print("Total:", total)
#
# Como preencher o Teste de Mesa desse exemplo?
#
# 1️⃣ Rastreamento da Memória (Parâmetros e Retorno):
# - Passo 1: A função 'somar' é chamada passando os valores (5, 3).
# - Passo 2: O parâmetro 'a' recebe 5 e o 'b' recebe 3.
# - Passo 3: A variável 'resultado' vira 5 + 3 -> 8.
# - Passo 4: A função retorna 8, que é guardado na variável externa 'total'.
#
# 2️⃣ Saída na Tela (O que o print mostra?):
# Total: 8
#
# Fácil, né? Agora é a sua vez de testar os algoritmos de acordo com o cenário proposto[span_6](start_span)[span_6](end_span)!
# ==============================================================================
# DESAFIO 1: Saudação de Candidatos (Passagem de Parâmetros)[span_7](start_span)[span_7](end_span)
# ==============================================================================
# Situação: O sistema de Recursos Humanos da JWC envia mensagens automáticas
# para os candidatos que avançam nas etapas do processo seletivo para a vaga
# de Programador Full Stack[span_8](start_span)[span_8](end_span).
# Enunciado: Faça o teste de mesa acompanhando os valores que entram nos
# parâmetros 'nome' e 'vaga[span_9](start_span)'[span_9](end_span). Escreva a saída final.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /).
#
# Código:
# def enviar_saudacao(nome, vaga):
#     mensagem = f"Olá {nome}, você avançou na vaga de {vaga}!"
#     print(mensagem)
#
# candidato_atual = "Ana"
# enviar_saudacao(candidato_atual, "Full Stack")
# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA (Preencha as lacunas):
#
# 🔄 RASTREAMENTO DOS PARÂMETROS:
# - Quando a função é chamada, o parâmetro 'nome' recebe: "____"
# - O parâmetro 'vaga' recebe: "____"
# - A variável interna 'mensagem' passa a valer: "_________________________"
#
# 🖥️ SAÍDA NA TELA DO MONITOR (O que o print imprime):
# ____________________________________________________
# ==============================================================================
# DESAFIO 2: Cálculo de Bônus (Entendendo o 'return')[span_10](start_span)[span_10](end_span)
# ==============================================================================
# Situação: A JWC possui 20 colaboradores na equipe de desenvolvimento[span_11](start_span)[span_11](end_span).
# O diretor autorizou um cálculo automático de bônus salarial.
# Enunciado: Acompanhe como a função calcula o valor e como o 'return'
# devolve esse dado para a variável principal[span_12](start_span)[span_12](end_span).
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:
# def calcular_bonus(salario, percentual):
#     valor_bonus = salario * (percentual / 100)
#     return valor_bonus
#
# salario_dev = 5000
# bonus_recebido = calcular_bonus(salario_dev, 10)
# salario_final = salario_dev + bonus_recebido
# print(f"Salário Final: R$ {salario_final}")
# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DA FUNÇÃO:
# - Parâmetro 'salario' = ____ | Parâmetro 'percentual' = ____
# - Cálculo interno: valor_bonus = ____ * (____ / 100) = ____
# - O comando 'return' devolve o valor: ____
#
# 🔄 DE VOLTA AO CÓDIGO PRINCIPAL:
# - A variável 'bonus_recebido' armazena o retorno, logo vale: ____
# - A variável 'salario_final' = 5000 + ____ = ____
#
# 🖥️ SAÍDA NA TELA DO MONITOR:
# ____________________________________________________
# ==============================================================================
# DESAFIO 3: Reutilização de Código (Chamadas Múltiplas)[span_13](start_span)[span_13](end_span)
# ==============================================================================
# Situação: Um dos maiores benefícios das funções é a reutilização. O sistema
# da JWC precisa validar a senioridade baseada nos anos de experiência dos 
# novos programadores[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).
# Enunciado: Faça o teste de mesa para cada vez que a função for invocada.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:
# def definir_senioridade(anos):
#     if anos >= 5:
#         return "Sênior"
#     elif anos >= 2:
#         return "Pleno"
#     else:
#         return "Júnior"
#
# print("Ana:", definir_senioridade(6))
# print("Beto:", definir_senioridade(1))
# print("Carlos:", definir_senioridade(3))
# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 AVALIAÇÃO DAS CHAMADAS:
# - 1ª Chamada (anos = 6): 6 >= 5? (Sim/Não) ____ | Retorna: "________"
# - 2ª Chamada (anos = 1): 1 >= 5? (___) | 1 >= 2? (___) | Retorna: "________"
# - 3ª Chamada (anos = 3): 3 >= 5? (___) | 3 >= 2? (___) | Retorna: "________"
#
# 🖥️ SAÍDA FINAL NA TELA DO MONITOR:
# 1. _________________________________________________
# 2. _________________________________________________
# 3. _________________________________________________
# ==============================================================================
# DESAFIO 4: A Pegadinha do Escopo (Local vs Global)[span_16](start_span)[span_16](end_span)
# ==============================================================================
# Situação: Um candidato tentou alterar a pontuação de um teste prático
# diretamente dentro de um procedimento isolado, mas o recrutador notou um erro lógico[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span).
# Enunciado: Variáveis criadas DENTRO de uma função "morrem" quando a função
# acaba (escopo local). Rastreie os valores para entender por que a nota
# final não mudou fora da função!
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:
# nota = 50
#
# def adicionar_pontos(nota):
#     nota = nota + 20
#     print("Nota dentro da função:", nota)
#
# adicionar_pontos(nota)
# print("Nota fora da função:", nota)
# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DO ESCOPO:
# - Variável GLOBAL 'nota' inicial = ____
# - A função é chamada. O parâmetro LOCAL 'nota' recebe o valor: ____
# - Dentro da função, a nota LOCAL vira ____ + 20 = ____
# - O primeiro print (dentro da função) exibe: ___________________________
# - A função termina. A variável LOCAL é destruída da memória!
# - De volta ao código principal, a variável GLOBAL 'nota' ainda vale: ____
#
# 🖥️ SAÍDA NA TELA DO MONITOR (Escreva as duas linhas que vão aparecer):
# _________________________________________________
# _________________________________________________
# ==============================================================================
# DESAFIO 5: Funções que chamam Funções (Modularização)[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span)
# ==============================================================================
# Situação: O sistema da JWC precisa aplicar um desconto em um serviço web,
# mas antes deve validar se o cliente tem direito. A modularização de sistemas
# propõe dividir o problema em partes menores[span_21](start_span)[span_21](end_span)[span_22](start_span)[span_22](end_span).
# Enunciado: Acompanhe o fluxo de execução pulando de uma função para outra.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:
# def tem_desconto(tipo_cliente):
#     if tipo_cliente == "Parceiro":
#         return True
#     return False
#
# def calcular_preco(preco_base, tipo_cliente):
#     if tem_desconto(tipo_cliente):
#         return preco_base - 100
#     else:
#         return preco_base
#
# preco_final = calcular_preco(500, "Parceiro")
# print("Preço cobrado: R$", preco_final)
# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 PASSO A PASSO DO FLUXO DE EXECUÇÃO:
# - 1. O código chama 'calcular_preco' passando os parâmetros (500, "Parceiro").
# - 2. Dentro de 'calcular_preco', o 'if' invoca a função 'tem_desconto("Parceiro")'.
# - 3. Entra em 'tem_desconto'. O tipo é "Parceiro"? (Sim/Não) ____
# - 4. A função 'tem_desconto' devolve o retorno: (True/False) ________
# - 5. De volta ao 'if' de 'calcular_preco', a condição é Verdadeira!
# - 6. Retorna preco_base (____) - 100 = ____
# - 7. A variável 'preco_final' recebe o valor: ____
#
# 🖥️ SAÍDA EXATA NA TELA DO MONITOR:
# ____________________________________________________________________
# ==============================================================================
# ==============================================================================
# DESAFIO OPCIONAL (PARA ALUNOS QUE QUEREM IR ALÉM)
# ==============================================================================
# ==============================================================================
# ==============================================================================
# DESAFIO 6 (OPCIONAL): Parâmetros Opcionais (Default)[span_23](start_span)[span_23](end_span)
# ==============================================================================
# Lembrete Didático: Em Python, você pode definir um valor "padrão" para um
# parâmetro. Se quem chamar a função não enviar esse dado, a função usa o padrão!
# Enunciado: Avalie as duas chamadas da mesma função abaixo e descubra a saída.
#
# Código:
# def criar_perfil(nome, nivel="Júnior"):
#     print(f"Dev: {nome} | Nível: {nivel}")
#
# criar_perfil("Carlos", "Pleno")
# criar_perfil("Marina")
# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 AVALIAÇÃO DAS CHAMADAS:
# - Chamada 1: nome="Carlos", nivel enviado="Pleno". Imprime: _________________
# - Chamada 2: nome="Marina", nivel enviado=Nenhum. Usa o padrão: "_______".
#              Imprime: _______________________________________________________