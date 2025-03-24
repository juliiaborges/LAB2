import os
import pandas as pd

BATCHES_DIR = "batches"
METRICS_DIR = "metrics"

def carregar_batches():
    arquivos = [f for f in os.listdir(BATCHES_DIR) if f.endswith(".csv")]
    dfs = [pd.read_csv(os.path.join(BATCHES_DIR, f)) for f in arquivos]
    df = pd.concat(dfs, ignore_index=True)
    df["name"] = df["name"].str.strip()
    df["name_lower"] = df["name"].str.lower()
    return df

def carregar_metricas_ck():
    resultados = []
    for repo in os.listdir(METRICS_DIR):
        class_path = os.path.join(METRICS_DIR, repo, "class.csv")
        if os.path.exists(class_path):
            df = pd.read_csv(class_path)
            if not df.empty:
                resultados.append({
                    "name_lower": repo.strip().lower(),
                    "cbo": df["cbo"].mean(),
                    "dit": df["dit"].mean(),
                    "lcom": df["lcom"].mean(),
                    "loc": df["loc"].sum(),
                   "comment_lines": df["comment_lines"].sum() if "comment_lines" in df.columns else 0

                })
    return pd.DataFrame(resultados)

def juntar_metricas():
    print("📦 Carregando batches...")
    df_repos = carregar_batches()

    print("📊 Carregando métricas CK...")
    df_qualidade = carregar_metricas_ck()

    print("🔗 Unificando dados...")
    if not df_qualidade.empty:
        df_final = pd.merge(df_repos, df_qualidade, on="name_lower", how="left")
        df_final.drop(columns=["name_lower"], inplace=True)
    else:
        df_final = df_repos

    df_final.to_csv("metricas_finais.csv", index=False)
    print("✅ Arquivo 'metricas_finais.csv' gerado com sucesso!")
    print("📁 Caminho:", os.path.abspath("metricas_finais.csv"))

if __name__ == "__main__":
    juntar_metricas()
