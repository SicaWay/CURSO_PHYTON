# ==============================================================================
# DESAFIOS - AULA 9: FUNÇÕES, PARÂMETROS E RETORNO
# ==============================================================================


# ==============================================================================
# 🧠 REVISÃO: FUNÇÕES E PASSAGEM DE PARÂMETROS
# ==============================================================================

# Olá, futuro(a) dev!
#
# Na Aula 8, você aprendeu que as FUNÇÕES permitem organizar e reutilizar
# partes do código de um programa.
#
# Uma função pode receber informações através de PARÂMETROS, realizar algum
# processamento e, quando necessário, devolver um resultado utilizando
# o comando RETURN.
#
# Nesta aula, continuaremos praticando esses conceitos através de novos
# cenários e desafios.
#
# Lembre-se:
#
# 1. Os PARÂMETROS recebem os valores enviados para a função.
# 2. O código dentro da função realiza o processamento.
# 3. O RETURN devolve um valor para o local onde a função foi chamada.
# 4. Uma função pode ser chamada várias vezes.
# 5. Variáveis criadas dentro de uma função possuem ESCOPO LOCAL.
# 6. Uma função também pode chamar outra função.
#
# O TESTE DE MESA será novamente muito importante!
#
# Antes de executar o código, acompanhe cuidadosamente:
#
# - Qual valor entra em cada parâmetro;
# - O que acontece dentro da função;
# - Qual valor é retornado;
# - Onde o retorno é armazenado;
# - Qual será a saída final do programa.
#
# ==============================================================================


# ==============================================================================
# 📌 EXEMPLO GUIADO
# ==============================================================================

# Observe este pequeno trecho:

# def calcular_dobro(numero):
#     resultado = numero * 2
#     return resultado
#
# valor = calcular_dobro(7)
# print("Resultado:", valor)
#
# Como fazer o teste de mesa?
#
# 1️⃣ A função 'calcular_dobro' é chamada passando o valor 7.
#
# 2️⃣ O parâmetro 'numero' recebe 7.
#
# 3️⃣ A variável 'resultado' recebe:
#
#    7 * 2 = 14
#
# 4️⃣ O comando 'return' devolve o valor 14.
#
# 5️⃣ A variável 'valor' recebe o retorno da função.
#
# 6️⃣ O print mostra:
#
# Resultado: 14
#
# Agora é sua vez!


# ==============================================================================
# DESAFIO 1: Cadastro de Produtos (Passagem de Parâmetros)
# ==============================================================================

# Situação: A JWC está desenvolvendo um sistema para organizar os produtos
# cadastrados em sua loja virtual. Para evitar a repetição de código, o
# programador decidiu criar uma função responsável por gerar uma mensagem
# com o nome e a categoria de cada produto.
#
# Enunciado: Faça o teste de mesa acompanhando os valores que entram nos
# parâmetros 'produto' e 'categoria'. Depois, escreva a mensagem que será
# exibida pelo programa.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
# Quando for testar no VS Code, selecione o código abaixo e pressione (Ctrl + /).
#
# Código:

# def cadastrar_produto(produto, categoria):
#     mensagem = f"Produto: {produto} | Categoria: {categoria}"
#     print(mensagem)
#
# nome_produto = "Teclado"
# cadastrar_produto(nome_produto, "Periféricos")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DOS PARÂMETROS:
#
# - Quando a função é chamada, o parâmetro 'produto' recebe: "__________"
#
# - O parâmetro 'categoria' recebe: "________________"
#
# - A variável interna 'mensagem' passa a valer:
#
#   "____________________________________________________________"
#
# 🖥️ SAÍDA NA TELA DO MONITOR:
#
# ________________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 2: Calculando o Total de uma Compra (Entendendo o 'return')
# ==============================================================================

# Situação: A JWC precisa automatizar o cálculo do valor total dos pedidos
# realizados pelos clientes da loja. O sistema recebe o preço de um produto
# e a quantidade comprada e utiliza uma função para realizar esse cálculo.
#
# Enunciado: Acompanhe como os valores são enviados para os parâmetros,
# observe o cálculo realizado dentro da função e descubra qual valor será
# devolvido pelo comando 'return'.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def calcular_total(preco, quantidade):
#     total = preco * quantidade
#     return total
#
# preco_produto = 80
# quantidade = 4
#
# valor_compra = calcular_total(preco_produto, quantidade)
#
# print("Valor da compra: R$", valor_compra)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DA FUNÇÃO:
#
# - Parâmetro 'preco' = ______
# - Parâmetro 'quantidade' = ______
#
# - Cálculo interno:
#
#   total = ______ * ______ = ______
#
# - O comando 'return' devolve o valor: ______
#
# 🔄 DE VOLTA AO CÓDIGO PRINCIPAL:
#
# - A variável 'valor_compra' armazena o retorno, logo vale: ______
#
# 🖥️ SAÍDA NA TELA DO MONITOR:
#
# ________________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 3: Resultado dos Alunos (Chamadas Múltiplas)
# ==============================================================================

# Situação: A JWC desenvolveu uma plataforma de cursos de programação.
# Para facilitar o acompanhamento dos alunos, o sistema precisa informar
# automaticamente a situação de cada estudante de acordo com sua nota.
#
# Enunciado: Faça o teste de mesa para cada vez que a função for invocada.
# Observe que a MESMA função será utilizada para analisar alunos diferentes.
#
# Regras:
#
# - Nota maior ou igual a 7 -> "Aprovado"
# - Nota maior ou igual a 5 -> "Recuperação"
# - Nota menor que 5 -> "Reprovado"
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def verificar_resultado(nota):
#     if nota >= 7:
#         return "Aprovado"
#     elif nota >= 5:
#         return "Recuperação"
#     else:
#         return "Reprovado"
#
# print("Lucas:", verificar_resultado(8))
# print("Julia:", verificar_resultado(6))
# print("Pedro:", verificar_resultado(4))

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 AVALIAÇÃO DAS CHAMADAS:
#
# - 1ª Chamada:
#
#   nota = 8
#   8 >= 7? (Sim/Não) ____
#   Retorna: "____________"
#
# - 2ª Chamada:
#
#   nota = 6
#   6 >= 7? (Sim/Não) ____
#   6 >= 5? (Sim/Não) ____
#   Retorna: "____________"
#
# - 3ª Chamada:
#
#   nota = 4
#   4 >= 7? (Sim/Não) ____
#   4 >= 5? (Sim/Não) ____
#   Retorna: "____________"
#
# 🖥️ SAÍDA FINAL NA TELA DO MONITOR:
#
# 1. _________________________________________________
# 2. _________________________________________________
# 3. _________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 4: A Pegadinha do Escopo (Local vs Global)
# ==============================================================================

# Situação: Um programador criou uma variável dentro de uma função para
# armazenar uma mensagem temporária. Depois que a função terminou, ele tentou
# utilizar essa mesma variável fora da função.
#
# Enunciado: Faça o teste de mesa identificando quais variáveis pertencem
# ao escopo global e quais pertencem ao escopo local da função.
#
# Observe também o que acontece quando o programa tenta acessar uma variável
# que foi criada somente dentro da função.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# mensagem = "Olá!"
#
# def criar_mensagem():
#     texto = "Bem-vindo ao sistema!"
#     print(texto)
#
# criar_mensagem()
# print(mensagem)
# print(texto)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DO ESCOPO:
#
# - Variável GLOBAL 'mensagem' inicial = "____________"
#
# - A função 'criar_mensagem()' é chamada.
#
# - Dentro da função, o parâmetro 'texto' recebe/cria:
#
#   "________________________________________"
#
# - O primeiro print, dentro da função, exibe:
#
#   __________________________________________
#
# - A função termina.
#
# - A variável 'mensagem' continua existindo porque foi criada fora da função.
#
# - A variável 'texto' foi criada dentro da função.
#
# - Quando o programa tenta executar:
#
#   print(texto)
#
#   O que acontece?
#
#   (   ) O programa imprime o texto normalmente.
#
#   (   ) O programa apresenta um erro porque 'texto' não existe
#         no escopo global.
#
# 🖥️ SAÍDA / COMPORTAMENTO DO PROGRAMA:
#
# ________________________________________________________________
# ________________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 5: Funções que Chamam Funções (Modularização)
# ==============================================================================

# Situação: A JWC precisa criar um sistema de vendas capaz de calcular o
# preço final de um produto depois da aplicação de um desconto.
#
# Para deixar o programa organizado, o desenvolvedor decidiu separar o
# problema em duas funções:
#
# - Uma função será responsável por calcular o desconto.
# - Outra função utilizará esse resultado para descobrir o preço final.
#
# Enunciado: Acompanhe o fluxo de execução passando de uma função para outra.
# Observe atentamente o momento em que cada função recebe seus parâmetros e
# devolve seu resultado.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def calcular_desconto(preco):
#     desconto = preco * 0.10
#     return desconto
#
# def calcular_preco_final(preco):
#     desconto = calcular_desconto(preco)
#     return preco - desconto
#
# preco_final = calcular_preco_final(200)
#
# print("Preço final: R$", preco_final)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 PASSO A PASSO DO FLUXO DE EXECUÇÃO:
#
# - 1. O código chama 'calcular_preco_final' passando:
#
#   preco = ______
#
# - 2. Dentro de 'calcular_preco_final', a função
#   'calcular_desconto(preco)' é chamada.
#
# - 3. A função 'calcular_desconto' recebe:
#
#   preco = ______
#
# - 4. O cálculo interno é:
#
#   desconto = ______ * 0.10 = ______
#
# - 5. A função 'calcular_desconto' devolve:
#
#   ______
#
# - 6. A variável 'desconto', dentro de 'calcular_preco_final',
#   recebe o valor: ______
#
# - 7. A função calcula:
#
#   ______ - ______ = ______
#
# - 8. O comando 'return' de 'calcular_preco_final' devolve:
#
#   ______
#
# - 9. A variável 'preco_final' recebe:
#
#   ______
#
# 🖥️ SAÍDA EXATA NA TELA DO MONITOR:
#
# ________________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 6: Parâmetros Opcionais (Default)
# ==============================================================================

# Situação: O sistema de suporte técnico da JWC precisa registrar chamados
# feitos pelos usuários. Cada chamado possui um nome de usuário e uma
# prioridade.
#
# Para facilitar o cadastro, o programador definiu que a prioridade será
# automaticamente "Normal" quando o usuário não informar outra prioridade.
#
# Enunciado: Avalie as duas chamadas da mesma função abaixo e descubra o
# comportamento do parâmetro opcional.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def abrir_chamado(usuario, prioridade="Normal"):
#     print(f"Usuário: {usuario} | Prioridade: {prioridade}")
#
# abrir_chamado("Rafael", "Alta")
# abrir_chamado("Camila")

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 AVALIAÇÃO DAS CHAMADAS:
#
# - Chamada 1:
#
#   usuario = "Rafael"
#   prioridade enviada = "Alta"
#
#   Imprime:
#
#   ______________________________________________________________
#
# - Chamada 2:
#
#   usuario = "Camila"
#   prioridade enviada = Nenhuma.
#
#   Como nenhum valor foi enviado para 'prioridade', a função utiliza
#   o valor padrão:
#
#   "____________"
#
#   Imprime:
#
#   ______________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 7: Calculando a Média (Mais de um Parâmetro)
# ==============================================================================

# Situação: Uma escola utiliza um sistema para calcular automaticamente a
# média dos alunos. Para isso, uma função recebe três notas e realiza o
# cálculo da média aritmética.
#
# Enunciado: Faça o teste de mesa acompanhando os três parâmetros, o cálculo
# da soma, o cálculo da média e o valor devolvido pelo 'return'.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def calcular_media(nota1, nota2, nota3):
#     soma = nota1 + nota2 + nota3
#     media = soma / 3
#     return media
#
# resultado = calcular_media(7, 8, 10)
#
# print("Média:", resultado)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DOS PARÂMETROS:
#
# - nota1 = ______
# - nota2 = ______
# - nota3 = ______
#
# 🔄 CÁLCULO INTERNO:
#
# - soma = ______ + ______ + ______ = ______
#
# - media = ______ / 3 = ______
#
# - O comando 'return' devolve: ______
#
# 🔄 DE VOLTA AO PROGRAMA PRINCIPAL:
#
# - A variável 'resultado' recebe: ______
#
# 🖥️ SAÍDA NA TELA DO MONITOR:
#
# ________________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 8: Frete Grátis (Condição + Função + Return)
# ==============================================================================

# Situação: A loja virtual da JWC oferece frete grátis para compras com
# valor maior ou igual a R$ 150,00.
#
# O programador criou uma função para verificar automaticamente se cada
# cliente terá direito ao benefício.
#
# Enunciado: Faça o teste de mesa para cada chamada da função e identifique
# qual valor será retornado em cada situação.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def verificar_frete(valor):
#     if valor >= 150:
#         return "Frete grátis"
#     else:
#         return "Frete pago"
#
# print("Compra 1:", verificar_frete(200))
# print("Compra 2:", verificar_frete(100))
# print("Compra 3:", verificar_frete(150))

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 AVALIAÇÃO DAS CHAMADAS:
#
# - 1ª Chamada:
#
#   valor = 200
#   200 >= 150? (Sim/Não) ______
#   Retorna: "________________"
#
# - 2ª Chamada:
#
#   valor = 100
#   100 >= 150? (Sim/Não) ______
#   Retorna: "________________"
#
# - 3ª Chamada:
#
#   valor = 150
#   150 >= 150? (Sim/Não) ______
#   Retorna: "________________"
#
# 🖥️ SAÍDA FINAL NA TELA DO MONITOR:
#
# 1. __________________________________________________________
# 2. __________________________________________________________
# 3. __________________________________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 9: Função + Return + Outra Função
# ==============================================================================

# Situação: Uma plataforma de cursos precisa calcular a situação final de
# seus alunos.
#
# Primeiro, o sistema precisa calcular a média de duas notas.
# Depois, uma segunda função deverá analisar essa média e informar se o
# aluno foi aprovado ou reprovado.
#
# Enunciado: Acompanhe o fluxo completo do programa, desde o envio das notas
# para a primeira função até o resultado final produzido pela segunda função.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def calcular_media(nota1, nota2):
#     return (nota1 + nota2) / 2
#
# def verificar_situacao(media):
#     if media >= 7:
#         return "Aprovado"
#     else:
#         return "Reprovado"
#
# media_final = calcular_media(8, 6)
# situacao = verificar_situacao(media_final)
#
# print("Média final:", media_final)
# print("Situação:", situacao)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 PRIMEIRA FUNÇÃO - calcular_media():
#
# - nota1 = ______
# - nota2 = ______
#
# - Cálculo:
#
#   (______ + ______) / 2 = ______
#
# - O return devolve: ______
#
# 🔄 DE VOLTA AO PROGRAMA PRINCIPAL:
#
# - A variável 'media_final' recebe: ______
#
# 🔄 SEGUNDA FUNÇÃO - verificar_situacao():
#
# - O parâmetro 'media' recebe: ______
#
# - ______ >= 7? (Sim/Não) ______
#
# - O return devolve:
#
#   "________________"
#
# 🔄 DE VOLTA AO PROGRAMA PRINCIPAL:
#
# - A variável 'situacao' recebe:
#
#   "________________"
#
# 🖥️ SAÍDA FINAL NA TELA DO MONITOR:
#
# Média final: __________________________________
# Situação: _____________________________________
# ==============================================================================


# ==============================================================================
# DESAFIO 10: O Desafio do Salário (Função + Parâmetros + Return)
# ==============================================================================

# Situação: O setor financeiro da JWC precisa calcular o salário final de
# seus colaboradores depois de aplicar um bônus.
#
# O sistema recebe o salário e o percentual de bônus através de parâmetros.
# A função calcula o valor do bônus e devolve o resultado.
#
# Enunciado: Faça o teste de mesa acompanhando os valores que entram na
# função, o cálculo realizado e o valor que retorna para o programa principal.
#
# ⚠️ ATENÇÃO: Faça o teste de mesa no papel/tabela PRIMEIRO.
#
# Código:

# def calcular_bonus(salario, percentual):
#     bonus = salario * (percentual / 100)
#     return bonus
#
# salario = 3500
# bonus_recebido = calcular_bonus(salario, 8)
# salario_final = salario + bonus_recebido
#
# print("Bônus: R$", bonus_recebido)
# print("Salário final: R$", salario_final)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 RASTREAMENTO DA FUNÇÃO:
#
# - Parâmetro 'salario' = ______
# - Parâmetro 'percentual' = ______
#
# - Cálculo:
#
#   bonus = ______ * (______ / 100)
#
#   bonus = ______
#
# - O comando 'return' devolve: ______
#
# 🔄 DE VOLTA AO PROGRAMA PRINCIPAL:
#
# - 'bonus_recebido' recebe: ______
#
# - 'salario_final' será:
#
#   ______ + ______ = ______
#
# 🖥️ SAÍDA FINAL NA TELA DO MONITOR:
#
# Bônus: R$ ___________________________________
# Salário final: R$ ____________________________
# ==============================================================================


# ==============================================================================
# 🎯 DESAFIO FINAL: MONTE O FLUXO COMPLETO
# ==============================================================================

# Situação: A JWC está criando um pequeno sistema para calcular o valor final
# de uma compra.
#
# O sistema deverá:
#
# 1. Calcular o subtotal da compra;
# 2. Calcular um desconto;
# 3. Calcular o valor final;
# 4. Exibir o resultado.
#
# Para deixar o programa organizado, cada tarefa foi separada em uma função.
#
# Enunciado: Faça um teste de mesa completo acompanhando o fluxo de execução.
# Observe atentamente quando uma função chama outra função e onde cada
# resultado é armazenado.
#
# ⚠️ ATENÇÃO: Não execute o código antes de terminar o teste de mesa!
#
# Código:

# def calcular_subtotal(preco, quantidade):
#     return preco * quantidade
#
# def calcular_desconto(valor):
#     return valor * 0.10
#
# def calcular_final(subtotal):
#     desconto = calcular_desconto(subtotal)
#     return subtotal - desconto
#
# subtotal = calcular_subtotal(50, 4)
# valor_final = calcular_final(subtotal)
#
# print("Subtotal: R$", subtotal)
# print("Valor final: R$", valor_final)

# ------------------------------------------------------------------------------
# ✍️ SEU TESTE DE MESA:
#
# 🔄 1ª FUNÇÃO - calcular_subtotal():
#
# - preco = ______
# - quantidade = ______
# - Cálculo: ______ * ______ = ______
# - return devolve: ______
#
# 🔄 PROGRAMA PRINCIPAL:
#
# - 'subtotal' recebe: ______
#
# 🔄 2ª FUNÇÃO - calcular_final():
#
# - 'subtotal' recebe: ______
#
# - Dentro dela, 'calcular_desconto()' é chamada.
#
# - A função 'calcular_desconto()' recebe: ______
#
# - Cálculo do desconto:
#
#   ______ * 0.10 = ______
#
# - O desconto calculado é: ______
#
# - Agora 'calcular_final()' realiza:
#
#   ______ - ______ = ______
#
# - O return devolve: ______
#
# 🔄 PROGRAMA PRINCIPAL:
#
# - 'valor_final' recebe: ______
#
# 🖥️ SAÍDA FINAL:
#
# Subtotal: R$ _________________________________
# Valor final: R$ ______________________________
# ==============================================================================


# ==============================================================================
# ⭐ DESAFIO OPCIONAL: CRIE SUA PRÓPRIA FUNÇÃO
# ==============================================================================

# Lembrete Didático:
# Agora você deverá criar uma função sozinho(a), utilizando tudo o que
# aprendeu nesta aula.
#
# Enunciado:
# Crie uma função chamada 'calcular_triplo' que receba um número através
# de um parâmetro chamado 'numero'.
#
# A função deverá:
#
# 1. Receber o número;
# 2. Multiplicar o número por 3;
# 3. Retornar o resultado.
#
# Depois, crie uma variável chamada 'resultado' para armazenar o retorno
# da função e mostre esse resultado na tela.
#
# ⚠️ Tente resolver sozinho antes de olhar qualquer exemplo!

# ------------------------------------------------------------------------------
# ✍️ ESCREVA SEU CÓDIGO:
#
# def ______________________________________________
#     ______________________________________________
#     ______________________________________________
#
# resultado = ______________________________________
#
# print(____________________________________________)
#
# ------------------------------------------------------------------------------
# 🔄 SEU TESTE DE MESA:
#
# - O parâmetro 'numero' recebe: ______
#
# - Cálculo realizado:
#
#   ______ * 3 = ______
#
# - O return devolve: ______
#
# - A variável 'resultado' recebe: ______
#
# 🖥️ SAÍDA:
#
# ________________________________________________________________
# ==============================================================================


# ==============================================================================
# 🎯 OBJETIVOS DA AULA 9
# ==============================================================================

# Ao terminar estes desafios, você deverá conseguir:
#
# [ ] Identificar os parâmetros de uma função;
#
# [ ] Acompanhar os valores enviados para uma função;
#
# [ ] Entender o funcionamento do return;
#
# [ ] Identificar onde o retorno é armazenado;
#
# [ ] Acompanhar chamadas múltiplas de uma função;
#
# [ ] Diferenciar variáveis locais e globais;
#
# [ ] Entender o escopo de uma função;
#
# [ ] Acompanhar uma função chamando outra função;
#
# [ ] Utilizar parâmetros com valores padrão;
#
# [ ] Fazer teste de mesa envolvendo várias funções;
#
# [ ] Criar uma função simples utilizando parâmetros e return.
#
# 🚀 Continue praticando!
#
# O objetivo não é apenas descobrir a resposta, mas conseguir explicar
# PASSO A PASSO o caminho que cada valor percorreu dentro do programa.
#
# Quanto melhor você dominar o teste de mesa, mais facilidade terá para
# entender programas maiores e encontrar erros no seu próprio código.
# ==============================================================================