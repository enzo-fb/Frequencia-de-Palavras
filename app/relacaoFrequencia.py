import os

def verificarFrequencia(texto):
    relacaoFinal = {} # dicionário para armazenar a tabela
    listaDePalavras = texto.split() #lista com palavras do texto
    for x in listaDePalavras:
        contagem = listaDePalavras.count(x)
        relacaoFinal.update({x:contagem})
    return relacaoFinal


def tabela(relacao):
    relacaoOrdenada = dict(sorted(relacao.items(), key=lambda item: item[1], reverse=True))
    os.system('clear')
    print("Palavras - Frequência\t")
    for x in relacaoOrdenada.items():
        print(x)