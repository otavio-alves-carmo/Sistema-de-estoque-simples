# Sistema de estoque
mouse = 0
teclado = 0
monitor = 0
while True:
    print("\nEscolha qual dos itens para a venda ou entrada")
    print("1. mouse")
    print("2. teclado")
    print("3. monitor")
    print("4. exibir estoque")
    print("5. saida")
    escolha = input("Escolha uma opção")
    if escolha == "1":
        tipo = input("Vai ser saida ou entrada de estoque? (entrada/saida): ")
        quantidade = int(input("Qual vai ser a quantidade? "))
        if tipo == "entrada":
            mouse += quantidade
            print("Entrada feita com sucesso!")
            print("Estoque total do mouse", mouse)
        elif tipo == "saida":
            mouse -= quantidade
            print("saida feita com sucesso!")
            print("Estoque total do mouse", mouse)
    if  escolha == "2":
        tipo = input("Vai ser saida ou entrada de estoque? (entrada/saida): ")
        quantidade = int(input("Qual vai ser a quantidade? "))
        if tipo == "entrada":
            teclado += quantidade
            print("Entrada feita com sucesso!", teclado)
            print("Estoque total do teclado", teclado)
        elif tipo == "saida":
            teclado -= quantidade
            print("Saida feita com sucesso!", teclado)
            print("Estoque total do teclado", teclado)
    if  escolha == "3":
        tipo = input("Vai ser saida ou entrada de estoque? (entrada/saida): ")
        quantidade = int(input("Qual vai ser a quantidade? "))
        if tipo == "entrada":
            monitor += quantidade
            print("Entrada feita com sucesso!", monitor)
            print("Estoque total do monitor", monitor)
        elif tipo == "saida":
            monitor -= quantidade
            print("Saida feita com sucesso!", monitor)
            print("Estoque total do monitor", monitor)
    if escolha == "4":
        print("estoque do mouse: ", mouse)
        print("estoque do teclado: ", teclado)
        print("estoque do monitor: ", monitor)
    if escolha == "5":
        print("Saindo...")
        break