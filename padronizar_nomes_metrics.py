import os
import shutil

METRICS_DIR = "metrics"

def organizar_arquivos():
    arquivos = [f for f in os.listdir(METRICS_DIR) if f.endswith(".csv")]

    for arquivo in arquivos:
        nome_base = arquivo.replace("class.csv", "").replace("method.csv", "").strip()

        pasta_destino = os.path.join(METRICS_DIR, nome_base.lower())
        os.makedirs(pasta_destino, exist_ok=True)

        origem = os.path.join(METRICS_DIR, arquivo)

        if "class.csv" in arquivo:
            destino = os.path.join(pasta_destino, "class.csv")
        elif "method.csv" in arquivo:
            destino = os.path.join(pasta_destino, "method.csv")
        else:
            continue

        shutil.move(origem, destino)
        print(f"✅ Movido: {arquivo} → {destino}")

    print("\n🎯 Todos os arquivos foram organizados em subpastas!")

if __name__ == "__main__":
    organizar_arquivos()
