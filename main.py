# main.py
import requests
import pandas as pd
from config import GITHUB_TOKEN

GITHUB_API_URL = "https://api.github.com/search/repositories"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def fetch_top_repositories(language="Java", per_page=100, total_repos=1000):
    repos = []
    pages = total_repos // per_page
    for page in range(1, pages + 1):
        params = {
            "q": f"language:{language}",
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
            "page": page
        }
        response = requests.get(GITHUB_API_URL, headers=HEADERS, params=params)
        if response.status_code == 200:
            data = response.json()
            repos.extend(data["items"])
        else:
            print(f"Erro ao buscar dados: {response.status_code}")
            break
    return repos

def save_to_csv(repositories, filename="top_java_repos.csv"):
    df = pd.DataFrame(repositories)
    df.to_csv(filename, index=False)
    print(f"Arquivo salvo: {filename}")

def main():
    print("Buscando os 1000 repositórios Java mais populares...")
    repositories = fetch_top_repositories()
    if repositories:
        filtered_repos = [
            {
                "name": repo["name"],
                "owner": repo["owner"]["login"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "language": repo["language"],
                "url": repo["html_url"]
            }
            for repo in repositories
        ]
        save_to_csv(filtered_repos)
    else:
        print("Nenhum repositório encontrado.")

if __name__ == "__main__":
    main()