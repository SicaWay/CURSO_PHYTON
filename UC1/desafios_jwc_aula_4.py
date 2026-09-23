# ==============================================================================
# CADERNO DE DESAFIOS - AULA 4: GIT E ESTRUTURAS CONDICIONAIS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================

# ==============================================================================
# NOVO PERFIL PROFISSIONAL: Matheus - Analista DevSecOps (Líder de Infraestrutura)
# ==============================================================================
# Para agregar à equipe de desenvolvimento da JWC,
# apresentamos o cargo de Analista DevSecOps, liderado pelo Matheus.
# Responsabilidades: Matheus atua na interseção entre desenvolvimento 
# e operações (DevOps), garantindo automação, versionamento seguro e práticas de 
# segurança integradas ao código.
# Missão de hoje: Matheus avaliará como você lida com versionamento simultâneo na 
# nuvem e testará sua lógica com estruturas condicionais.


# ==============================================================================
# DESAFIO 1: Trabalho Simultâneo em Equipe (Comandos GIT Remoto)
# ==============================================================================
# Situação: Matheus iniciou o dia com o seguinte questionamento para a equipe: 
# "Como trabalhar com um código de forma simultânea com a equipe em máquinas 
# diferentes".
# Enunciado: Utilizando a função print, descreva o que fazem os seguintes 
# comandos de interação na criação de um repositório online:
# A) git clone
# B) git push
# C) git pull

# Código:
print( "A) git clone = É utilizado para baixar uma cópia completa de um repositório remoto para a máquina local.")
print ( "B) git push =  Serve para enviar alterações e commits salvos na maquina para o repositório remoto")

# ==============================================================================
# DESAFIO 2: Simulação de Desastres (Recuperação de Arquivos)
# ==============================================================================
# Situação: Durante o treinamento, Matheus pediu para que os alunos apaguem os 
# diretórios do projeto em sua máquina para simular uma falha.
# Enunciado: Matheus quer saber como você recuperaria o sistema. Sem 
# usar código Python de lógica, apenas responda em um print: Quais comandos 
# do Git você usaria para realizar a recuperação dos arquivos?

# Código:


# ==============================================================================
# DESAFIO 3: Controle de Acesso ao Servidor (Condicional if / else)
# ==============================================================================
# Situação: Matheus entregou uma lista de atividades focadas em estruturas 
# condicionais. A primeira tarefa é criar uma validação de acesso para 
# o banco de dados.
# Enunciado: Crie uma variável 'senha_digitada' e atribua o valor "DevSec2026". 
# Use a estrutura condicional if e else. Se a senha for igual a 
# "JWC@Admin", imprima "Acesso Liberado.". Caso contrário, imprima "Acesso Negado!".

# Código:
senha_digitada = "DevSec2026"
if senha_digitada == "JWC@Admin":
    print("Acesso Liberado.")
else:
    print("Acesso Negado!")


# ==============================================================================
# DESAFIO 4: Classificação de Ameaças (Condicionais if / elif / else)
# ==============================================================================
# Situação: O sistema da JWC (que atua na área de desenvolvimento de aplicações web) 
# recebe chamados de vulnerabilidades. Matheus exige que você domine as estruturas
# if, if else e if else if (que no Python usamos elif).
# Enunciado: Crie uma variável 'nivel_ameaca' valendo 3. 
# Crie a estrutura para verificar:
# - Se for 1: Imprima "Baixa: Adicionar ao Backlog da Sprint."
# - Se for 2: Imprima "Média: Desenvolvedor deve revisar hoje."
# - Se for 3: Imprima "Alta/Crítica: Acionar Matheus (DevSecOps) imediatamente!"
# - Para qualquer outro valor: Imprima "Nível não reconhecido."

# Código:
nivel_ameaca = 3
if 



# ==============================================================================
# DESAFIO 5: Menu de Ferramentas (Switch Case)
# ==============================================================================
# Situação: Para fechar a etapa de condicionais, você precisa demonstrar domínio 
# da estrutura Switch Case. Matheus quer um menu rápido no terminal 
# para rodar automações.
# Enunciado: Crie uma variável 'opcao_menu' valendo 2. Utilize a estrutura 
# `match-case` do Python (equivalente ao Switch Case) para avaliar a opção:
# Caso 1: "Iniciando varredura SAST no código fonte..."
# Caso 2: "Iniciando processo de sanitização de metadados..."
# Caso 3: "Gerando relatório OWASP de vulnerabilidades..."
# Caso Padrão (_): "Opção inválida. Tente novamente."

# Código:
