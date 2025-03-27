# Laboratório 02 - Análise de Qualidade de Repositórios Java

No desenvolvimento de sistemas open-source, a qualidade do código pode ser impactada por diversos fatores, como a modularidade, manutenibilidade e legibilidade. Neste contexto, este projeto tem como objetivo **analisar a qualidade de repositórios Java utilizando métricas de produto** extraídas pela ferramenta **CK**.

## Metas

- Coletar e analisar os 1.000 repositórios Java mais populares do GitHub.
- Medir e correlacionar a qualidade do código com características como popularidade, maturidade, atividade e tamanho.
- Utilizar métricas de qualidade como **CBO (Coupling Between Objects)**, **DIT (Depth Inheritance Tree)** e **LCOM (Lack of Cohesion of Methods)**.
- Gerar gráficos de correlação entre as métricas.
- Utilizar testes estatísticos para validação dos resultados.
- Apresentar um relatório final com as análises realizadas.

## Metodologia

### 1. Seleção de Repositórios

Utilizando o GraphQL do GitHub, serão coletados os 1.000 repositórios Java mais populares para análise.

### 2. Questões de Pesquisa

As seguintes questões orientam este estudo:

- **RQ01**: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?
- **RQ02**: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?
- **RQ03**: Qual a relação entre a atividade dos repositórios e suas características de qualidade?
- **RQ04**: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

### 3. Definição de Métricas

As métricas consideradas para o estudo incluem:

#### Métricas de Processo:

- **Popularidade**: Número de estrelas do repositório no GitHub.
- **Tamanho**: Linhas de código (LOC) e linhas de comentários.
- **Atividade**: Número de releases.
- **Maturidade**: Idade (em anos) do repositório.

#### Métricas de Qualidade (usando CK):

- **CBO**: Coupling between objects (Acoplamento entre objetos).
- **DIT**: Depth Inheritance Tree (Profundidade da árvore de herança).
- **LCOM**:  Lack of Cohesion of Methods (Falta de coesão entre métodos).

### 4. Coleta e Análise de Dados

- Uso das APIs do GitHub para coleta de informações sobre popularidade, atividade e maturidade.
- Uso da ferramenta **CK** para extração das métricas de qualidade.
- Geração de gráficos de correlação entre as métricas.
- Uso de testes estatísticos para validação dos resultados.
- Geração de gráficos de correlação entre as métricas.
- Uso de testes estatísticos para validação dos resultados.
- Geração de relatório final com sumarização dos dados e análise estatística.

## Tecnologias Utilizadas

- **Java**
- **GraphQL**
- **Ferramenta CK para análise de código**
- **Python para análise estatística e geração de gráficos**
- **Pandas para a geração de gráficos**

# Passo a Passo Para Reprodução do Experimento

## 1. Configurar o Ambiente
Antes de começar, certifique-se de ter **Python 3.8+** instalado. Para manter as dependências organizadas, crie um ambiente virtual:

```sh
python -m venv .venv
```

Ative o ambiente virtual:
- **Windows**:
  ```sh
  .\venv\Scripts\Activate
  ```
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```

---

## 2. Configurar o Token do GitHub
Para acessar a API do GitHub, você precisa de um **Personal Access Token**.

1. Acesse [GitHub Tokens](https://github.com/settings/tokens).
2. Gere um token com permissões de **leitura de repositórios**.
3. No arquivo `config.py`, substitua a linha:

   ```python
   GITHUB_TOKEN = "SEU_TOKEN_AQUI"
   ```

---

## 3. Coletar os 1000 Repositórios Java Mais Populares
Para coletar os repositórios e armazená-los em um arquivo CSV, execute:

```sh
python main.py
```

Este comando irá:
- Buscar os **1000 repositórios Java mais populares**.
- Gerar um arquivo `top_java_repos.csv` com os dados coletados.

---

## 4. Clonando os 1000 Repositórios em 10 Batches
Os 1000 repositórios foram divididos em **10 grupos de 100** na pasta `batches`. Cada grupo é clonado, analisado e excluído após a extração das métricas, reduzindo o uso de memória.

### Clonando os Repositórios
Execute o seguinte comando, substituindo `X` pelo número do batch (1 a 10):

```sh
python clone_repos_batch.py batches/batch_X.csv
```

### Extraindo Métricas dos Repositórios
Após a clonagem, extraia as métricas com:

```sh
python analyze_batch.py batches/batch_X.csv
```

Isso gerará arquivos `batch_X.csv` com as métricas de cada lote.

---

## 5. Adicionar Releases e Idade dos Repositórios
Para cada batch processado (`batch_X.csv`), adicione informações sobre releases e idade do repositório executando:

```sh
python add_process_metrics.py batches/batch_X.csv
```

Isso criará arquivos como:

```sh
batches/batch_0_with_process.csv
batches/batch_1_with_process.csv
...
```

---

## 6. Consolidar os Dados em um Arquivo Final
Para gerar um arquivo final consolidado com as métricas de processo e as métricas CK:
1. Renomeie ou una todos os arquivos `_with_process.csv` em um único arquivo chamado:
   ```sh
   metrics_process.csv
   ```

Após esse processo, o conjunto final de métricas estará pronto para análise.
