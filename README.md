🛒 NovaMart — Pipeline de Dados do Zero

Projeto de portfólio desenvolvido como exercício prático de análise de dados, cobrindo geração de dados com Python, armazenamento em banco SQLite, análise com SQL e visualização no Power BI.


📊 Resultado Final
O dashboard interativo está publicado e disponível online — os filtros por região e categoria funcionam em tempo real sobre todos os visuais.

🗂️ Estrutura do Projeto
📁 nova-marte/
├── 🐍 pipe-line.py              # Geração de dados e carga no banco
├── 🗄️ novamart.db               # Banco de dados SQLite
├── 📋 novamart.sqbpro           # Projeto DB Browser (queries salvas)
├── 📝 queries_completas.sql     # As 6 queries de análise
├── 📊 dashboard.pbix            # Dashboard Power BI
└── 📖 explicacao_pipe-line.txt  # Documentação do script Python

🔧 Tecnologias Utilizadas
TecnologiaUsoPython 3.14Geração de dados fictícios e carga no bancoPandasManipulação e estruturação dos dadosFakerGeração de nomes, datas e valores aleatóriosSQLiteBanco de dados relacional localSQLQueries de análise (JOIN, CTE, Window Functions)Power BI DesktopDashboard interativo

⚙️ Como Rodar o Projeto
Pré-requisitos

Python 3.x instalado
Power BI Desktop instalado
SQLite ODBC Driver instalado

Instalação
bash# Clone o repositório
git clone https://github.com/seu-usuario/nova-marte.git
cd nova-marte

# Instale as dependências
pip install -r requirements.txt
Rodando o pipeline
bashpython pipe-line.py
Saída esperada:
✅ 500 registros de vendas salvos em novamart.db
✅ 60 metas salvas em novamart.db

🐍 Etapa 1 — Python
O script pipe-line.py gera 500 registros de vendas fictícios e uma tabela de metas mensais por região, salvando tudo no banco novamart.db.
Tabela vendas:
ColunaTipoDescriçãoid_vendaINTEGERChave primáriadata_vendaTEXTData entre 01/01/2024 e 31/12/2024regiaoTEXTUma das 5 regiões do BrasilcategoriaTEXTEletrônicos, Roupas, Alimentos, Móveis ou EsportesvendedorTEXTNome fictício gerado pelo FakervalorREALValor entre R$ 50,00 e R$ 5.000,00quantidadeINTEGERQuantidade entre 1 e 20 itensticket_medioREALvalor / quantidade
Tabela metas:
ColunaTipoDescriçãoregiaoTEXTRegiãomesTEXTMês no formato YYYY-MMmetaREALMeta fixa de R$ 50.000,00 por região/mês

🗄️ Etapa 2 — SQL
Seis queries de análise escritas no DB Browser for SQLite:
QueryDescriçãoConceitosQ1Receita total por regiãoGROUP BY, SUM, COUNTQ2Ticket médio por categoriaAVG, GROUP BYQ3Evolução mensal de receitaSTRFTIME, GROUP BYQ4Top 5 vendedoresORDER BY DESC, LIMITQ5Crescimento % mês a mêsWITH (CTE), LAG()Q6Receita real vs metaJOIN, STRFTIME
Exemplo — Query 5 (crescimento mensal com Window Function):
sqlWITH mensal AS (
    SELECT
        STRFTIME('%Y-%m', data_venda) AS mes,
        ROUND(SUM(valor), 2)           AS receita
    FROM vendas
    GROUP BY mes
)
SELECT
    mes,
    receita AS receita_atual,
    LAG(receita) OVER (ORDER BY mes) AS receita_mes_anterior,
    ROUND(
        (receita - LAG(receita) OVER (ORDER BY mes))
        / LAG(receita) OVER (ORDER BY mes) * 100
    , 2) AS crescimento_pct
FROM mensal
ORDER BY mes;

📊 Etapa 3 — Power BI
Dashboard interativo com os seguintes visuais:

3 Cartões — Ticket Médio, Total Receita, Qtd Vendas
Gráfico de Barras — Receita por Região
Gráfico de Linhas — Evolução Mensal de Receita
Gráfico de Pizza — Receita por Categoria
Tabela — Ranking de Vendedores
2 Slicers — Filtro por Região e por Categoria

Medidas DAX criadas:
daxTotal Receita = SUM(vendas[valor])
Qtd Vendas = COUNTROWS(vendas)
Ticket Médio = DIVIDE([Total Receita], [Qtd Vendas])

📈 Principais Insights

Receita total 2024: R$ 1.260.798,11
Mês com maior queda: Novembro (-31% vs outubro)
Mês com maior crescimento: Abril (+23% vs março)
Todas as regiões ficaram abaixo da meta de R$ 50.000/mês — dado esperado para uma base de 500 vendas distribuídas entre 5 regiões × 12 meses


👤 Autor
Desenvolvido por José Leite Duarte Junior
Estudante de Sistemas para Internet — SENAC | Em transição para a área de dados


Projeto desenvolvido com fins educacionais. A empresa NovaMart e todos os dados são fictícios.
