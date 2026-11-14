# Jogo da Velha - Coding (UNINASSAU)
# Alunos: Gustavo Mateus Santana Ferreira e Miguel Lucas Mendes do Monte

# Inicialização do placar
vitorias_x = 0
vitorias_o = 0
empates = 0

# Loop principal do menu controlado por while
executando = True

while executando == True:
    print("========================================")
    print("         JOGO DA VELHA NO TERMINAL      ")
    print("========================================")
    print("1. Jogar")
    print("2. Ver Placar")
    print("3. Ver Regras")
    print("4. Sair")
    
    # Leitura e validação da opção do menu (sem isdigit/try-except)
    opcao_valida = False
    opcao_escolhida = ""
    while opcao_valida == False:
        opcao_escolhida = input("Escolha uma opcao (1 a 4): ")
        for n in range(1, 5):
            if opcao_escolhida == str(n):
                opcao_valida = True
        if opcao_valida == False:
            print("Entrada invalida! Digite um numero de 1 a 4.")
            
    if opcao_escolhida == "1":
        # Inicialização da matriz do tabuleiro 3x3 por extenso
        tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        
        simbolo_atual = "X"
        partida_andamento = True
        
        while partida_andamento == True:
            # Exibição do tabuleiro com números de linhas e colunas visíveis usando for aninhado
            print("\n    0   1   2 ")
            print("  -------------")
            for i in range(3):
                linha_texto = str(i) + " |"
                for j in range(3):
                    linha_texto = linha_texto + " " + tabuleiro[i][j] + " |"
                print(linha_texto)
                print("  -------------")
                
            print("Vez do jogador: " + simbolo_atual)
            
            # Leitura e validação da Linha (0 a 2)
            linha_valida = False
            linha_escolhida = 0
            while linha_valida == False:
                entrada_l = input("Escolha a linha (0, 1 ou 2): ")
                for n in range(3):
                    if entrada_l == str(n):
                        linha_valida = True
                        linha_escolhida = n
                if linha_valida == False:
                    print("Linha invalida! Digite 0, 1 ou 2.")
                    
            # Leitura e validação da Coluna (0 a 2)
            coluna_valida = False
            coluna_escolhida = 0
            while coluna_valida == False:
                entrada_c = input("Escolha a coluna (0, 1 ou 2): ")
                for n in range(3):
                    if entrada_c == str(n):
                        coluna_valida = True
                        coluna_escolhida = n
                if coluna_valida == False:
                    print("Coluna invalida! Digite 0, 1 ou 2.")
                    
            # Verificação se a casa está livre
            if tabuleiro[linha_escolhida][coluna_escolhida] == " ":
                tabuleiro[linha_escolhida][coluna_escolhida] = simbolo_atual
                
                # Verificação automática de vitória usando laços for
                venceu = False
                
                # Checagem de linhas
                for i in range(3):
                    if tabuleiro[i][0] == simbolo_atual and tabuleiro[i][1] == simbolo_atual and tabuleiro[i][2] == simbolo_atual:
                        venceu = True
                        
                # Checagem de colunas
                for j in range(3):
                    if tabuleiro[0][j] == simbolo_atual and tabuleiro[1][j] == simbolo_atual and tabuleiro[2][j] == simbolo_atual:
                        venceu = True
                        
                # Checagem de diagonal principal
                if tabuleiro[0][0] == simbolo_atual and tabuleiro[1][1] == simbolo_atual and tabuleiro[2][2] == simbolo_atual:
                    venceu = True
                    
                # Checagem de diagonal secundária
                if tabuleiro[0][2] == simbolo_atual and tabuleiro[1][1] == simbolo_atual and tabuleiro[2][0] == simbolo_atual:
                    venceu = True
                    
                if venceu == True:
                    # Exibe tabuleiro final
                    print("\n    0   1   2 ")
                    print("  -------------")
                    for i in range(3):
                        lt = str(i) + " |"
                        for j in range(3):
                            lt = lt + " " + tabuleiro[i][j] + " |"
                        print(lt)
                        print("  -------------")
                    print("Parabens! O jogador " + simbolo_atual + " venceu a partida!")
                    if simbolo_atual == "X":
                        vitorias_x = vitorias_x + 1
                    else:
                        vitorias_o = vitorias_o + 1
                    partida_andamento = False
                else:
                    # Verificação de empate usando for aninhado para contar casas vazias
                    vazias = 0
                    for i in range(3):
                        for j in range(3):
                            if tabuleiro[i][j] == " ":
                                vazias = vazias + 1
                                
                    if vazias == 0:
                        print("\n    0   1   2 ")
                        print("  -------------")
                        for i in range(3):
                            lt = str(i) + " |"
                            for j in range(3):
                                lt = lt + " " + tabuleiro[i][j] + " |"
                            print(lt)
                            print("  -------------")
                        print("Deu empate!")
                        empates = empates + 1
                        partida_andamento = False
                    else:
                        # Alterna o jogador
                        if simbolo_atual == "X":
                            simbolo_atual = "O"
                        else:
                            simbolo_atual = "X"
            else:
                print("Erro: Esta casa ja esta ocupada! Escolha outra.")
                
    elif opcao_escolhida == "2":
        print("\n--- PLACAR ACUMULADO ---")
        print("Vitorias do Jogador X: " + str(vitorias_x))
        print("Vitorias do Jogador O: " + str(vitorias_o))
        print("Empates: " + str(empates))
        print("------------------------\n")
        
    elif opcao_escolhida == "3":
        print("\n--- REGRAS DO JOGO DA VELHA ---")
        print("- Dois jogadores (X e O) se alternam.")
        print("- O tabuleiro possui 3 linhas e 3 colunas (0 a 2).")
        print("- Vence quem completar primeiro uma linha, coluna ou diagonal.")
        print("- Se o tabuleiro preencher sem vencedor, e empate.\n")
        
    elif opcao_escolhida == "4":
        print("Encerrando o programa. Obrigado por jogar!")
        executando = False
