import requests

BASE_URL = 'http://127.0.0.1:8000' 
rotas = ['/', '/matriculas', '/matriculas/1']

for rota in rotas:
    try:
        resposta = requests.get(BASE_URL + rota)
        print(f'{rota}: {resposta.status_code}')
        print(resposta.json())
        print("-" * 30)
    except requests.exceptions.ConnectionError:
        print(f"Erro: Não foi possível conectar em {BASE_URL}. A API está ligada?")
