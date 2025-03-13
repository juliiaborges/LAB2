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

## 🛠️ Passo a Passo Para Executar o Código

### **1️⃣ Configurar o Ambiente**  
Antes de iniciar, certifique-se de ter **Python 3.8+** instalado. Se necessário, crie um ambiente virtual para manter as dependências organizadas:

```sh
python -m venv venv
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

Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```

---

### **2️⃣ Configurar o Token do GitHub**  
Para acessar a API do GitHub, você precisa de um **Personal Access Token**.  

1. Vá até [GitHub Tokens](https://github.com/settings/tokens).  
2. Gere um token com permissões de **leitura de repositórios**.  
3. No arquivo `config.py`, substitua:  

   ```python
   GITHUB_TOKEN = "SEU_TOKEN_AQUI"
   ```

---

### **3️⃣ Coletar os 1000 Repositórios Java Mais Populares**  
Para obter os repositórios e armazená-los em um arquivo CSV, execute:

```sh
python main.py
```

Isso irá:  
✅ Buscar os **1000 repositórios Java mais populares**.  
✅ Gerar um arquivo `top_java_repos.csv` contendo os dados coletados.  

---
