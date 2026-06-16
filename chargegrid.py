# GoodWe Challenge - Sprint 2

carregadores = [
    {
        "nome": "FIAP Paulista",
        "id": "FIAP001",
        "localizacao": "Av. Paulista",
        "potencia": 22,
        "status": "Disponível",
        "conector": "Tipo 2"
    }
]

recargas = []

tarifa_normal = 0.70
tarifa_pico = 1.50


def pausar():
    print()
    input("Pressione ENTER para continuar...")


def cadastrar_carregador():
    print()
    print("==============================")
    print("CADASTRO DO CARREGADOR")
    print("==============================")

    novo_id = input("ID do carregador: ")

    for c in carregadores:
        if c["id"] == novo_id:
            print()
            print("ID já cadastrado!")
            pausar()
            return

    carregador = {
        "nome": input("Nome do carregador: "),
        "id": novo_id,
        "localizacao": input("Localização: "),
        "potencia": float(input("Potência máxima (kW): ").replace(",", ".")),
        "status": "Disponível",
        "conector": input("Tipo de conector: ")
    }

    carregadores.append(carregador)

    print()
    print("Carregador cadastrado com sucesso!")
    pausar()


def listar_carregadores():
    if len(carregadores) == 0:
        print()
        print("Nenhum carregador cadastrado!")
        return False

    print()
    print("==============================")
    print("CARREGADORES CADASTRADOS")
    print("==============================")

    for i, c in enumerate(carregadores, start=1):
        print()
        print(f"[{i}] {c['nome']}")
        print(f"ID: {c['id']}")
        print(f"Localização: {c['localizacao']}")
        print(f"Potência: {c['potencia']} kW")
        print(f"Conector: {c['conector']}")
        print(f"Status: {c['status']}")

    return True


def editar_carregador():
    if len(carregadores) == 0:
        print()
        print("Nenhum carregador cadastrado!")
        pausar()
        return

    print()
    id_busca = input("Digite o ID do carregador: ")

    for c in carregadores:

        if c["id"] == id_busca:

            nome = input(f"Nome [{c['nome']}]: ")
            if nome:
                c["nome"] = nome

            local = input(f"Localização [{c['localizacao']}]: ")
            if local:
                c["localizacao"] = local

            potencia = input(f"Potência [{c['potencia']}]: ")
            if potencia:
                c["potencia"] = float(potencia.replace(",", "."))

            conector = input(f"Conector [{c['conector']}]: ")
            if conector:
                c["conector"] = conector

            print()
            print("Carregador atualizado com sucesso!")
            pausar()
            return

    print()
    print("ID não encontrado!")
    pausar()


def cadastrar_tarifas():
    global tarifa_normal, tarifa_pico

    print()
    print("==============================")
    print("CADASTRO DE TARIFAS")
    print("==============================")

    tarifa_normal = float(
        input("Tarifa normal (R$/kWh): ").replace(",", "."))

    tarifa_pico = float(
        input("Tarifa de pico (R$/kWh): ").replace(",", "."))

    print()
    print("Tarifas cadastradas com sucesso!")
    pausar()


def visualizar_tarifas():
    print()
    print("==============================")
    print("TARIFAS")
    print("==============================")

    print(f"Tarifa Normal: R$ {tarifa_normal:.2f}/kWh")
    print(f"Tarifa de Pico: R$ {tarifa_pico:.2f}/kWh")

    pausar()


def iniciar_recarga():

    if len(carregadores) == 0:
        print()
        print("Cadastre um carregador primeiro!")
        pausar()
        return

    if tarifa_normal == 0 or tarifa_pico == 0:
        print()
        print("Cadastre as tarifas primeiro!")
        pausar()
        return

    listar_carregadores()

    try:

        print()
        escolha = int(input("Escolha o carregador: ")) - 1

        if escolha < 0 or escolha >= len(carregadores):
            print()
            print("Opção inválida!")
            pausar()
            return

        carregador = carregadores[escolha]

        carregador["status"] = "Ocupado"

        capacidade_bateria = float(
            input("Capacidade da bateria do veículo (kWh): ").replace(",", "."))

        bateria_atual = float(
            input("Bateria atual (%): ").replace(",", "."))

        bateria_desejada = float(
            input("Bateria desejada (%): ").replace(",", "."))

        if bateria_desejada <= bateria_atual:
            print()
            print("Valor inválido!")
            carregador["status"] = "Disponível"
            pausar()
            return

        print()
        print("1 - Horário Normal")
        print("2 - Horário de Pico")

        periodo = input("Escolha: ")

        if periodo == "1":
            tarifa = tarifa_normal
            nome_periodo = "Normal"
            potencia_utilizada = carregador["potencia"]

        elif periodo == "2":
            tarifa = tarifa_pico
            nome_periodo = "Pico"
            potencia_utilizada = carregador["potencia"] * 0.5

        else:
            print()
            print("Opção inválida!")
            carregador["status"] = "Disponível"
            pausar()
            return

        energia = (
            (bateria_desejada - bateria_atual) / 100) * capacidade_bateria

        tempo_horas = energia / potencia_utilizada

        horas = int(tempo_horas)
        minutos = int((tempo_horas - horas) * 60)

        custo = energia * tarifa

        recargas.append({
            "carregador": carregador["nome"],
            "energia": energia,
            "tempo": f"{horas}h {minutos}min",
            "custo": custo
        })

        print()
        print("==============================")
        print("RESUMO DA RECARGA")
        print("==============================")

        print(f"Carregador: {carregador['nome']}")
        print(f"Período: {nome_periodo}")
        print(f"Bateria Inicial: {bateria_atual:.0f}%")
        print(f"Bateria Final: {bateria_desejada:.0f}%")
        print(f"Capacidade da Bateria: {capacidade_bateria:.2f} kWh")
        print(f"Energia Consumida: {energia:.2f} kWh")
        print(f"Tempo Estimado: {horas}h {minutos}min")
        print(f"Custo: R$ {custo:.2f}")
        print("Status da Recarga: Concluída")

        if periodo == "2":
            print()
            print("IA ChargeGrid:")
            print("Potência reduzida em 50%")
            print("para evitar sobrecarga da rede.")

        carregador["status"] = "Disponível"

        pausar()

    except ValueError:
        print()
        print("Entrada inválida!")
        pausar()


def historico_recargas():

    print()
    print("==============================")
    print("HISTÓRICO DE RECARGAS")
    print("==============================")

    if len(recargas) == 0:
        print("Nenhuma recarga registrada.")
    else:
        for i, r in enumerate(recargas, start=1):
            print()
            print(f"Recarga {i}")
            print(f"Carregador: {r['carregador']}")
            print(f"Energia: {r['energia']:.2f} kWh")
            print(f"Tempo: {r['tempo']}")
            print(f"Custo: R$ {r['custo']:.2f}")

    pausar()


while True:

    print()
    print("==============================")
    print("CHARGEGRID INTELLIGENCE")
    print("==============================")

    print("1 - Iniciar Recarga")
    print("2 - Informações do Carregador")
    print("3 - Histórico de Recargas")
    print("4 - Sair")

    print()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        iniciar_recarga()

    elif opcao == "2":

        while True:

            print()
            print("==============================")
            print("INFORMAÇÕES DO CARREGADOR")
            print("==============================")

            print("1 - Cadastrar Carregador")
            print("2 - Editar Carregador")
            print("3 - Listar Carregadores")
            print("4 - Cadastrar Tarifas")
            print("5 - Visualizar Tarifas")
            print("6 - Voltar")

            print()
            sub = input("Escolha uma opção: ")

            if sub == "1":
                cadastrar_carregador()

            elif sub == "2":
                editar_carregador()

            elif sub == "3":
                listar_carregadores()
                pausar()

            elif sub == "4":
                cadastrar_tarifas()

            elif sub == "5":
                visualizar_tarifas()

            elif sub == "6":
                break

            else:
                print()
                print("Opção inválida!")

    elif opcao == "3":
        historico_recargas()

    elif opcao == "4":
        print()
        print("Encerrando sistema...")
        break

    else:
        print()
        print("Opção inválida!")
