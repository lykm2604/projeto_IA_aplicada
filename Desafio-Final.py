import json
from contato_com_LLM import retorno_em_json
# Etapa 1

lista_de_resenhas = []
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

# Etapa 2

lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = retorno_em_json(resenha)
    resenha_dict = (resenha_json)
    lista_de_resenhas_json.append(resenha_dict)
