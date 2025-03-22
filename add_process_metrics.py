import pandas as pd
import requests
import sys
from datetime import datetime

GITHUB_API = "https://api.github.com/repos"

def get_repo_data(owner, repo):
    url = f"{GITHUB_API}/{owner}/{repo}"
    releases_url = f"{url}/releases"

    try:
        repo_resp = requests.get(url)
        repo_data = repo_resp.json()
        created_at = repo_data.get("created_at", None)

        releases_resp = requests.get(releases_url)
        releases = len(releases_resp.json()) if releases_resp.status_code == 200 else 0

        age_years = 0
        if created_at:
            created = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
            now = datetime.now()
            age_years = round((now - created).days / 365, 2)

        return releases, age_years

    except Exception as e:
        print(f"Erro em {owner}/{repo}: {e}")
        return 0, 0

def enrich_with_process_metrics(csv_file):
    df = pd.read_csv(csv_file)
    releases_list = []
    age_list = []

    for _, row in df.iterrows():
        owner = row["owner"]
        name = row["name"]
        releases, age = get_repo_data(owner, name)
        releases_list.append(releases)
        age_list.append(age)

    df["releases"] = releases_list
    df["age_years"] = age_list

    enriched_file = csv_file.replace(".csv", "_with_process.csv")
    df.to_csv(enriched_file, index=False)
    print(f"Arquivo salvo: {enriched_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python add_process_metrics.py batches/batch_X.csv")
    else:
        enrich_with_process_metrics(sys.argv[1])
