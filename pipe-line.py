import sqlite3
import pandas as pd
from faker import Faker
import random
from datetime import date

fake = Faker('pt_BR')
random.seed(42)

# --- Dados fixos de referência ---
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis', 'Esportes']

# --- Gerar tabela de vendas ---
registros = []
for i in range(500):
    valor = round(random.uniform(50, 5000), 2)
    quantidade = random.randint(1, 20)

    registros.append({
        'id_venda':   i + 1,
        'data_venda': fake.date_between(
                         start_date=date(2024, 1, 1),
                         end_date=date(2024, 12, 31)
                      ),
        'regiao':     random.choice(regioes),
        'categoria':  random.choice(categorias),
        'vendedor':   fake.name(),
        'valor':      valor,
        'quantidade': quantidade,
        'ticket_medio': round(valor / quantidade, 2)
    })

vendas_df = pd.DataFrame(registros)

# --- Criar tabela de metas ---
meses = []
for mes in range(1, 13):
    # esse f' serve para: o valor 2024 ser fixo, ou seja o ano dessa lista nao muda. {o mes:02d } significa que o mes sera formatado com (2) digitos (...d).
    meses.append(f'2024-{mes:02d}')
meta_por_regiao = 50000
metas_registros = []
for regiao in regioes:
    for mes in meses:
        metas_registros.append({
            'regiao': regiao,
            'mes': mes,
            'meta': meta_por_regiao
        })

metas_df = pd.DataFrame(metas_registros)

# --- Salvar no SQLite ---
conn = sqlite3.connect('novamart.db')
vendas_df.to_sql('vendas', conn, if_exists='replace', index=False)
metas_df.to_sql('metas', conn, if_exists='replace', index=False)
conn.close()

print(f"✅ {len(vendas_df)} registros de vendas salvos em novamart.db")
print(f"✅ {len(metas_df)} metas salvas em novamart.db")
print(vendas_df.head())
print(metas_df.head())