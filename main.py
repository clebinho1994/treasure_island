print('''Bem vindo à ilha do Tesouro!
Sua missão é encontrar o tesouro.''')

lado = input("Escolha um lado: direito ou esquerdo? ")
if lado == "direito":
    print('''Caiu em um buraco!
    Fim de jogo!''')

else:
    print('''Você chegou em um lago!
    Espere um barco ou nade até o outro lado.''')
    acao = input("Escolha uma opção: esperar ou nadar? ")

    if acao == "nadar":
        print('''Atacado por um Crododilo!
        Fim de jogo!''')
    else:
        print('''Agora você se depara com 3 portas.
        Qual delas deseja abrir?''')
        porta = input("Escolha uma opção: amarela, vermelha ou azul? ")
        if porta == "red":
            print('''Você pegou fogo!
            Fim de jogo!''')
        elif porta == "blue":
            print('''Você foi devorado por Ursos!
            Fim de jogo!''')
        elif porta == "":
            print('''Fim de jogo!''')
        else:
            print('''Você ganhou!!''')

