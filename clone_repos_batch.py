import os
import subprocess
import pandas as pd
import sys

def clone_repositories(csv_file):
    df = pd.read_csv(csv_file)
    os.makedirs("repos", exist_ok=True)

    for index, row in df.iterrows():
        repo_url = row["url"]
        repo_name = repo_url.split("/")[-1]
        repo_path = os.path.join("repos", repo_name)

        if os.path.exists(repo_path):
            print(f"✅ Já clonado: {repo_name}")
            continue

        print(f"🔄 Clonando {repo_name}...")

        try:
            subprocess.run(["git", "clone", repo_url, repo_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao clonar {repo_name}: {e}")
        except Exception as e:
            print(f"⚠️ Erro inesperado ao clonar {repo_name}: {e}")
        else:
            print(f"✅ Clonado com sucesso: {repo_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python clone_repos_batch.py batches/batch_1.csv")
        sys.exit(1)

    clone_repositories(sys.argv[1])
