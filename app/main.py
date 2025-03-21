from exceptionPersonalizada import  ExtrapolacaoDeCaracteres



texto = str(input("Digite o texto a ser verificado:"))
try:
    if len(texto)>2048:
        raise ExtrapolacaoDeCaracteres("Texto com número de caracteres maior que o permitido!")
except ExtrapolacaoDeCaracteres as e:
    print(e)
    
texto.split() # lista as palavras