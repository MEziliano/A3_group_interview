Este projeto demonstra o treinamento e avaliação de um modelo de Machine Learning (Árvore de Decisão) no conjunto de dados Iris, bem como sua implantação como uma API RESTful usando FastAPI.

### Pré-requisitos

Certifique-se de ter o `Python 3.8+` e `pip` instalados em seu sistema.

### 1. Clonar o Repositório

Primeiro, clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/MEziliano/A3_group_interview/
cd seu_projeto_iris_ml
```

### 2. Criar e Ativar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

**Para ativar o ambiente virtual:**

* **No Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
* **No macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Conteúdo esperado do `requirements.txt`:**

```
scikit-learn
matplotlib
joblib
fastapi
uvicorn[standard]
pydantic
numpy
```


### 4. Reproduzir a Pipeline de Treinamento e Salvar o Modelo

Para treinar o modelo de Árvore de Decisão e salvá-lo para uso pela API, execute o script da pipeline:

```bash
python notebooks/train_and_save_model.py
```

Este script fará o seguinte:
* Carregará o dataset Iris.
* Dividirá os dados em conjuntos de treinamento e teste.
* Treinará o modelo de Árvore de Decisão.
* Avaliará a acurácia do modelo.
* Gerará uma imagem da árvore de decisão (`arvore_decisao_iris.png`).
* **Salvará o modelo treinado** como `app/models/decision_tree_iris_model.pkl`.

Após a execução, você deverá ver uma mensagem de sucesso no terminal e o arquivo `.pkl` será criado dentro da pasta `app/models/`.

Após reproduzir a pipeline e ter o modelo salvo (`app/models/decision_tree_iris_model.pkl`), você pode iniciar a API.

### 1. Certifique-se de que o Ambiente Virtual Está Ativado

Se você fechou o terminal ou desativou o ambiente, ative-o novamente:

* **No Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
* **No macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 2. Iniciar o Servidor FastAPI

Navegue até o diretório raiz do projeto (onde está a pasta `app/`) e execute o Uvicorn para iniciar a API:

```bash
uvicorn app.main:app --reload --port 8000
```

* `app.main`: Indica que a aplicação FastAPI (`app`) está definida no módulo `main` dentro do pacote `app`.
* `--reload`: Útil para desenvolvimento, pois o servidor reiniciará automaticamente ao detectar mudanças no código.
* `--port 8000`: A API estará acessível na porta 8000. Você pode usar outra porta se preferir.

Você verá uma saída no terminal indicando que o Uvicorn está rodando, algo como:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxx]
INFO:     Started server process [xxxx]
INFO:     Waiting for application startup.
Modelo 'app/models/decision_tree_iris_model.pkl' carregado com sucesso na inicialização.
INFO:     Application startup complete.
```

### 3. Acessar a Documentação da API

Com a API rodando, abra seu navegador e acesse as URLs de documentação interativa:

* **Swagger UI (recomendado para testar):**
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:**
    [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Na interface Swagger UI, você pode testar o endpoint `/predict` fornecendo os 4 parâmetros da flor Iris (comprimento da sépala, largura da sépala, comprimento da pétala, largura da pétala) e ver a previsão retornada pelo modelo.

#### Exemplo de requisição `curl` para o endpoint `/predict`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "sepal_length": 5.1,
           "sepal_width": 3.5,
           "petal_length": 1.4,
           "petal_width": 0.2
         }'
```
