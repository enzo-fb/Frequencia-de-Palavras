from exceptionPersonalizada import  ExtrapolacaoDeCaracteres
import os
def verificarFrequencia(texto):
    relacaoFinal = {} # dicionário para armazenar a tabela
    listaDePalavras = texto.split() #lista com palavras do texto
    for x in listaDePalavras:
        contagem = listaDePalavras.count(x)
        relacaoFinal.update({x:contagem})
    return relacaoFinal

def tratarErro(texto):
    try:
        if len(texto)>2048:
            raise ExtrapolacaoDeCaracteres("Texto com número de caracteres maior que o permitido!")
    except ExtrapolacaoDeCaracteres as e:
        return print(e)

 
def tabela(relacao):
    relacaoOrdenada = dict(sorted(relacao.items(), key=lambda item: item[1], reverse=True))
    os.system('clear')
    print("Palavras - Frequência\t")
    for x in relacaoOrdenada.items():
        print(x)


 
texto = str(input("Digite o texto a ser verificado:")).lower()
tratarErro(texto)       
relacao = verificarFrequencia(texto) #recebe o dicionário
tabela(relacao)





