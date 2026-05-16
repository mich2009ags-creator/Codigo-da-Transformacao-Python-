# Modulo_10/clima_simples.py
import requests

# OBTER SUA CHAVE EM: https://openweathermap.org/api
API_KEY = "fcf365f899b8f8cde217ce11781e046c"
CIDADE = "São Paulo"

try:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url, timeout=10)
    dados = resposta.json()
    
    if resposta.status_code == 200:
        print(f"\nCidade: {dados['name']}")
        print(f"Temperatura: {dados['main']['temp']}°C")
        print(f"Condição: {dados['weather'][0]['description']}")
        print(f"Umidade: {dados['main']['humidity']}%")
    else:
        print(f"Erro: {dados.get('message', 'Falha na requisição')}")
        
except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")
