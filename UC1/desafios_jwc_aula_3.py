# ==============================================================================
# CADERNO DE DESAFIOS - AULA 3: GIT E EXPRESSÕES ARITMÉTICAS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================

# ==============================================================================
# DESAFIO 1: O Onboarding com a Tech Lead (O Mundo do GIT)
# ==============================================================================
# Situação: No seu primeiro dia focado em código, a Patrícia (Líder Técnica) 
# avisa que não aceita código perdido. Antes de você programar a regra de 
# negócio do cliente, ela quer garantir que você entende de versionamento.
# Enunciado: Faça uma breve pesquisa e responda (usando a função print):
# A) Quem criou o Git e o GitHub?[cite: 2]
# B) Para qual empresa o GitHub foi vendido e por qual valor aproximado?[cite: 2]
# C) Cite o nome de pelo menos dois outros subversionadores (concorrentes do GitHub) 
#    usados no mercado.[cite: 2]
# Código:
print("A) O Git foi criado por Linus Torvalds em 2005, já o GitHub foi criado por Tom Preston-Werner, Chris Wanstrath, PJ Hyett e Scott Chacon em 2008.")
print("B) O GitHub foi vendido para a Microsoft em 2018 por cerca de 7,5 bilhões de dólares.")
print("C) O GitLab e o Bitbucket.")

# ==============================================================================
# DESAFIO 2: O Padrão da Empresa (Comandos GIT)
# ==============================================================================
# Situação: A Patrícia criou um manual de boas práticas da JWC. Todo desenvolvedor 
# precisa saber o fluxo básico para salvar o código na nuvem e evitar desastres. 
# Enunciado: Sem usar código Python, escreva dentro de prints quais são os 
# comandos do GIT responsáveis por:
# 1. Iniciar um novo repositório local na sua máquina.[cite: 2]
# 2. Verificar o estado atual dos arquivos (o que foi alterado).[cite: 2]
# 3. Adicionar arquivos para a "área de preparação" para serem salvos.[cite: 2]
# 4. Salvar as alterações criando um ponto na história (com uma mensagem).[cite: 2]

# Código:
print("1. Iniciar um repositório local: git init e git clone")
print("2. Verificar o estado dos arquivos: git status e git status -s")
print("3. Adicionar arquivos para preparação: git add e git add -A .")
print("4. Salvar alterações na história: git commit -m \"Olá\" e git commit -am \"Olá\"")

# git in = cria repositório do zero; git clone = copia um repositório existente da nuvem para sua maquina
# git status = visão geral; git status -s = visão resumida 
# git add = adiciona todas as alterações na pasta atual; git add -A =  adiciona todos os arquivos modificados no projeto
# git commit -m "mensagem" = mais utilizada; git commit -am "mensagem" ou git commit -a -m "mensagem" = -a = faz o git add automático para arquivos que já são rastreados pelo Git que foram modificados ou deletados, -m = inclui a mensagem.

# ==============================================================================
# DESAFIO 3: A Primeira Feature (Operador de Subtração -)
# ==============================================================================
# Situação: O Arthur (Product Owner) chegou com uma demanda de um cliente da 
# área de educação[cite: 2]. O sistema precisa mostrar no painel da diretoria 
# quantas vagas ainda estão disponíveis na escola.
# Enunciado: Como desenvolvedor, crie uma variável 'capacidade_total_escola' 
# valendo 850. Crie 'alunos_matriculados' valendo 523. O sistema deve calcular 
# a variável 'vagas_disponiveis' subtraindo os matriculados da capacidade total. 
# Imprima o resultado na tela.

# Código:
capacidade_total_escola = 850
alunos_matriculados = 523
vagas_disponiveis = capacidade_total_escola - alunos_matriculados
print(f"Vagas disponíveis na escola: {vagas_disponiveis}")


# ==============================================================================
# DESAFIO 4: Calculando o Faturamento (Operador de Multiplicação *)
# ==============================================================================
# Situação: O Arthur (PO) pediu para você criar a funcionalidade que projeta o 
# faturamento do mês seguinte, multiplicando o número de alunos pela mensalidade.
# Enunciado: Crie a variável 'mensalidade_padrao' valendo 850.50. Crie a variável 
# 'novas_matriculas' valendo 42. Crie a variável 'faturamento_projetado' que 
# multiplique os dois valores e exiba o resultado para o cliente.

# Código:
mensalidade_padrao = 850.50
novas_matriculas = 42
faturamento_projetado = mensalidade_padrao * novas_matriculas
print(f"O faturamento projetado para as novas matrículas é de R$ {faturamento_projetado:.2f}")


# ==============================================================================
# DESAFIO 5: Divisão de Turmas (Operador de Divisão /)
# ==============================================================================
# Situação: O sistema precisa de um botão "Gerar Grupos de Estudo". O Arthur (PO) 
# definiu que a regra de negócio é dividir o total de alunos de uma turma pelo 
# tamanho ideal do grupo.
# Enunciado: Crie 'total_alunos_turma' valendo 45. Crie 'tamanho_grupo_ideal' 
# valendo 5. Calcule e imprima quantos grupos serão formados usando a divisão (/).
# (Note que no Python, a divisão normal sempre retorna um número quebrado - float).

# Código:
total_alunos_turma = 45
tamanho_grupo_ideal = 5
grupos_formados = total_alunos_turma / tamanho_grupo_ideal
print(f"Serão formados {grupos_formados} grupos de estudo.")

# ==============================================================================
# DESAFIO 6: Lógica de Paginação (Divisão Inteira // e Resto %)
# ==============================================================================
# Situação: O cliente educacional comprou 100 tablets. O sistema precisa 
# distribuir esses tablets igualmente entre 3 salas, mas a Patrícia (Tech Lead) 
# avisa: "O sistema não pode quebrar um tablet no meio!".
# Enunciado: Você precisa usar a divisão inteira (//) para descobrir quantos 
# tablets inteiros vão para cada sala. Depois, use o resto da divisão (%) para 
# programar a variável 'tablets_sobra' e avisar quantos ficam na reserva da TI. 
# Imprima ambos os resultados.

# Código:
total_tablets = 100
total_salas = 3
tablets_por_sala = total_tablets // total_salas
tablets_sobra = total_tablets % total_salas
print(f"Cada sala receberá: {tablets_por_sala} tablets")
print(f"Tablets na reserva da TI (sobra): {tablets_sobra}")

# ==============================================================================
# DESAFIO 7: Escalabilidade de Servidor (Exponenciação **)
# ==============================================================================
# Situação: A Patrícia (Tech Lead) precisa configurar os servidores da AWS para 
# suportar o novo sistema educacional. Ela sabe que a base de dados dobra de 
# tamanho a cada ano.
# Enunciado: Crie a variável 'armazenamento_atual_tb' valendo 3. Como o volume 
# dobra anualmente, calcule o tamanho necessário para daqui a 4 anos elevando 
# 2 à 4ª potência (**). Multiplique o resultado pelo armazenamento atual e imprima.

# Código:
armazenamento_atual_tb = 3
anos = 4 
fator_crescimento = 2 ** anos
armazenamento_futuro_tb = armazenamento_atual_tb * fator_crescimento
print(f"Armazenamento necessário após {anos} anos: {armazenamento_futuro_tb} TB")

# ==============================================================================
# DESAFIO 8: O MVP do Boletim Digital (Projeto Final da Aula 3)
# ==============================================================================
# Situação: Sprint final! O Arthur (PO) precisa apresentar o Produto Mínimo 
# Viável (MVP) funcionando. A funcionalidade principal é o cálculo da média 
# do aluno pelo professor[cite: 2].
# Regra da Patrícia: "O sistema não pode ter valores fixos. O usuário (professor) 
# é quem deve digitar os dados no terminal."
# Enunciado: 
# 1. Use input() para capturar o nome do aluno.
# 2. Use input() para capturar as notas do 1º, 2º e 3º trimestre (lembre-se 
#    de aplicar a conversão float() para que o Python entenda como matemática).
# 3. Calcule a média somando as 3 notas e dividindo por 3. (Cuidado com a 
#    ordem de precedência matemática: use parênteses!).
# 4. Exiba o resultado formatado (f-string) na tela para o professor: 
#    "Sistema JWC: O aluno [nome] fechou o ano com média [media]".

# Código:
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota do 1º trimestre: "))
nota2 = float(input("Digite a nota do 2º trimestre: "))
nota3 = float(input("Digite a nota do 3º trimestre: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Sistema JWC: O aluno {nome_aluno} fechou o ano com média {media:.2f}")
