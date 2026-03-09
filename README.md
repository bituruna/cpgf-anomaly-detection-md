# Detecção de Anomalias no Cartão de Pagamento do Governo Federal (CPGF)

**Disciplina:** Mineração de Dados Aplicada a Finanças
**Curso:** FACOM
**Projeto:** Análise e Detecção de Anomalias em Gastos Públicos
**Base de dados:** Portal da Transparência — Cartão de Pagamento do Governo Federal (CPGF)

**Repositório do projeto:**
https://github.com/bituruna/cpgf-anomaly-detection-md.git

---

# Descrição do Projeto

Este projeto aplica técnicas de **Ciência de Dados e Mineração de Dados** para identificar **padrões atípicos de gastos** realizados com o **Cartão de Pagamento do Governo Federal (CPGF)**.

O objetivo é construir um **pipeline completo de análise de dados**, composto por três etapas principais:

1. **Pré-processamento**
2. **Mineração de Dados e Avaliação**
3. **Pós-processamento e análise de negócio**

A partir dos dados públicos disponibilizados pelo Portal da Transparência, o projeto busca detectar **anomalias estatísticas em perfis de gastos**, que podem indicar comportamentos fora do padrão e servir como ponto de partida para **auditoria e controle público**.

---

# Estrutura do Projeto

```
cpgf-analise-anomalias/
│
├── datasets/                              # Bases de dados utilizadas no projeto
│   └── (arquivos CSV baixados do Google Drive)
│
├── src/                                   # Notebooks do projeto
│   ├── 01_pre_processamento.ipynb
│   ├── 02_mineracao_e_avaliacao.ipynb
│   └── 03_pos_processamento.ipynb
│
├── relatorio/                             # Relatório final do projeto
│   ├── Relatório Projeto Final MD.pdf
│   └── referencias/                       # Artigos científicos e materiais de referência utilizados
│
├── README.md
└── requirements.txt
```

---

# Download das Bases de Dados

As bases de dados utilizadas no projeto não estão incluídas diretamente no projeto devido ao tamanho dos arquivos.

Para executar o projeto corretamente, é necessário baixar os datasets no link abaixo:

https://drive.google.com/drive/folders/1IzUlHcLJuneSwA6k4OuDT7K7czKGmoIF

Passos:

1. Acesse o link do Google Drive.
2. Faça o download de todos os arquivos CSV disponíveis.
3. Crie a pasta `datasets` na raiz do projeto (caso ainda não exista).
4. Coloque todos os arquivos CSV dentro dessa pasta.

Estrutura esperada:

```
cpgf-analise-anomalias/
│
├── datasets/
│   ├── arquivo1.csv
│   ├── arquivo2.csv
│   └── ...
│
├── src/
│   ├── 01_pre_processamento.ipynb
│   ├── 02_mineracao_e_avaliacao.ipynb
│   └── 03_pos_processamento.ipynb
```

Após adicionar os arquivos na pasta `datasets`, os notebooks poderão acessar os dados normalmente.

---

# Etapas do Projeto

## 1. Pré-processamento

Notebook:
`src/01_pre_processamento.ipynb`

Nesta etapa os dados brutos do CPGF passam por um processo de preparação para análise.

Principais atividades:

* Exploração inicial dos dados
* Estatísticas descritivas
* Identificação de inconsistências
* Tratamento de valores ausentes
* Remoção de ruídos
* Seleção de atributos relevantes
* Normalização dos atributos numéricos (Z-Score)

Arquivos gerados:

| Arquivo                | Descrição                                              |
| ---------------------- | ------------------------------------------------------ |
| `cpgf_limpo.csv`       | Dados tratados e consistentes                          |
| `cpgf_normalizado.csv` | Dados padronizados para uso em algoritmos de mineração |

---

# 2. Mineração de Dados e Avaliação

Notebook:
`src/02_mineracao_e_avaliacao.ipynb`

Nesta etapa são aplicadas técnicas de **aprendizado não supervisionado** para identificar padrões de gastos e possíveis anomalias.

Algoritmos utilizados:

* **K-Means**
* **HDBSCAN**

Objetivos da modelagem:

* Identificar **grupos de comportamento de gastos**
* Medir **distância ao centro do cluster**
* Detectar **pontos fora do padrão (outliers)**

Principais técnicas aplicadas:

* Método do Cotovelo (Elbow Method) para escolha de K
* Distância Euclidiana ao centróide
* Detecção de outliers baseada em densidade
* Score de anomalia com HDBSCAN

Resultado:

Cada registro analisado recebe um **score de anomalia**, indicando o nível de divergência em relação ao comportamento típico de gastos.

---

# 3. Pós-processamento e Validação de Negócio

Notebook:
`src/03_pos_processamento.ipynb`

Nesta etapa os resultados da mineração são transformados em **informação útil para análise e auditoria**.

Principais atividades:

* Definição de **threshold de anomalia**
* Filtragem das entidades mais suspeitas
* Integração com os dados originais
* Criação de um **ranking de casos críticos**

Threshold adotado:

```
HDBSCAN_Outlier_Score > 0.75
```

Saídas da análise:

* Lista das **maiores anomalias detectadas**
* **Top 10 registros com maior score de anomalia**
* Consolidação de gastos relevantes
* Base para investigação manual

---

# Pré-requisitos

* Python 3.10+
* pip
* Jupyter Notebook ou Google Colab

---

# Execução do Projeto

1. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

2. Baixe os datasets conforme descrito na seção **Download das Bases de Dados**.

3. Execute os notebooks na seguinte ordem:

```
1 → src/01_pre_processamento.ipynb
2 → src/02_mineracao_e_avaliacao.ipynb
3 → src/03_pos_processamento.ipynb
```

---

# Execução no Google Colab

1. Envie a pasta do projeto para o **Google Drive**.
2. Abra os notebooks pelo **Google Colab**.
3. Monte o Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

4. Ajuste os caminhos para a pasta `datasets` se necessário.

---

# Resultados Esperados

Ao final do pipeline, o projeto produz no arquivo:

```
./dados/relatorio_auditoria_final.csv
```

Este arquivo contém:

* CPF's dos portadores com comportamento anômalo
* Base de dados limpa e padronizada
* Identificação de clusters de comportamento de gastos
* Score de anomalia para cada registro
* Ranking de possíveis casos críticos para auditoria

O sistema funciona como uma **ferramenta exploratória de apoio à fiscalização de gastos públicos**, buscando evidenciar quais foram os portadores com o comportamento mais anômalo dos órgãos com maior volume de transações.

---

# Relatório Acadêmico

O relatório completo do projeto pode ser encontrado em:

```
relatorio/Relatório Projeto Final MD.pdf
```

Nesta pasta também está disponível a subpasta:

```
relatorio/referencias/
```

que contém os **artigos científicos e materiais utilizados como base teórica para o desenvolvimento do projeto**.

---

# Licença

Projeto acadêmico desenvolvido para fins educacionais.
