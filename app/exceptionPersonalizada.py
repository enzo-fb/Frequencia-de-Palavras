class ExtrapolacaoDeCaracteres(Exception):
    
    def __init__(self, mensagem):
        super().__init__(mensagem)  # Passa a mensagem para a classe Exception
