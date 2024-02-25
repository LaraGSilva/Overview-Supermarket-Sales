# Dashboard de Vendas Mensais 🧾🛍️🛒

Este projeto consiste em um painel interativo construído com Streamlit para visualizar dados de vendas mensais de um supermercado.

## Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas Python: streamlit, pandas, plotly

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

Para executar o painel, navegue até o diretório raiz do projeto e execute o seguinte comando:

```bash
streamlit run app/main.py
```

Isso iniciará o servidor Streamlit e abrirá automaticamente o painel em seu navegador padrão.

## Funcionalidades

- O painel permite selecionar o mês desejado para visualizar os dados de vendas.
- Apresenta gráficos interativos de barra e pizza para visualizar o faturamento por período, tipo de produto, tipo de pagamento e filial.
- Inclui uma visualização da avaliação média por filial.

## Estrutura do Projeto

- `app/main.py`: Script principal que contém o código do painel Streamlit.
- `database/supermarket_sales.csv`: Conjunto de dados de vendas do supermercado.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/): Biblioteca para construção de aplicativos da web com Python.
- [Pandas](https://pandas.pydata.org/): Biblioteca Python para manipulação e análise de dados.
- [Plotly](https://plotly.com/python/): Biblioteca para criação de gráficos interativos.

Pandas: Biblioteca Python para manipulação e análise de dados.
Plotly: Biblioteca para criação de gráficos interativos.
