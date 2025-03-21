from app.exceptionPersonalizada import EmptyInputError, ExtrapolacaoDeCaracteres

def tratarErro(texto):

        if len(texto)>2048:
            raise ExtrapolacaoDeCaracteres("Texto com número de caracteres maior que o permitido!")

        texto = texto.strip()

        if len(texto)==0:
            raise EmptyInputError("Caixa de texto vazia!")        
 