import os
import subprocess
import pandas as pd

CSV_FILE = "top_java_repos.csv"
CLONE_DIR = "cloned_repos"
CK_JAR = "C:\\faculdade\\6 periodo\\laboratorio de exp\\LAB2\\libs\\ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar"

os.makedirs(CLONE_DIR, exist_ok=True)

def clone_repo(repo_url, repo_name):
    """Clona um repositório do GitHub."""
    repo_path = os.path.join(CLONE_DIR, repo_name)
    
    if os.path.exists(repo_path):
        print(f"Repositório {repo_name} já clonado. Pulando...")
        return repo_path
    
    print(f"Clonando {repo_url}...")
    
    result = subprocess.run(["git", "clone", repo_url, repo_path], check=False, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Erro ao clonar {repo_name}: {result.stderr}")
        return None

    return repo_path

def run_ck_analysis(repo_path):
    """Executa a análise do CK no repositório clonado."""
    print(f"Executando CK no repositório {repo_path}...")
    output_dir = os.path.join(repo_path, "ck_results")
    os.makedirs(output_dir, exist_ok=True)
    
    command = ["java", "-jar", CK_JAR, repo_path, "false", "0", "true"]
    subprocess.run(command, check=True)
    
    return os.path.join(repo_path, "class.csv")  

def main():
    # Carregar os repositórios do CSV
    df = pd.read_csv(CSV_FILE)
    
    # Testar com o segundo repositório da lista (índice 1)
    test_repo = df.iloc[1]  # Alterado para pegar o segundo repositório
    repo_name = test_repo["name"]
    repo_url = test_repo["url"].replace("https://github.com/", "https://github.com/") + ".git"
    
    try:
        repo_path = clone_repo(repo_url, repo_name)
        metrics_file = run_ck_analysis(repo_path)
        print(f"Métricas extraídas: {metrics_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao processar {repo_name}: {e}")
    
    # Depois de testar, podemos rodar para todos os 1000
    # for index, row in df.iterrows():
    #     clone_repo(row["url"], row["name"])
    #     run_ck_analysis(os.path.join(CLONE_DIR, row["name"]))

if __name__ == "__main__":
    main()