from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def retorno_em_json(resenha):
    resposta = client.chat.completions.create(
        model = "google/gemma-3-4b",
        messages = [
            {
                "role": "system",
                "content": """Você é um especialista em análise e conversão de dados para JSON.
                Você receberá uma linha de texto contendo uma resenha de um aplicativo online.
                Sua tarefa é analisar e retornar um JSON com as seguintes chaves:
                - 'usuario' : o nome do usuário que fez a resenha.
                - 'resenha original' : resenha no idioma original.
                - 'resenha traduzida' : resenha traduzida para o português.
                - 'avaliacao' : se a avaliação é 'Positiva', 'Negativa' ou 'Neutra', apenas uma dessas opções.

                Exemplo de entrada:
                '508293$João$This is a positive review for the app, it's very useful and easy to use.'
                Exemplo de saída:
                {
                    "usuario": "João",
                    "resenha original": "This is a positive review for the app, it's very useful and easy to use.",
                    "resenha traduzida": "Esta é uma resenha positiva para o aplicativo, é muito útil e fácil de usar.",
                    "avaliacao": "Positiva"
                }
                
                Você deve retornar apenas o JSON, sem NENHUM outro testo ou explicação.
                """
            }
            ,
            {
                "role": "user",
                "content": f"Resenha: {resenha}"
            }
        ],
        
        temperature = 0.5
    )
    print(resposta.choices[0].message.content)
    return resposta.choices[0].message.content