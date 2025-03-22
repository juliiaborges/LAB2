import os
import subprocess
import shutil
import pandas as pd
import sys
import stat  # <-- esse aqui estava faltando

CK_JAR_PATH = "ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"
REPOS_DIR = "repos"
METRICS_DIR = "metrics"

def handle_remove_readonly(func, path, exc):
    # Remove atributo de somente leitura e tenta novamente
    os.chmod(path, stat.S_IWRITE)
    func(path)

def run_ck(repo_name):
    repo_path = os.path.join(REPOS_DIR, repo_name)
    output_path = os.path.join(METRICS_DIR, repo_name)
    os.makedirs(output_path, exist_ok=True)

    try:
        subprocess.run([
            "java", "-jar", CK_JAR_PATH,
            repo_path, "false", "0", "false", output_path
        ], check=True)
        print("Metrics extracted!!!")
    except:
        print(f"Erro ao rodar CK em {repo_name}")
    finally:
        try:
            shutil.rmtree(repo_path, onerror=handle_remove_readonly)
        except Exception as e:
            print(f"Erro ao remover pasta {repo_path}: {e}")

def analyze_batch(csv_file):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        repo_name = row["name"]
        if os.path.exists(os.path.join(REPOS_DIR, repo_name)):
            run_ck(repo_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python analyze_batch.py batches/batch_X.csv")
    else:
        analyze_batch(sys.argv[1])
