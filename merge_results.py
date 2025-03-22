import os
import pandas as pd

BATCHES_DIR = "batches"
METRICS_DIR = "metrics"
PROCESS_METRICS_FILE = "metrics_process.csv"

def carregar_batches():
    arquivos = [f for f in os.listdir(BATCHES_DIR) if f.endswith(".csv")]
    dfs = [pd.read_csv(os.path.join(BATCHES_DIR, f)) for f in arquivos]
    df = pd.concat(dfs, ignore_index=True)
    df["name"] = df["name"].str.strip()
    return df

def carregar_metricas_processuais():
    if os.path.exists(PROCESS_METRICS_FILE):
        df = pd.read_csv(PROCESS_METRICS_FILE)
        df["name"] = df["name"].str.strip()
        return df
    return pd.DataFrame()

def carregar_metricas_ck():
    resultados = []
    for repo in os.listdir(METRICS_DIR):
        class_path = os.path.join(METRICS_DIR, repo, "class.csv")
        if os.path.exists(class_path):
            df = pd.read_csv(class_path)
            if not df.empty:
                resultados.append({
                    "name": repo.strip(),
                    "cbo": df["cbo"].mean(),
                    "dit": df["dit"].mean(),
                    "lcom": df["lcom"].mean(),
                    "loc": df["loc"].sum(),
                    "comment_lines": df["locComment"].sum()
                })
    return pd.DataFrame(resultados)

def juntar_metricas():
    df_repos = carregar_batches()
    df_process = carregar_metricas_processuais()
    df_qualidade = carregar_metricas_ck()

    if not df_process.empty:
        df_repos = pd.merge(df_repos, df_process, on="name", how="left")

    df_final = pd.merge(df_repos, df_qualidade, on="name", how="left")
    df_final.to_csv("metricas_finais.csv", index=False)
    print("Arquivo 'metricas_finais.csv' gerado com sucesso!")

if __name__ == "__main__":
    juntar_metricas()
