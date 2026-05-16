import sqlite3
import os
from datetime import datetime

conn = sqlite3.connect('missoes_anime.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Missoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    dificuldade TEXT DEFAULT 'D',
    rank TEXT DEFAULT 'E',
    status TEXT DEFAULT 'pendente',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_rank(dificuldade):
    ranks = {
        'S': '🔴🟣🔴 MISSAO RANK S - ULTRA RARO 🔴🟣🔴',
        'A': '🟠🟡 MISSAO RANK A - ALTO RISCO 🟡🟠',
        'B': '🔵 MISSAO RANK B - MEDIO 🔵',
        'C': '🟢 MISSAO RANK C - BAIXO 🟢',
        'D': '⚪ MISSAO RANK D - TREINAMENTO ⚪'
    }
    return ranks.get(dificuldade, '❓ MISSAO SEM RANK')

def menu():
    while True:
        print("\n" + "="*50)
        print("🔥  SISTEMA DE MISSOES NINJA  🔥")
        print("="*50)
        print("⚡ 1. Registrar nova missão")
        print("📜 2. Listar todas as missões")
        print("⏳ 3. Missões pendentes")
        print("✅ 4. Concluir missão (Ganhe XP!)")
        print("💀 5. Excluir missão falha")
        print("🏆 6. Ver estatísticas ninja")
        print("👋 7. Sair da aldeia")
        
        opcao = input("\n🔮 Escolha seu jutsu (1-7): ")
        
        if opcao == '1':
            titulo = input("📝 Nome da missão: ")
            print("\nDificuldade:")
            print("  S - Impossível | A - Alto | B - Médio | C - Baixo | D - Treino")
            dificuldade = input("🎯 Rank (S/A/B/C/D): ").upper()
            if dificuldade not in ['S','A','B','C','D']:
                dificuldade = 'D'
            cursor.execute("INSERT INTO Missoes (titulo, dificuldade, rank) VALUES (?, ?, ?)", 
                           (titulo, dificuldade, dificuldade))
            conn.commit()
            print(f"\n✨ Missão '{titulo}' registrada! {mostrar_rank(dificuldade)}")
        
        elif opcao == '2':
            cursor.execute("SELECT * FROM Missoes ORDER BY data_criacao DESC")
            missoes = cursor.fetchall()
            if missoes:
                print("\n📜 TODAS AS MISSOES DA VILA:")
                print("-"*50)
                for m in missoes:
                    status_icon = "🏆" if m[4] == 'concluida' else "⚡"
                    rank_icon = "🔴" if m[2]=='S' else "🟠" if m[2]=='A' else "🟡" if m[2]=='B' else "🟢" if m[2]=='C' else "⚪"
                    print(f"{status_icon}{rank_icon} [{m[0]}] {m[1]} (Rank {m[2]}) - {m[4].upper()}")
            else:
                print("📭 Nenhuma missão ainda... Que tal aceitar um rank D?")
        
        elif opcao == '3':
            cursor.execute("SELECT * FROM Missoes WHERE status = 'pendente' ORDER BY 
                           CASE rank WHEN 'S' THEN 1 WHEN 'A' THEN 2 WHEN 'B' THEN 3 WHEN 'C' THEN 4 ELSE 5 END")
            pendentes = cursor.fetchall()
            if pendentes:
                print("\n⏳ MISSOES PENDENTES (Urgência primeiro):")
                for p in pendentes:
                    print(f"   🔥 [{p[0]}] Rank {p[2]} - {p[1]}")
            else:
                print("🎉 Todas as missões foram cumpridas! Ninja lendário!")
        
        elif opcao == '4':
            cursor.execute("SELECT id, titulo, rank FROM Missoes WHERE status = 'pendente'")
            pendentes = cursor.fetchall()
            if pendentes:
                print("\n🎯 Missões para concluir:")
                for p in pendentes:
                    print(f"   ID {p[0]} | Rank {p[2]} | {p[1]}")
                id_mission = input("\n🆔 ID da missão cumprida: ")
                cursor.execute("UPDATE Missoes SET status = 'concluida' WHERE id = ?", (id_mission,))
                conn.commit()
                print("✨✨✨ MISSAO CUMPRIDA! +1000 XP ✨✨✨")
            else:
                print("😴 Sem missões pendentes... Aproveite o onsen!")
        
        elif opcao == '5':
            cursor.execute("SELECT id, titulo, rank FROM Missoes")
            todas = cursor.fetchall()
            if todas:
                print("\n💀 Todas as missões cadastradas:")
                for t in todas:
                    print(f"   ID {t[0]} | Rank {t[2]} | {t[1]}")
                id_mission = input("\n❌ ID da missão falha (excluir): ")
                cursor.execute("DELETE FROM Missoes WHERE id = ?", (id_mission,))
                conn.commit()
                print("💀 Missão excluída... Falhou como ninja.")
            else:
                print("📭 Nenhuma missão para excluir.")
        
        elif opcao == '6':
            cursor.execute("SELECT COUNT(*) FROM Missoes")
            total = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Missoes WHERE status = 'concluida'")
            concluidas = cursor.fetchone()[0]
            cursor.execute("SELECT rank, COUNT(*) FROM Missoes GROUP BY rank")
            print("\n🏆 ESTATÍSTICAS DO NINJA:")
            print(f"   • Total de missões: {total}")
            print(f"   • Taxa de conclusão: {concluidas/total*100:.1f}%" if total > 0 else "   • Sem missões")
            print("   • Missões por rank:")
            for rank, qtd in cursor.fetchall():
                barra = "⭐" * qtd
                print(f"      Rank {rank}: {qtd} {barra}")
        
        elif opcao == '7':
            print("\n👋 Sayonara! Que o poder do anime esteja com você!")
            break
        
        else:
            print("❌ Jutsu inválido! Tente novamente.")

if __name__ == "__main__":
    menu()
    conn.close()
