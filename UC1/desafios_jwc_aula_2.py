# ==============================================================================
# CADERNO DE DESAFIOS - AULA 2: O PRIMEIRO DIA NA JWC
# ==============================================================================

# ==============================================================================
# DESAFIO 1: A Chegada ao Centro
# ==============================================================================
# Situação: Você finalmente chegou à sede da JWC, localizada no movimentado 
# centro do Rio de Janeiro. A Líder Técnica, Patrícia, 
# te recebe na porta com um sorriso e pede para você testar o terminal do saguão.
# Missão: Use a função print() para exibir a mensagem: "Cheguei na JWC!"

#Código :

print("Cheguei na JWC!")

# ==============================================================================
# DESAFIO 2: O Crachá de Visitante
# ==============================================================================
# Situação: A recepcionista precisa gerar o seu crachá temporário para o 
# processo seletivo da vaga de Programador Full Stack.
# Missão: Crie uma variável descritiva 'nome_candidato' e guarde o seu nome nela. 
# Depois, crie uma variável 'idade_candidato'. Imprima as duas variáveis na tela.

# Código:

nome_candidato = "Jéssica Chaves"
idade_candidato = 33

print(nome_candidato)
print(idade_candidato)

# ==============================================================================
# DESAFIO 3: Conhecendo a Estrutura
# ==============================================================================
# Situação: No elevador, Patrícia te conta que a empresa tem 30 colaboradores na 
# área administrativa e 20 na equipe de desenvolvimento. 
# Missão: Crie a variável 'total_colaboradores_administrativos' valendo 30 e a 
# variável 'total_colaboradores_desenvolvimento' valendo 20. Crie uma terceira 
# variável chamada 'total_geral_funcionarios' que some as duas e imprima o resultado!

# Código:

total_colaboradores_administrativos = 30
total_colaboradores_desenvolvimento = 20

total_geral_funcionarios = total_colaboradores_administrativos + total_colaboradores_desenvolvimento
print(total_geral_funcionarios)

# ==============================================================================
# DESAFIO 4: O Boom da Educação
# ==============================================================================
# Situação: Durante a pandemia, a JWC cresceu muito atendendo um setor específico: 
# o da educação. 
# Missão: Crie uma constante (tudo em maiúsculo) chamada 'SETOR_MERCADO_PRINCIPAL' 
# e guarde nela a palavra "Educação". Imprima uma frase usando essa constante.

# Código:
SETOR_MERCADO_PRINCIPAL = "Educação"
print ("É um objetivo primordial na nossa empresa: o desenvolvimento da", SETOR_MERCADO_PRINCIPAL)


# ==============================================================================
# DESAFIO 5: O Armário do RH
# ==============================================================================
# Situação: O pessoal do RH te explica que eles organizam os dados dos candidatos 
# como se fosse a "arrumação de um armário". As gavetas com cadeado são 
# as Constantes, e as caixas abertas são as Variáveis.
# Missão: Crie uma constante 'NOME_EMPRESA' valendo "JWC". Crie uma variável 
# 'status_atual_candidato' valendo "Em teste". Imprima ambas.

# Código:
NOME_EMPRESA = "JWC"
status_atual_candidato = "Em teste"
print ("Prezado candidato, agradecemos o seu interesse em desenvolver conosco, na", NOME_EMPRESA)
print ("O status dos seu processo seletivo é:" , status_atual_candidato)


# ==============================================================================
# DESAFIO 6: Conversa no Cafezinho
# ==============================================================================
# Situação: Na copa da empresa, um desenvolvedor sênior quer puxar assunto com você.
# Missão: Use a função input() para perguntar: "Qual é a sua linguagem de 
# programação favorita?". Guarde a resposta numa variável chamada 'linguagem_favorita' 
# e depois imprima essa resposta.

# Código:
linguagem_favortia = input("Qual é a sua linguagem de programação favorita? ")
print (f"A sua linguagem favorita é {linguagem_favortia}, a minha também!")


# ==============================================================================
# DESAFIO 7: O Formulário de Transporte
# ==============================================================================
# Situação: O RH precisa saber como você vai se deslocar até o centro do Rio de Janeiro 
# todos os dias, caso seja contratado.
# Missão: Use o input() para perguntar qual meio de transporte você utiliza. 
# Salve na variável 'meio_transporte_utilizado' e exiba na tela formatado.

# Código:
meio_transporte_utilizado = input ("Qual meio de transporte você utiliza para chegar ao Centro do Rio de Janeiro? ")
print (f"A utilização de {meio_transporte_utilizado} para o deslocamento até o Centro é eficaz!")

# ==============================================================================
# DESAFIO 8: Mudança de Planos
# ==============================================================================
# Situação: Você estava concorrendo para uma posição inicial, mas o diretor viu seu 
# potencial e te alocou para a vaga de "Programador Full Stack"!
# Missão: Crie a variável 'cargo_pretendido_candidato' valendo "Estágio". Imprima. 
# Na linha de baixo, atualize o valor da MESMA variável para "Full Stack" e imprima novamente.

# Código:
cargo_pretendido_candidato = "Estágio"
print (f"Você estava participado do processo seletivo para a vaga de {cargo_pretendido_candidato}.")
cargo_pretendido_candidato = "Full Stack"
print (f"De acordo com o seu potencial, atualizamos seu processo seletivo para a vaga de {cargo_pretendido_candidato}.") 

# ==============================================================================
# DESAFIO 9: Avaliação de Perfil
# ==============================================================================
# Situação: A JWC busca pessoas "curiosas, ágeis e inovadoras". 
# Missão: Crie três variáveis descritivas do tipo booleano (True ou False): 
# 'possui_perfil_curioso', 'possui_perfil_agil' e 'possui_perfil_inovador'. 
# Atribua True para todas e imprima-as.

# Código:
possui_perfil_curioso = True
possui_perfil_agil = True
possui_perfil_inovador = True
print (f"É curioso? = {possui_perfil_curioso}. É ágil? = {possui_perfil_agil}. É inovador? = {possui_perfil_inovador}.")



# ==============================================================================
# DESAFIO 10: O Grito do Diretor
# ==============================================================================
# Situação: O diretor da JWC adora avisos em letras MAIÚSCULAS no mural da empresa.
# Missão: Crie uma variável 'mensagem_aviso_mural' com o texto "bem-vindos novos talentos". 
# Use o método .upper() no print para exibir a frase toda em letras maiúsculas.

# Código:
mensagem_aviso_mural = "bem-vindos novos talentos"
print(mensagem_aviso_mural.upper())

# ==============================================================================
# DESAFIO 11: A Senha de Acesso
# ==============================================================================
# Situação: Você pediu a senha temporária de rede, mas a equipe de segurança 
# informou que senhas seguras precisam ser medidas em tamanho.
# Missão: Crie a variável 'senha_temporaria_rede' com um valor de texto. Use a 
# função len() dentro do print para contar e exibir quantos caracteres essa senha possui.

# Código:
senha_temporaria_rede = "JWC7053#Segura"
print(f"A senha possui {len(senha_temporaria_rede)} caracteres.")

# ==============================================================================
# DESAFIO 12: Juntando os Pedaços
# ==============================================================================
# Situação: O banco de dados da empresa separa o primeiro nome do sobrenome.
# Missão: Crie a variável 'primeiro_nome' e a variável 'sobrenome_candidato'. 
# Depois, crie uma terceira variável chamada 'nome_completo_formatado' que junte 
# as duas com um espaço no meio. Imprima o resultado.

# Código:
primeiro_nome = "Jéssica"
sobrenome_candidato = "Chaves"
nome_completo_formatado = primeiro_nome + " " + sobrenome_candidato
print(nome_completo_formatado)

# ==============================================================================
# DESAFIO 13: Cálculo do Benefício
# ==============================================================================
# Situação: Todo novo funcionário ganha um auxílio inicial para ferramentas de estudo.
# Missão: Crie uma variável 'valor_salario_base' valendo 2000 e uma variável 
# 'valor_auxilio_ferramentas' valendo 150. Imprima a soma das duas variáveis usando 
# uma variável de resultado chamada 'total_remuneracao_inicial'.

# Código:
valor_salario_base = 2000
valor_auxilio_ferramentas = 150
total_remuneracao_inicial = valor_salario_base + valor_auxilio_ferramentas
print(f"Total da remuneração inicial: R$ {total_remuneracao_inicial}")

# ==============================================================================
# DESAFIO 14: O Bug do Código
# ==============================================================================
# Situação: Um colega da equipe de desenvolvimento tentou criar uma mensagem, mas 
# esqueceu de estruturar o texto corretamente e o código quebrou!
# Missão: Conserte o código abaixo para que ele funcione sem erros de sintaxe.
# texto_informativo = Alerta do sistema interno da JWC
# print(texto_informativo)

# Código (escreva a versão corrigida aqui):
texto_informativo = "Alerta do sistema interno da JWC"
print(texto_informativo)

# ==============================================================================
# DESAFIO 15: O Relatório de Fim de Dia (Projeto Final da Aula)
# ==============================================================================
# Situação: O seu primeiro dia de testes práticos na JWC chegou ao fim! Para registrar 
# seu progresso, você precisa gerar um relatório automatizado.
# Missão: Use 'inputs' para coletar: 'nome_colaborador_input', 'idade_colaborador_input' 
# e 'pontuacao_teste_pratico'. Depois, exiba um print formatado (f-string) unindo 
# todas essas informações em uma frase clara para o recrutador.

# Código:
nome_colaborador_input = input("Digite o nome do colaborador: ")
idade_colaborador_input = input("Digite a idade do colaborador: ")
pontuacao_teste_pratico = input("Digite a pontuação obtida no teste: ")

print(f"Relatório Final: O colaborador {nome_colaborador_input}, de {idade_colaborador_input} anos, concluiu o teste prático na JWC com a pontuação {pontuacao_teste_pratico}.")

