from exceptionPersonalizada import  ExtrapolacaoDeCaracteres

def verificarFrequencia(texto):
    relacaoFinal = {} # dicionário para armazenar a tabela
    listaDePalavras = texto.split() #lista com palavras do texto
    for x in listaDePalavras:
        contagem = verificarFrequencia(x,listaDePalavras)
        relacaoFinal.update({x:contagem})
    return relacaoFinal


texto = str(input("Digite o texto a ser verificado:"))
try:
    if len(texto)>2048:
        raise ExtrapolacaoDeCaracteres("Texto com número de caracteres maior que o permitido!")
except ExtrapolacaoDeCaracteres as e:
    print(e)
       
relacao = verificarFrequencia(texto) #recebe o dicionário




