#coding: utf-8
import json
import GerenciarPerguntas
import os #para debug, limpar o console
import time #pausar execução do programa

time_duration = 10 #pausar execução do programa por 10 segundos, antes de encerrar



ranking = {}
score = 0
#Funções
def novo_jogo(): 
    lista_Respostas = []
    respostas_corretas = 0
    questao_num = 1
    dificuldade_num = 0
    score = 0
    for x in questoes:
        print("---------")
        print(x)
        for i in opcoes[questao_num-1]:
            print(i)
        dificuldadeQuestao = dificuldade[dificuldade_num]
        print(f"Nível de dificuldade: {dificuldadeQuestao.upper()}")
        resposta = input("Digite a alternativa correta (A, B, C, ou D): ")
        resposta = resposta.upper()
        lista_Respostas.append(resposta)

        respostas_corretas += Confirmar_Respostas(questoes.get(x), resposta, dificuldadeQuestao)
        questao_num += 1
        dificuldade_num += 1

    mostrar_pontuação(respostas_corretas, lista_Respostas)

# Função para verificar se a resposta está de fato correta
def Confirmar_Respostas(resposta_usuario, resposta, dificuldadeQuestao):
    if resposta_usuario == resposta:
        print("CORRETO!")
        calcular_score(dificuldadeQuestao)
        return 1
    else:
        print("ERRADO!")
        return 0

#Calcular pontuação se a questão for respondida corretamente
def calcular_score(dificuldadeQuestao):
    global score
    if (dificuldadeQuestao.upper() == 'FÁCIL' or dificuldadeQuestao.upper() == 'FACIL'):
        print("Você ganhou 10 pontos!") #acertou a questão fácil, ganha 10 pontos no score
        score = score + 10
    elif (dificuldadeQuestao.upper() == 'MÉDIO' or dificuldadeQuestao.upper() == 'MEDIO'):
        print("Você ganhou 20 pontos!") #acertou a questão de nível médio, ganha 20 pontos no score
        score = score + 20
    elif (dificuldadeQuestao.upper() == 'DIFÍCIL' or dificuldadeQuestao.upper() == 'DIFICIL'):
        print("Você ganhou 30 pontos!") #acertou a questão de nível difícil, ganha 30 pontos no score
        score = score + 30
#Função para mostrar a pontuação do jogador na rodada de perguntas
def mostrar_pontuação(respostas_corretas, lista_Respostas):
    global score
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-------------------------")
    print("RESULTADOS")
    print("-------------------------")

    print("RESPOSTAS CORRETAS: ", end="")
    for i in questoes:
        print(questoes.get(i), end=" ")
    print()

    print("RESPOSTAS DO USUÁRIO: ", end="")
    for i in lista_Respostas:
        print(i, end=" ")
    print()

    #Salvar nome do jogador e exibir sua pontuação
    NomeJogador = str(input("Digite o nome do Jogador! "))
    print("Sua pontuação é: "+str(score)+"")
    ranking.update({f'{NomeJogador}': score})
    score = 0 #redefinir score para 0

# -------------------------
def Nova_Rodada(): #se  o jogador disser sim, uma nova rodada irá se iniciar. Caso NÃO, o programa será encerrado.

    jogarnovamente = input("Deseja jogar novamente? (sim ou não): ")
    jogarnovamente = jogarnovamente.upper()

    if jogarnovamente == "SIM":
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        return False
# -------------------------

#INICIO DO CODIGO

while True:
    resposta = int(input(f"Seja bem vindo ao QUIZ! Digite a opção desejada.\n 1 - Iniciar Quiz \n 2 - Gerenciar Perguntas\n"))
    if resposta == 1:
        #Importar arquivos com questões, dificuldades e opções
        with open("questoes.json") as file: 
            questoes = json.load(file)
        with open("opcoes.json") as file: 
            opcoes = json.load(file)
        with open("dificuldades.json") as file: 
            dificuldade = json.load(file)
        novo_jogo()

        while Nova_Rodada():
            novo_jogo()

        print("Fim de jogo!")

        #Imprimir ranking, caso tenha mais de um jogador na rodada.
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(ranking) > 1:
            print("***********************************************")
            print ("Ranking")
            print("***********************************************")
            #Ranking decrescente
            for i in sorted(ranking, key = ranking.get, reverse=True):
                print(f"{i} | {ranking[i]}pts")
            with open(f'RANKING.txt', 'w') as f:
                            f.write(f"RANKING \n")
                            for i in sorted(ranking, key = ranking.get, reverse=True):
                                    f.write(f"{i} | {ranking[i]}pts\n")
                            print("")
                            print("O arquivo RANKING.txt foi gerado e salvo no diretório do programa.")
        print("Obrigado por utilizar o programa!")
        time.sleep(time_duration)
        break
    if resposta == 2:
        #O usuário será levado para a parte do programa responsável por gerenciar as questões.
        print("Seja bem vindo ao programa para cadastrar ou remover as perguntas.")
        print("Se deseja adicionar uma pergunta, digite 1. Caso queira remover, digite 2. ")
        opcao = int(input("Digite a opcao [1/2]: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        with open("questoes.json") as file: 
            questoes = json.load(file)
        with open("opcoes.json") as file: 
            opcoes = json.load(file)
        with open("dificuldades.json") as file: 
            dificuldade = json.load(file)

        if opcao == 1:
            print("CADASTRAR PERGUNTA")
            pergunta = str(input("Digite o titulo da pergunta: "))
            resp1 = str(input("Digite a primeira alternativa para resposta: "))
            resp2 = str(input("Digite a segunda alternativa para resposta: "))
            resp3 = str(input("Digite a terceira alternativa para resposta: "))
            resp4 = str(input("Digite a quarta alternativa para resposta: "))
            dificuldadePerg = str(input("Digite o nivel de dificuldade da pergunta [Facil/Medio/Dificil]: ")).upper()
            respPergunta = str(input("Digite a resposta correta da pergunta [A/B/C/D]: ")).upper()
            GerenciarPerguntas.CadastrarPergunta(pergunta, respPergunta, dificuldadePerg, resp1, resp2, resp3, resp4)
            GerenciarPerguntas.FuncaoAtualizarArquivo()
            

        elif opcao == 2:
            print("PERGUNTAS CADASTRADAS")
            print("-------------------------------------------")
            ListaQuestoes = [*questoes]
            for a in ListaQuestoes:
                print(f"{a}")
                print("____________________________________________")
            print("--")
            print("REMOVER PERGUNTA:")
            pergunta = str(input("Digite a pergunta que deseja remover: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            GerenciarPerguntas.RemoverPergunta(pergunta)
            GerenciarPerguntas.FuncaoAtualizarArquivo()
            
                

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção Inválida. ")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida.")

