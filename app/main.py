from exceptionPersonalizada import  ExtrapolacaoDeCaracteres

def verificarFrequencia(palavra, lista):
    return lista.count(palavra)
    

texto = str(input("Digite o texto a ser verificado:"))
try:
    if len(texto)>2048:
        raise ExtrapolacaoDeCaracteres("Texto com número de caracteres maior que o permitido!")
except ExtrapolacaoDeCaracteres as e:
    print(e)
       
listaDePalavras = texto.split() # lista as palavras
relacaoFinal = {} # dicionário para armazenar a tabela

for x in listaDePalavras:
    contagem = verificarFrequencia(x,listaDePalavras)
    relacaoFinal.update({x:contagem})