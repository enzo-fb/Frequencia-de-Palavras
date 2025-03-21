from exceptionPersonalizada import  ExtrapolacaoDeCaracteres 
from exceptionPersonalizada import EmptyInputError
import os
def verificarFrequencia(texto):
    relacaoFinal = {} # dicionário para armazenar a tabela
    listaDePalavras = texto.split() #lista com palavras do texto
    for x in listaDePalavras:
        contagem = listaDePalavras.count(x)
        relacaoFinal.update({x:contagem})
    return relacaoFinal

def tratarErro(texto):

        if len(texto)>2048:
            raise ExtrapolacaoDeCaracteres("Texto com número de caracteres maior que o permitido!")

        texto = texto.strip()

        if len(texto)==0:
            raise EmptyInputError("Caixa de texto vazia!")        
 
def tabela(relacao):
    relacaoOrdenada = dict(sorted(relacao.items(), key=lambda item: item[1], reverse=True))
    os.system('clear')
    print("Palavras - Frequência\t")
    for x in relacaoOrdenada.items():
        print(x)

texto = input("Digite o texto a ser verificado:").lower()
tratarErro(texto)      
relacao = verificarFrequencia(texto) #recebe o dicionário
tabela(relacao)





