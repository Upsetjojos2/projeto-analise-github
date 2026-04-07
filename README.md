# Projeto de Análise de Linguagens de Repositórios GitHub

Este projeto utiliza Python para coletar e analisar dados de repositórios públicos no GitHub de empresas como Amazon, Netflix e Spotify. O foco é identificar as linguagens de programação mais utilizadas em seus projetos open-source.

## Funcionalidades

- **Coleta de Dados**: Faz requisições à API do GitHub para obter informações sobre repositórios.
- **Processamento**: Organiza os dados em DataFrames usando pandas.
- **Armazenamento**: Salva os dados em arquivos CSV.
- **Upload Automático**: Envia arquivos para um repositório GitHub personalizado.

## Tecnologias Utilizadas

- Python
- Requests (para APIs)
- Pandas (para manipulação de dados)
- Base64 (para encoding de arquivos)
- GitHub API

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Upsetjojos2/projeto-analise-github.git
   cd projeto-analise-github
   ```

2. Instale as dependências:
   ```bash
   pip install requests pandas
   ```

3. Configure a variável de ambiente para o token do GitHub:
   ```bash
   export GITHUB_TOKEN=seu_token_aqui
   ```

4. Execute os scripts:
   - `python dados_repo.py` para coletar dados.
   - `python manipula_repos.py` para criar repo e fazer upload.

## Estrutura do Projeto

- `dados_repo.py`: Script para coleta de dados.
- `manipula_repos.py`: Classe para manipulação de repositórios GitHub.
- `microsoft.py`: Exemplo para Microsoft.
- `linguagens_repos.ipynb`: Notebook Jupyter com exemplos.
- `dados/`: Pasta com arquivos CSV gerados.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests!

## Licença

Este projeto é open-source. Use por sua conta e risco.