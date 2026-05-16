import requests

API_KEY = "SUA_CHAVE_TMDB"
FILME = "Inception"

url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={FILME}&language=pt-BR"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    filme = dados["results"][0]

    print("\n🎬 Filme:")
    print(f"Título: {filme['title']}")
    print(f"Sinopse: {filme['overview']}")
    print(f"Data de lançamento: {filme['release_date']}")

except Exception as e:
    print(f"Erro: {e}")
