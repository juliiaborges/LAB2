
# Laboratório 02 

Este projeto coleta os **1000 repositórios mais populares** escritos em Java no GitHub e realiza análises de métricas relacionadas à sua qualidade e desenvolvimento. (acrescentar mais infos conforme implementações)

---

## 🚀 **Como Executar**

### **1️⃣ Configurar o Token do GitHub**
Antes de rodar o projeto, é necessário **configurar o Token do GitHub** para acessar a API.  
1. Acesse [GitHub Personal Access Tokens](https://github.com/settings/tokens).
2. Gere um token com as permissões de **leitura de repositórios**.
3. Abra o arquivo `config.py` e substitua a linha:
   ```python
   GITHUB_TOKEN = "SEU_TOKEN_AQUI"
   ```
4. Salve o arquivo.

---

### **2️⃣ Criar o Ambiente Virtual (Opcional, Recomendado)**
Para manter o ambiente isolado, execute:

```sh
python -m venv venv
```
Ative o ambiente virtual:
- **Windows**:
  ```sh
  .\venv\Scripts\Activate
  ```
---

### **3️⃣ Instalar as Dependências**
Execute no terminal:
```sh
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, como `requests` e `pandas`.

---

### **4️⃣ Coletar os 1000 Repositórios Java**
Para listar e salvar os repositórios no arquivo CSV, execute:
```sh
python main.py
```
Após a execução, o arquivo `top_java_repos.csv` será gerado com os dados coletados.

---
