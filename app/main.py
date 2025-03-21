

texto = str(input("Digite o texto a ser verificado:"))
try:
    len(texto)>2048
except:
    print("Texto com número de caracteres maior que o permitido!")