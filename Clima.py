import requests

# 🔑 Coloque sua chave da API aqui
API_KEY = "fcf365f899b8f8cde217ce11781e046c "
CIDADE = "Sao Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&lang=pt_br&units=metric"

def buscar_clima():
    try:
        resposta = requests.get(URL)
        
        # Verifica se deu erro HTTP
        resposta.raise_for_status()
        
        dados = resposta.json()

        # 📊 Informações importantes
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]

        print("🌤️ Clima atual:")
        print(f"Cidade: {CIDADE}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Condição: {descricao}")
        print(f"Umidade: {umidade}%")

    except requests.exceptions.HTTPError:
        print("❌ Erro na requisição HTTP.")
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão.")
    except requests.exceptions.Timeout:
        print("❌ Tempo de resposta excedido.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro inesperado: {e}")

# 🚀 Executa o programa
buscar_clima()


import requests

