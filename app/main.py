from exceptionPersonalizada import  ExtrapolacaoDeCaracteres 
from exceptionPersonalizada import EmptyInputError
from tratamentoDeErros import tratarErro
from relacaoFrequencia import tabela, verificarFrequencia


texto = input("Digite o texto a ser verificado:").lower()
tratarErro(texto)      
relacao = verificarFrequencia(texto) #recebe o dicionário
tabela(relacao) #relação final





