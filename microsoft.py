import requests
import pandas as pd
import base64
import os

api_base_url = "https://api.github.com"
owner = "microsoft"
url = f"{api_base_url}/users/{owner}/repos"

access_token = os.getenv('GITHUB_TOKEN') 

headers = {
    "Authorization": f"Bearer {access_token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

repos_list = []

for page_num in range(1, 10):

    url_page = f"{url}?page={page_num}&per_page=100"
    response = requests.get(url_page, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            repos_list.append(data)

repos_name = []
repos_language = []
repos_description = []

for page in repos_list:
    for repo in page:
        repos_name.append(repo["name"])
        repos_language.append(repo["language"])
        repos_description.append(repo["description"])

dados_microsoft = pd.DataFrame({
    "repo_name": repos_name,
    "language": repos_language,
    "description": repos_description
})

print(dados_microsoft)

dados_microsoft.to_csv("dados_microsoft.csv", index=False)

url_repos = f"{api_base_url}/user/repos"

data_repo = {
    "name": "repos-microsoft",
    "description": "Repositório com dados da Microsoft",
    "private": False
}

response = requests.post(url_repos, json=data_repo, headers=headers)
print("Criação do repo:", response.status_code)  # 201 = criado

# ─── CRIAR E UPLOAD README ───────────────────────────────────
username = "Upsetjojos2"
repo = "repos-microsoft"

readme_content = """# Repos Microsoft

Este repositório contém dados dos repositórios públicos da Microsoft.

## Arquivos

- `dados_microsoft.csv`: Lista de repositórios com nome, linguagem e descrição.
"""

encoded_readme = base64.b64encode(readme_content.encode("utf-8")).decode("utf-8")

url_readme = f"{api_base_url}/repos/{username}/{repo}/contents/README.md"

data_readme = {
    "message": "Adicionando README",
    "content": encoded_readme
}

# Check if README exists
check_readme = requests.get(url_readme, headers=headers)
if check_readme.status_code == 200:
    sha_readme = check_readme.json()["sha"]
    data_readme["sha"] = sha_readme

response_readme = requests.put(url_readme, json=data_readme, headers=headers)
print("Upload README:", response_readme.status_code)

# ─── FORMATANDO O ARQUIVO ───────────────────────────────────
arquivo = "dados_microsoft.csv"

if os.path.exists(arquivo):
    with open(arquivo, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content)
    print("Arquivo lido e codificado!")
else:
    print("Arquivo não encontrado!")

# ─── UPLOAD COM PUT ─────────────────────────────────────────
username = "Upsetjojos2"   
repo = "repos-microsoft"
path = "dados_microsoft.csv"

url_upload = f"{api_base_url}/repos/{username}/{repo}/contents/{path}"

data_upload = {
    "message": "Adicionando dados da Microsoft",
    "content": encoded_content.decode("utf-8")
}

# Check if file exists
check_response = requests.get(url_upload, headers=headers)
if check_response.status_code == 200:
    sha = check_response.json()["sha"]
    data_upload["sha"] = sha

response = requests.put(url_upload, json=data_upload, headers=headers)
print("Upload:", response.status_code)

# ─── DELETAR README ─────────────────────────────────────────
delete_url = f"{api_base_url}/repos/{username}/{repo}/contents/README.md"

# Get sha
get_response = requests.get(delete_url, headers=headers)
if get_response.status_code == 200:
    sha_delete = get_response.json()["sha"]
    data_delete = {
        "message": "Removendo README",
        "sha": sha_delete
    }
    delete_response = requests.delete(delete_url, json=data_delete, headers=headers)
    print("Delete README:", delete_response.status_code)
else:
    print("README não encontrado para deletar")  