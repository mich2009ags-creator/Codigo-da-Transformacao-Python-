import sqlite3

conn = sqlite3.connect('anime_clientes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')
conn.commit()

def inserir_cliente(nome, email):
    try:
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print(f"⚡ Cliente '{nome}' foi inserido no reino dos animes!")
    except sqlite3.IntegrityError:
        print("❌ Esse email já existe na Akatsuki!")

def consultar_clientes():
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    if clientes:
        print("\n🎌 CLÃ DOS ANIMES 🎌")
        print("-" * 40)
        for c in clientes:
            print(f"🟣 ID: {c[0]} | 👤 Nome: {c[1]} | 📧 Email: {c[2]}")
        print("-" * 40)
    else:
        print("📭 Nenhum cliente ainda... A vila está vazia.")
    return clientes

def atualizar_cliente(id, novo_nome, novo_email):
    cursor.execute("UPDATE Clientes SET nome=?, email=? WHERE id=?", (novo_nome, novo_email, id))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"🔁 Cliente ID {id} teve seu chakra atualizado!")
    else:
        print(f"⚠️ Cliente ID {id} não existe na folha de cadastro.")

def deletar_cliente(id):
    cursor.execute("DELETE FROM Clientes WHERE id=?", (id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"💀 Cliente ID {id} foi deletado... Sayonara!")
    else:
        print(f"👻 Cliente ID {id} não foi encontrado nem com Sharingan.")

# Dados de animes
personagens = [
    ("Naruto Uzumaki", "naruto@folha.com"),
    ("Monkey D. Luffy", "luffy@chapéupalha.com"),
    ("Goku", "goku@dbz.com"),
    ("Eren Yeager", "eren@titan.com"),
    ("Levi Ackerman", "levi@reconhecimento.com"),
    ("Tanjiro Kamado", "tanjiro@demon.com"),
    ("Gojo Satoru", "gojo@jujutsu.com"),
    ("Edward Elric", "edward@alquimia.com")
]

for nome, email in personagens:
    inserir_cliente(nome, email)

consultar_clientes()
atualizar_cliente(3, "Vegeta", "vegeta@dbz.com")
deletar_cliente(7)
consultar_clientes()

conn.close()
