# Etapa 1
lista_de_resenhas = []
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

print("\n".join(lista_de_resenhas))