import sqlite3

conn = sqlite3.connect('anime_clientes.db')
cursor = conn.cursor()

# Reset com dados mais completos
cursor.execute('DROP TABLE IF EXISTS Clientes')
cursor.execute('''
CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    anime_origem TEXT
)
''')

# Dados com anime de origem
animes_data = [
    ("Naruto Uzumaki", "naruto@aldeiafolha.com", "Naruto"),
    ("Sasuke Uchiha", "sasuke@uchiha.com", "Naruto"),
    ("Monkey D. Luffy", "luffy@gear5.com", "One Piece"),
    ("Roronoa Zoro", "zoro@santoryu.com", "One Piece"),
    ("Goku", "goku@sayajin.com", "Dragon Ball"),
    ("Vegeta", "vegeta@orgulhosayajin.com", "Dragon Ball"),
    ("Eren Yeager", "eren@shiganshina.com", "Attack on Titan"),
    ("Mikasa Ackerman", "mikasa@ackerman.com", "Attack on Titan"),
    ("Tanjiro Kamado", "tanjiro@kisatsu.com", "Demon Slayer"),
    ("Gojo Satoru", "gojo@mugen.com", "Jujutsu Kaisen"),
    ("Light Yagami", "light@deathnote.com", "Death Note"),
    ("L Lawliet", "l@watari.com", "Death Note")
]

cursor.executemany("INSERT INTO Clientes (nome, email, anime_origem) VALUES (?, ?, ?)", animes_data)
conn.commit()

print("🎴 CONSULTAS COM CHAKRA AVANÇADO 🎴\n")

# 1. Personagens com nome começando em 'G'
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'G%'")
print("⚡ Personagens com nome começando em 'G':")
for r in cursor.fetchall():
    print(f"   👤 {r[1]} | 📧 {r[2]} | 🎬 {r[3]}")

# 2. Personagens do anime "One Piece"
cursor.execute("SELECT * FROM Clientes WHERE anime_origem = 'One Piece'")
print("\n☠️ Tripulação do Chapéu de Palha (One Piece):")
for r in cursor.fetchall():
    print(f"   🏴‍☠️ {r[1]} - {r[2]}")

# 3. Personagens com 'a' no nome (case insensitive)
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE '%a%' ORDER BY nome")
print("\n📜 Personagens com a letra 'a' no nome:")
for i, r in enumerate(cursor.fetchall()[:8], 1):
    print(f"   {i}. {r[1]} ({r[3]})")

# 4. Quantos personagens por anime
cursor.execute("SELECT anime_origem, COUNT(*) FROM Clientes GROUP BY anime_origem")
print("\n📊 Ranking de animes no banco de dados:")
for anime, total in cursor.fetchall():
    barra = "🟣" * total
    print(f"   {anime:15} : {total} personagem(ns) {barra}")

conn.close()
