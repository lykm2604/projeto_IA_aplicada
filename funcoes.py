# Etapa 4
def avaliacao_resenha(lista) :
    neg = 0
    pos = 0
    neu = 0
    dicionarios_str = []
    for dicionario in lista : 
        if dicionario["avaliacao"] == "Negativa" :
            neg += 1
        elif dicionario["avaliacao"] == "Positiva" :
            pos += 1
        else :
            neu += 1

        dicionarios_str.append(str(dicionario))

    textos_unidos = "#####".join(dicionarios_str)
    resultado = (f'Avaliação das resenhas:\nPositivas: {pos}\nNegativas: {neg}\nNeutras: {neu}')
    return resultado, textos_unidos