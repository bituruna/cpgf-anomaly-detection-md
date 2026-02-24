# Pré-processamento — Cartão de Pagamento do Governo Federal (CPGF)

**Disciplina:** FACOM39803 — Mineração de Dados Aplicada a Finanças  
**Etapa:** 1 de 3 — Pré-processamento

---

## Descrição

Este módulo realiza o **pré-processamento** dos dados públicos do Cartão de Pagamento do Governo Federal (CPGF), disponibilizados pelo Portal da Transparência. O objetivo é preparar a base de dados para as etapas subsequentes de mineração (detecção de outliers) e pós-processamento.

O pipeline de pré-processamento contempla:
- **Exploração dos dados** — estatísticas resumidas e visualizações
- **Qualidade dos dados** — tratamento de valores ausentes, ruído e inconsistências
- **Transformação** — normalização dos atributos financeiros contínuos

## Estrutura do Projeto

```
cpgf-pre-processamento/
├── dados/                              # Dados brutos do CPGF (CSVs 2022+)
│   └── link_acesso_dados.txt           # Link externo para arquivos > 20 MB
├── src/                                # Código-fonte
│   └── 01_pre_processamento.ipynb      # Notebook de pré-processamento
├── relatorio/                          # Relatório (PDF)
├── README.md
└── requirements.txt
```

## Pré-requisitos

- Python 3.10+
- pip

## Instalação e Execução (Linux — Fedora 42 / Ubuntu 24.04)

```bash
# 1. Extrair o projeto
unzip cpgf-pre-processamento.zip
cd cpgf-pre-processamento

# 2. Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Baixar os dados
# Consulte dados/link_acesso_dados.txt para o link de download dos CSVs.
# Coloque os arquivos CSV dentro da pasta dados/

# 5. Executar o notebook
jupyter notebook src/01_pre_processamento.ipynb
```

## Execução no Google Colab

1. Faça upload da pasta para o Google Drive.
2. Abra o notebook `src/01_pre_processamento.ipynb` pelo Colab.
3. Monte o Drive na primeira célula do notebook.

## Saídas Geradas

Após a execução, dois arquivos são gerados na pasta `dados/`:

| Arquivo | Descrição |
|---------|-----------|
| `cpgf_limpo.csv` | Dados limpos (sem nulos, sem ruído), valores originais |
| `cpgf_normalizado.csv` | Dados normalizados (Z-Score), prontos para mineração |
