# Menu para interação com o usuário
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[n] Cadastrar Conta Bancária
[q] Sair

=> """

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas_bancarias = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Informe o nome completo: ")
    cpf = input("Informe o CPF (somente números): ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    usuario = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para cadastrar uma nova conta bancária
def cadastrar_conta():
    cpf_usuario = input("Informe o CPF do usuário: ")
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["cpf"] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        numero_conta = len(contas_bancarias) + 1
        conta = {"numero_conta": numero_conta, "cpf_usuario": cpf_usuario, "saldo": 0}
        contas_bancarias.append(conta)
        print(f"Conta bancária {numero_conta} cadastrada com sucesso!")
    else:
        print("Usuário não encontrado. Certifique-se de que o CPF está correto.")

# Função para depósito
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para saque
def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para exibir o extrato
def exibir_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Loop principal do programa
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "c":
        cadastrar_usuario()

    elif opcao == "n":
        cadastrar_conta()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
