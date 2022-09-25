#coding: utf-8
import json
import os #para debug, limpar o console
#Importar arquivo com questões, dificuldades e opções
with open("questoes.json") as file: 
    questoes = json.load(file)
with open("opcoes.json") as file: 
    opcoes = json.load(file)
with open("dificuldades.json") as file: 
    dificuldade = json.load(file)

alternativa = []

#Função para atualizar o arquivo a cada modificação nas questões.
def FuncaoAtualizarArquivo():
    with open("questoes.json", "w") as outfile: 
        json.dump(questoes, outfile) 
    with open("dificuldades.json", "w") as outfile: 
        json.dump(dificuldade, outfile) 
    with open("opcoes.json", "w") as outfile: 
        json.dump(opcoes, outfile) 


#Funcao Cadastrar Pergunta
def CadastrarPergunta(pergunta, respPergunta, dificuldadePerg, resp1, resp2, resp3, resp4):
    alternativa.clear()
    if pergunta in questoes:
        print("Erro: pergunta ja cadastrada. ")
        return
    else:
        questoes[f"{pergunta}"] = respPergunta
        dificuldade.append(dificuldadePerg)
        alternativa.append(resp1)
        alternativa.append(resp2)
        alternativa.append(resp3)
        alternativa.append(resp4)
        opcoes.append(alternativa)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pergunta cadastrada!")

#Função para remover uma pergunta
def RemoverPergunta(pergunta):
    if pergunta in questoes:
        ListaQuestoes = [*questoes] #transformando as chaves do dicionário em uma lista, para obter o indíce(int) da pergunta
        indice = (ListaQuestoes.index(f"{pergunta}"))
        del questoes[f'{pergunta}']
        del dificuldade[indice]
        del opcoes[indice]
        print("Pergunta removida com sucesso!")
    else:
        print("Pergunta inválida!")