# ECommerce
![Python](https://img.shields.io/badge/Python-3.10%2B-2a9d8f)
![DuckDB](https://img.shields.io/badge/DuckDB-1.3.0-264653)
![Pandas](https://img.shields.io/badge/Pandas-2.3.0-e9c46a)
![Pandera](https://img.shields.io/badge/Pandera-0.24.0-f4a261)
![Pytest](https://img.shields.io/badge/Pytest-8.4.0-e76f51)
![Ruff](https://img.shields.io/badge/Ruff-0.11.13-8a4fff)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-ff4b4b)
![Taskipy](https://img.shields.io/badge/Taskipy-1.12.0-2e7d32)


## Estrutura de Diretórios
<pre lang="markdown"><code>.
├── README.md                 # Documentação principal do projeto
├── .gitignore                # Arquivos e pastas ignorados pelo Git
├── .python-version           # Versão do Python utilizada
├── poetry.lock               # Arquivo de bloqueio de dependências
├── pyproject.toml            # Configuração do projeto e dependências
├── data/
│   └── data.csv              # Conjunto de dados de entrada
├── ecommerce/
│   ├── main.py               # Script principal da aplicação
│   ├── schema.py             # Definições de schemas e validações
│   └── pipeline/
│       ├── extract.py        # Funções de extração de dados
│       ├── load.py           # Funções para carregar dados
│       └── transform.py      # Funções de transformação de dados
├── tests/
│   └── test_read_file.py     # Testes para leitura de arquivos
└── .github/
    └── workflows/
        └── CI.yaml           # CI com GitHub Actions
</code></pre>