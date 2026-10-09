# # ===============================================================================
# # EMPRESA JWC TECNOLOGIA - PROCESSO SELETIVO: PROGRAMAÇÃO ORIENTADA A OBJETO (AULA 11)[cite: 14]
# # ===============================================================================
# # CENÁRIO:
# # A empresa de Tecnologia JWC abriu vagas para Programador Full Stack e o RH 
# # estruturou o processo seletivo em etapas com diversos desafios[cite: 3, 4]. 
# # Nesta etapa, o recrutador entregou uma atividade para avaliar os seus conhecimentos 
# # em programação Orientada a Objeto (OO)[cite: 14]. 
# #
# # O desafio baseia-se na seguinte reflexão de escalabilidade proposta pelo recrutador: 
# # como desenvolver um sistema de conta bancária para gerir as informações de apenas 
# # dois clientes iniciais e, usando o mesmo código, ter a capacidade de escalar o 
# # sistema para dez, mil ou mais clientes de forma organizada?[cite: 14]
# #
# # REQUISITOS DO DESAFIO:
# # 1. Aplicar os conceitos de programação Orientada a Objeto (OO) para estruturar a solução[cite: 14].
# # 2. Criar uma classe que represente os clientes, contendo obrigatoriamente os seguintes atributos[cite: 14]:
# #    - Titular[cite: 14]
# #    - Saldo[cite: 14]
# #    - Conta[cite: 14]
# # 3. O sistema bancário deve conter a implementação lógica das seguintes operações[cite: 14]:
# #    - Depósito: Método para adicionar um valor financeiro ao saldo[cite: 14].
# #    - Saque: Método para retirar um valor do saldo[cite: 14].
# #    - Transferência: Método para movimentar um valor da conta atual para uma conta destino[cite: 14].
# #    - Extrato: Método para exibir os dados e o saldo atual do cliente[cite: 14].
# # ===============================================================================

# class ContaBancaria:
#     def __init__(self, titular, conta, saldo_inicial=0.0):
#         """
#         Método construtor da classe.
        # TODO: Inicializar os atributos 'Titular', 'Conta' e 'Saldo' baseando-se nos parâmetros recebidos[cite: 14].
#         """
#         pass

#     def depositar(self, valor):
#         """
#         TODO: Implementar a lógica da operação de depósito[cite: 14].
#         - Adicione o 'valor' ao saldo atual da conta.
#         - Opcional: exiba uma mensagem confirmando o depósito.
#         """
#         pass

#     def sacar(self, valor):
#         """
#         TODO: Implementar a lógica da operação de saque[cite: 14].
#         - Verifique se o 'valor' desejado é menor ou igual ao saldo atual (para evitar saldo negativo).
#         - Deduzir o valor do saldo se for válido.
#         """
#         pass

#     def extrato(self):
#         """
#         TODO: Implementar a exibição do extrato bancário[cite: 14].
#         - Utilize comandos de impressão (print) para mostrar o Titular, o número da Conta e o Saldo.
#         """
#         pass

#     def transferir(self, valor, conta_destino):
#         """
#         TODO: Implementar a lógica da operação de transferência entre contas[cite: 14].
#         - Verifique se a conta de origem (self) tem saldo suficiente.
#         - Se sim, deduza o 'valor' do saldo atual e adicione esse mesmo 'valor' ao saldo da 'conta_destino'.
#         """
#         pass


# # ===============================================================================
# # ÁREA DE TESTES E VALIDAÇÃO DA ESCALABILIDADE
# # ===============================================================================
# print("=== DESAFIO AULA 11: Sistema Bancário (OO) ===")

# # 1. Instancie os objetos criando apenas dois clientes iniciais com números de conta e saldos diferentes[cite: 14].
# # cliente1 = ContaBancaria(...)
# # cliente2 = ContaBancaria(...)

# # 2. Teste a operação de depósito adicionando fundos a um dos clientes[cite: 14].
# # Ex: cliente1.depositar(200.0)

# # 3. Teste a operação de saque em um dos clientes[cite: 14].

# # 4. Teste a operação de transferência, enviando um valor do cliente 1 para o cliente 2[cite: 14].

# # 5. Chame a operação de extrato para ambos os clientes e valide se as operações atualizaram os saldos corretamente[cite: 14].

# ===============================================================================
# EMPRESA JWC TECNOLOGIA - PROCESSO SELETIVO: PROGRAMAÇÃO ORIENTADA A OBJETO (AULA 11)
# ===============================================================================

class ContaBancaria:
    def __init__(self, titular, conta, saldo_inicial=0.0):
        """
        Método construtor da classe.
        Inicializa os atributos 'titular', 'conta' e 'saldo'.
        """
        self.titular = titular
        self.conta = conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """
        Adiciona o valor fornecido ao saldo da conta.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta de {self.titular}.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        """
        Realiza o saque caso o saldo seja suficiente.
        """
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso por {self.titular}.")
        else:
            print(f"Saque recusado para {self.titular}: Saldo insuficiente (R$ {self.saldo:.2f}).")

    def extrato(self):
        """
        Exibe as informações atuais da conta bancária.
        """
        print("\n--- EXTRATO BANCÁRIO ---")
        print(f"Titular: {self.titular}")
        print(f"Conta:   {self.conta}")
        print(f"Saldo:   R$ {self.saldo:.2f}")
        print("------------------------")

    def transferir(self, valor, conta_destino):
        """
        Transfere um valor desta conta para a conta_destino.
        """
        if valor <= 0:
            print("Valor de transferência inválido.")
        elif valor <= self.saldo:
            self.saldo -= valor  # Deduz da conta de origem
            conta_destino.saldo += valor  # Adiciona na conta de destino
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso de {self.titular} para {conta_destino.titular}.")
        else:
            print(f"Transferência recusada para {self.titular}: Saldo insuficiente (R$ {self.saldo:.2f}).")


# ===============================================================================
# ÁREA DE TESTES E VALIDAÇÃO DA ESCALABILIDADE
# ===============================================================================
if __name__ == "__main__":
    print("=== DESAFIO AULA 11: Sistema Bancário (OO) ===")

    # 1. Instanciação dos clientes
    cliente1 = ContaBancaria(titular="Carlos Silva", conta="1001-X", saldo_inicial=500.0)
    cliente2 = ContaBancaria(titular="Ana Souza", conta="2002-Y", saldo_inicial=200.0)

    # Exibe os extratos iniciais
    cliente1.extrato()
    cliente2.extrato()

    print("\n--- EXECUTANDO OPERAÇÕES ---")

    # 2. Teste de Depósito
    cliente1.depositar(200.0)

    # 3. Teste de Saque
    cliente2.sacar(50.0)

    # 4. Teste de Transferência
    cliente1.transferir(150.0, cliente2)

    # 5. Exibição dos Extratos Finais
    cliente1.extrato()
    cliente2.extrato()