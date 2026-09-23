# ==============================================================================
# CADERNO DE DESAFIOS - AULA 5: OPERADORES LÓGICOS E ESTRUTURAS CONDICIONAIS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================

# ==============================================================================
# PERFIL PROFISSIONAL: Eduarda - Desenvolvedora Plena (Full Stack)
# ==============================================================================
# Para integrar a equipe de desenvolvimento da JWC Tecnologia,
# apresentamos a Desenvolvedora Pleno Eduarda.
# Responsabilidades: Eduarda é responsável por construir código limpo e eficiente,
# realizar Code Reviews (revisões de código), orientar novos desenvolvedores
# e garantir que as regras de negócio das aplicações funcionem sem erros.
# Missão de hoje: Eduarda avaliará sua capacidade de construir expressões lógicas 
# claras, sem redundâncias, utilizando os operadores 'and', 'or' e 'not' combinados 
# com estruturas condicionais (if / elif / else / match-case).

# ==============================================================================
# DESAFIO 1: Validação de Acesso ao Módulo LMS (Operador 'and')
# ==============================================================================
# Situação: Eduarda está revisando o módulo de cursos da JWC. Um aluno só pode 
# acessar as aulas avançadas se tiver mais de 18 anos E possuir matrícula ativa.
# Enunciado: Crie as variáveis 'idade' (int) com valor 20 e 'matricula_ativa' (bool) 
# com valor True. Escreva uma estrutura 'if/else' com o operador 'and'.
# Se ambas as condições forem verdadeiras, imprima "Acesso liberado ao módulo avançado.".
# Caso contrário, imprima "Acesso negado: Requisitos não preenchidos.".

# Código:
idade = 20
matricula_ativa = True

if idade > 18 and matricula_ativa:
    print("Acesso liberado ao módulo avançado.")
else: 
    print ("Acesso negado: Requisitos não preenchidos.")

# ==============================================================================
# DESAFIO 2: Triagem de Mensagens no Chatbot (Operador 'or')
# ==============================================================================
# Situação: Eduarda está desenvolvendo o robô de atendimento da JWC em Python.
# O robô deve redirecionar a conversa para um atendente humano se o cliente
# digitar a palavra "suporte" OU a palavra "financeiro".
# Enunciado: Crie uma variável 'mensagem_cliente' com o texto "Quero falar com o suporte".
# Use a estrutura 'if/else' com o operador 'or' para verificar se a palavra "suporte"
# OU "financeiro" está presente na mensagem.
# Se verdadeiro, imprima "Transferindo para um atendente humano...".
# Caso contrário, imprima "Atendimento automatizado em andamento.".

# Código:
mensagem_cliente = "Quero falar com o suporte"

if "suporte" in mensagem_cliente or "financeiro" in mensagem_cliente:
    print("Transferindo para um atendente humano...")
else:
    print("Atendimento automatizado em adamento.")

# ==============================================================================
# DESAFIO 3: Status de Manutenção do Sistema (Operador 'not')
# ==============================================================================
# Situação: Eduarda quer garantir que rotinas de atualização só rodem quando 
# o servidor NÃO estiver sob carga de manutenção.
# Enunciado: Crie a variável 'em_manutencao' com o valor False.
# Utilize a estrutura 'if/else' com o operador 'not' para verificar se o sistema
# NÃO está em manutenção.
# Se for verdadeiro (não está em manutenção), imprima "Servidor operacional. Iniciando rotina.".
# Caso contrário, imprima "Sistema em manutenção. Tente novamente mais tarde.".

# Código:
em_manutencao = False
if not em_manutencao:
    print("Servidor operacional. Iniciando rotina.")
else:
    print("Sistema em manutenção. Tente movamente mais tarde.")

# ==============================================================================
# DESAFIO 4: Emissão de Certificado de Conclusão (Operadores 'and' e 'not')
# ==============================================================================
# Situação: No portal do aluno da JWC, a emissão do certificado exige que o 
# aluno tenha nota maior ou igual a 7.0 E NÃO possua pendências na secretaria.
# Enunciado: Crie as variáveis 'nota_final' valendo 8.5 e 'possui_pendencia' valendo False.
# Use 'if' com 'and' e 'not' para validar a regra.
# Se a nota for >= 7.0 E NÃO possuir pendência, imprima "Certificado emitido com sucesso!".
# Caso contrário, imprima "Emissão bloqueada. Verifique suas pendências ou nota.".

# Código:
nota_final = 8.5
possui_pendencia = False
if nota_final >= 7.0 and not possui_pendencia:
    print("Certificado emitido com sucesso!")
else:
    print("Emissão bloqueada.Verifique suas pendências ou nota.")

# ==============================================================================
# DESAFIO 5: Classificação de Desempenho do Código (if / elif / else com 'and')
# ==============================================================================
# Situação: Durante o Code Review, Eduarda mede o tempo de resposta das requisições 
# em milissegundos (ms) para garantir a qualidade do sistema.
# Enunciado: Crie a variável 'tempo_resposta_ms' com o valor 250.
# Estruture as condicionais usando 'if', 'elif' e 'else' com operadores lógicos:
# - Se tempo_resposta_ms < 100: "Excelente performance."
# - Se tempo_resposta_ms >= 100 E tempo_resposta_ms <= 300: "Performance aceitável."
# - Se tempo_resposta_ms > 300: "Atenção: Código precisa de otimização!"

# Código:
tempo_resposta_ms = 250
if  tempo_resposta_ms < 100:
    print("Excelente performance.")
elif tempo_resposta_ms >= 100 and tempo_resposta_ms <= 300:
    print("Performance aceitável.")
else: 
    print("Atenção: Código precisa de otimização!")


# ==============================================================================
# DESAFIO 6: Liberação de Bônus de Projeto (Operadores mistos 'or' e 'and')
# ==============================================================================
# Situação: A JWC concede um bônus aos desenvolvedores que realizarem mais de 
# 20 horas extras no mês OU (entregarem mais de 5 projetos E tirarem nota de avaliação > 8).
# Enunciado: Crie as variáveis 'horas_extras' (15), 'projetos_entregues' (6) e 
# 'nota_avaliacao' (9.0).
# Monte uma estrutura 'if/else' utilizando parênteses para organizar a precedência 
# dos operadores 'or' e 'and'.
# Imprima "Colaborador elegível para bônus!" ou "Critérios de bônus não atingidos.".

# Código:
horas_extras = 15
projetos_entregues = 6 
nota_avaliacao = 9.0

if horas_extras > 20 or (projetos_entregues > 5 and nota_avaliacao > 8.0):
    print("Colaborador elegível para bônus!")
else:
    print("Critérios de bônus não atingidos.")


# ==============================================================================
# DESAFIO 7: Validação de Cadastro de Usuário (Análise de Strings com 'and')
# ==============================================================================
# Situação: Eduarda pediu para você criar uma regra simples para validar o nome 
# de usuário no cadastro do sistema.
# Enunciado: Crie a variável 'usuario' com o valor "dev_python".
# Use 'if/else' com 'and' para checar duas coisas:
# 1. Se o tamanho do nome de usuário é maior que 3 caracteres (use len(usuario) > 3).
# 2. Se o nome de usuário não contém espaços em branco (use ' ' not in usuario).
# Imprima "Nome de usuário válido!" ou "Nome de usuário inválido.".

# Código:
usuario = "dev_python"
if len(usuario) > 3 and ' ' not in usuario:
    print("Nome de usuário válido!")   
else:
    print("Nome de usuário inválido.")

# ==============================================================================
# DESAFIO 8: Menu de Feedback de Code Review (Match-Case)
# ==============================================================================
# Situação: Eduarda classifica os retornos de Code Review em níveis para orientar a equipe.
# Enunciado: Crie uma variável 'codigo_status' com o valor 2.
# Utilize a estrutura 'match-case' para avaliar a opção:
# - Caso 1: "Aprovado: Código limpo e pronto para produção."
# - Caso 2: "Aprovado com ressalvas: Ajustar nomes de variáveis."
# - Caso 3: "Reprovado: Reescrever lógica e adicionar tratamento de erros."
# - Caso Padrão (_): "Status não identificado. Consulte a Eduarda."

# Código:
codigo_status = 2

match codigo_status:
    case 1:
        print("Aprovado: Código limpo e pronto para produção.")
    case 2:
        print("Aprovado com ressalvas: Ajustar nomes de variáveis.")
    case 3:
        print("Reprovado: Reescrever lógica e adicionar tratamento de erros.")
    case _:
        print("Status não identificado. Consulte a Eduarda.")


# ==============================================================================
# ==============================================================================
# DESAFIOS OPCIONAIS (PARA ALUNOS AVANÇADOS)
# ==============================================================================
# ==============================================================================


# ==============================================================================
# DESAFIO 9 (OPCIONAL): Regra de Desconto em Checkout LMS
# ==============================================================================
# Situação: Na plataforma da JWC, um cliente ganha 20% de desconto se for ex-aluno 
# OU se utilizar um cupom válido E a compra for realizada na Black Friday.
# Enunciado: Defina 'ex_aluno' = False, 'cupom_valido' = True, 'is_black_friday' = True.
# Monte a instrução 'if/else' combinando 'or', 'and' e parênteses.
# Imprima "Desconto de 20% aplicado!" ou "Valor integral da assinatura.".

# Código:
ex_aluno = False 
cupom_valido = True
is_black_friday = True

if ex_aluno or (cupom_valido and is_black_friday):
    print("Desconto de 20% aplicado!")
else:
    print("Valor integral da assinatura.")


# ==============================================================================
# DESAFIO 10 (OPCIONAL): Liberação de Feature Flag em Produção
# ==============================================================================
# Situação: Eduarda quer ativar uma nova funcionalidade no sistema apenas para 
# usuários 'beta_tester' OU administradores, desde que a versão do sistema seja >= 2.0.
# Enunciado: Crie as variáveis 'tipo_usuario' ("beta_tester") e 'versao_sistema' (2.1).
# Escreva a condicional utilizando 'or' e 'and' para validar a regra.
# Imprima "Nova funcionalidade habilitada." ou "Funcionalidade indisponível nesta versão.".

# Código:
tipo_usuario = "beta_tester"
versao_sistema = 2.1
if (tipo_usuario == "beta_tester" or tipo_usuario == "admin") and versao_sistema >= 2.0:
    print("Nova funcionalidade habilitada.")
else:
    print("Funcionalidade indisponível nesta versão.")


# ==============================================================================
# DESAFIO 11 (OPCIONAL): Validação de Formulário Completo
# ==============================================================================
# Situação: Para evitar erros de dados nulos nas APIs da JWC, Eduarda exige que 
# os campos do formulário não estejam vazios E possuam tamanhos adequados.
# Enunciado: Crie as variáveis 'nome' ("Ana") e 'email' ("ana@jwc.com").
# Escreva um 'if' que verifique se:
# (len(nome) > 0 e len(email) > 0) AND ('@' in email).
# Imprima "Formulário validado com sucesso!" ou "Preencha todos os campos corretamente.".

# Código:
nome = "Ana"
email = "ana@jwc.com"

if (len(nome) > 0 and len(email) > 0) and ('@' in email):
    print("Formulário validado com sucesso!")
else:
    print("Preencha todos os campos corretamente.")

# ==============================================================================
# DESAFIO 12 (OPCIONAL): Filtro de Logs de Erro Críticos
# ==============================================================================
# Situação: Eduarda está analisando os arquivos de log do servidor.
# O sistema deve emitir um alerta se o nível do log for "ERROR" OU "CRITICAL", 
# E o ambiente for igual a "PROD" (produção).
# Enunciado: Crie as variáveis 'nivel_log' ("CRITICAL") e 'ambiente' ("PROD").
# Escreva a condicional e exiba no terminal: "DISPARAR ALERTA NO SLACK DA EQUIPE!" 
# ou "Log registrado sem necessidade de alerta urgente.".

# Código:
nivel_log = "CRITTICAL"
ambiente = "PROD"
if (nivel_log == "ERROR" or nivel_log == "CRITICAL") and ambiente == "PROD":
    print("DISPARAR ALERTA NO SLACK DA EQUIPE!")
else:
    print("Log registrado sem necessidade de alerta urgente.")

# ==============================================================================
# DESAFIO 13 (OPCIONAL): Validação de Inscrição em Torneio de e-Sports
# ==============================================================================
# Situação: A JWC está desenvolvendo o sistema de validação de inscritos para um torneio.
# O jogador só pode ser inscrito se tiver idade >= 16, ranking "Diamante" ou "Mestre", 
# E NÃO estiver banido.
# Enunciado: Crie 'idade' (18), 'ranking' ("Mestre"), 'banido' (False).
# Monte a expressão lógica completa e imprima "Inscrição confirmada no torneio!" 
# ou "Inscrição recusada por não atender aos requisitos.".

# Código:
idade = 18
ranking = "Mestre"
banido = False
if idade >= 16 and (ranking == "Diamante" or ranking == "Mestre") and not banido:
    print("Inscrição confirmada no torneio!")
else:
    print("Inscrição recusada por não atender aos requisitos.")

# ==============================================================================
# DESAFIO 14 (OPCIONAL): Refatoração de Código Confuso
# ==============================================================================
# Situação: Um desenvolvedor em treinamento escreveu uma condicional redundante e confusa:
# if ativo == True:
#     if admin == True:
#         print("Acesso total")
# Eduarda pediu para você refatorar (simplificar) esse código em uma única linha de 'if'.
# Enunciado: Declare 'ativo' = True e 'admin' = True.
# Reescreva a verificação em um único 'if' usando o operador 'and' de forma limpa e idiomática.

# Código:


# ==============================================================================
# DESAFIO 15 (OPCIONAL): O Desafio Supremo de Pipeline da Eduarda
# ==============================================================================
# Situação: O pipeline de entrega contínua (CI/CD) da JWC realiza o deploy automatizado 
# se: Todos os testes passaram (True) E a cobertura de código for >= 80%, E NÃO houver 
# nenhuma vulnerabilidade alta detectada.
# Enunciado: Declare as variáveis:
# 'testes_passaram' = True
# 'cobertura_codigo' = 85
# 'vulnerabilidade_alta' = False
# Escreva a estrutura 'if/else' completa utilizando 'and', '>=' e 'not'.
# Imprima "Deploy aprovado pela Eduarda! Enviando para produção..." 
# ou "Deploy bloqueado! Corrija os problemas apontados no relatório.".

# Código: