import requests
import pandas as pd

# URL da API pública de conselhos
url = "https://api.adviceslip.com/advice"

# Fazendo a requisição (GET)
resposta = requests.get(url)

# A resposta vem em formato JSON (texto organizado tipo dicionário)
dados = resposta.json()

print(dados)  # só pra ver como vem cru

# Agora vamos organizar em um DataFrame
df = pd.DataFrame([dados['slip']])  # slip é a "chave" no JSON

print(df)
