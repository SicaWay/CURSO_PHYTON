# ==============================================================================
# CADERNO DE DESAFIOS - AULA 6: ESTRUTURAS DE REPETIÇÃO (FOR / WHILE)
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo (Avaliação Prática)
# Perfil Técnico: Eduarda - Desenvolvedora Plena (Full Stack)
# ==============================================================================

# ==============================================================================
# AVALIAÇÃO DE DESEMPENHO E MOMENTO REFLEXÃO
# ==============================================================================
# Instrução da Eduarda: "Equipe, chegamos a um ponto crucial. Antes de codificar, 
# parem por 5 minutos. Lembra daquela pesquisa sobre a vaga de Full Stack na Aula 1? 
# Reflitam: O quanto você evoluiu em lógica, uso de variáveis e condicionais até aqui?
# Hoje, avaliarei a capacidade de vocês em criar rotinas automatizadas usando laços 
# de repetição (loops) sem travar os nossos servidores."


# ==============================================================================
# DESAFIO 1: Disparo de Mensagens via WhatsApp (Laço 'for')
# ==============================================================================
# Situação: A JWC está desenvolvendo um chatbot para o Senac RJ usando a API 
# do Whapi.Cloud. Eduarda precisa que você envie uma mensagem de boas-vindas 
# para uma lista de novos alunos.
# Enunciado: Crie uma lista chamada 'novos_alunos' com os nomes: "Ana", "Carlos", "Beatriz".
# Utilize um laço 'for' para percorrer a lista e imprimir: 
# "Enviando mensagem via Whapi.Cloud para: [Nome]"

# Código:
novos_alunos = ["Ana", "Carlos", "Beatriz"]

for aluno in novos_alunos:
    print(f"Enviando mensagem via Whapi.Cloud para: {aluno}")

# ==============================================================================
# DESAFIO 2: Tentativas de Reconexão do Agente IA (Laço 'while')
# ==============================================================================
# Situação: O agente de IA construído no Dialogflow ES perdeu a conexão com 
# o servidor principal. Ele deve tentar reconectar no máximo 3 vezes.
# Enunciado: Crie uma variável 'tentativas' iniciando em 1.
# Use um laço 'while' que rode enquanto as tentativas forem menores ou iguais a 3.
# Dentro do laço, imprima: "Tentativa de conexão Dialogflow: [numero da tentativa]"
# Não se esqueça de incrementar a variável 'tentativas' para evitar um loop infinito!

# Código:
tentativas = 1

while tentativas <=3:
    print(f"Tentativa de conexão Dialogflow: {tentativas}")

    tentativas += 1


# ==============================================================================
# DESAFIO 3: Filtro de Intenções (Intents) (Laço 'for' com 'if')
# ==============================================================================
# Situação: O webhook do Make.com recebeu várias intenções de usuários, mas 
# precisamos processar apenas a intenção "Matricula".
# Enunciado: Crie a lista 'intencoes' = ["Duvida", "Matricula", "Reclamacao", "Matricula"].
# Use um 'for' para percorrer a lista. Se a intenção for igual a "Matricula", 
# imprima "Processando fluxo de matrícula no Make.com...". 
# Caso contrário, imprima "Intenção ignorada."

# Código:
intencoes = ["Duvida", "Matricula", "Reclamacao", "Matricula"]

for intencao in intencoes:
    if intencao == "Matricula":
        print("Processando fluxo de matrícula no Make.com...")
    else:
        print("Intenção ignorada.")




# ==============================================================================
# DESAFIO 4: Menu Interativo de Automação (Simulação de 'Do-While')
# ==============================================================================
# Situação: Python não possui o comando 'do-while' nativo, mas Eduarda exige que 
# o menu rode pelo menos uma vez e continue rodando até o usuário pedir para sair.
# Enunciado: Use um 'while True:' para criar um loop infinito controlado.
# Dentro dele, crie uma variável 'opcao' que recebe um input do usuário: 
# "Digite 1 para iniciar o chatbot ou 0 para sair: "
# Se a opção for "0", imprima "Encerrando sistema..." e use o comando 'break' para parar o loop.
# Se for "1", imprima "Chatbot iniciado!".

# Código:


# ==============================================================================
# DESAFIO 5: Contagem Regressiva para Deploy (Função range)
# ==============================================================================
# Situação: O novo fluxo de integração contínua precisa de um aviso regressivo 
# no terminal antes de reiniciar os servidores.
# Enunciado: Utilize um laço 'for' combinado com a função 'range()' para imprimir 
# uma contagem regressiva de 5 até 1. Ao final, imprima "Servidor reiniciado!".
# Dica: range(inicio, parada, passo).

# Código:


# ==============================================================================
# ==============================================================================
# DESAFIOS OPCIONAIS (PARA ALUNOS AVANÇADOS)
# ==============================================================================
# ==============================================================================


# ==============================================================================
# DESAFIO 6 (OPCIONAL): Processamento de Fila com Interrupção Crítica
# ==============================================================================
# Situação: Um array contém os status das mensagens recebidas: 
# status_msg = ["ok", "ok", "erro_critico", "ok"].
# Enunciado: Faça um loop 'for' na lista. Se o status for "ok", imprima "Mensagem lida".
# Se encontrar "erro_critico", imprima "Falha no sistema! Abortando fila." e pare
# o loop imediatamente usando 'break'.

# Código:


# ==============================================================================
# DESAFIO 7 (OPCIONAL): Pular Dados Inválidos ('continue')
# ==============================================================================
# Situação: Durante a extração de dados (RAG Architecture) para alimentar a IA, 
# alguns documentos vieram vazios e devem ser ignorados.
# Enunciado: lista_docs = ["Doc1", "", "Doc3", "", "Doc5"]
# Use um 'for'. Se o documento for igual a "" (vazio), use o comando 'continue' 
# para pular para a próxima iteração. Caso contrário, imprima "Processando [Doc]".

# Código:


# ==============================================================================
# DESAFIO 8 (OPCIONAL): Calculadora de Custo de Tokens da API (While Acumulador)
# ==============================================================================
# Situação: Cada interação com a IA gera um custo de tokens. Eduarda pediu um 
# script que some os tokens até o limite de 1000 ser atingido.
# Enunciado: Variáveis 'total_tokens' = 0 e 'tokens_por_requisicao' = 250.
# Faça um 'while' que adicione 'tokens_por_requisicao' ao 'total_tokens' enquanto 
# o limite de 1000 não for atingido. Imprima o total a cada iteração.

# Código: