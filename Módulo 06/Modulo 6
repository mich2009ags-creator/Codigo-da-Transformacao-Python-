import json, csv, os, shutil

def main():
    while True:
        print("\n1-TXT  2-JSON  3-CSV  4-Backup  5-Sair")
        op = input("Escolha: ")
        
        if op == "1":
            with open("dados.txt", "w") as f: f.write(input("Digite algo: "))
            print("✅ Salvo! Conteúdo:", open("dados.txt").read())
        
        elif op == "2":
            clientes = {}
            while True:
                n = input("Nome (sair): ")
                if n.lower() == 'sair': break
                clientes[n] = input("Telefone: ")
            json.dump(clientes, open("clientes.json", "w"), indent=2)
            print("✅ Salvos!", json.load(open("clientes.json")))
        
        elif op == "3":
            with open("notas.csv", "a") as f:
                if os.path.getsize("notas.csv") == 0: f.write("Nome,Nota1,Nota2,Nota3,Media\n")
                n = input("Nome: ")
                n1,n2,n3 = float(input("N1:")), float(input("N2:")), float(input("N3:"))
                f.write(f"{n},{n1},{n2},{n3},{(n1+n2+n3)/3:.2f}\n")
            print("✅ Salvo!\n", open("notas.csv").read())
        
        elif op == "4":
            os.makedirs("origem", exist_ok=True); os.makedirs("destino", exist_ok=True)
            for f in ["teste1.txt", "teste2.txt"]: open(f"origem/{f}","w").write("backup")
            for f in os.listdir("origem"): shutil.copy(f"origem/{f}", f"destino/{f}")
            print("✅ Backup feito!", os.listdir("destino"))
        
        elif op == "5":
            print("Até mais!"); break
        
        input("\nEnter...")

if __name__ == "__main__":
    main()
