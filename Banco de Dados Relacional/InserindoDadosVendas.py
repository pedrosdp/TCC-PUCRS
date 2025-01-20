import pandas as pd

# Ajuste o caminho
endereco = r"C:\Users\"

# Lê o CSV e transforma em DataFrame
vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";")
tbVendedor = pd.DataFrame(vendedor)

import sqlalchemy as sa
engine = sa.create_engine("sqlite:///BD//vendas.db")

import sqlalchemy.orm as orm
sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

import vendas as vd

# Loop para inserir cada linha do DataFrame na tabela 'vendedor'
for i in range(len(tbVendedor)):
    dados_vendedor = vd.vendedor(
        registro_vendedor=int(tbVendedor["registro_vendedor"][i]),
        cpf=tbVendedor["cpf"][i],
        nome=tbVendedor["nome"][i],
        genero=tbVendedor["genero"][i],
        email=tbVendedor["email"][i]
    )
    try:
        sessao.add(dados_vendedor)
        sessao.commit()
    except ValueError:
        ValueError()

print("Dados inseridos na tbVendedor")

#tbProduto
produto = pd.read_excel(endereco + "produto.xlsx")
tbProduto = pd.DataFrame(produto)

conn = engine.connect()
metadata = sa.schema.MetaData(bind=engine)

DadosProduto = tbProduto.to_dict(orient="records")

tabela_produto = sa.Table(vd.produto.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_produto.insert(), DadosProduto)
    sessao.commit()
except ValueError:
    ValueError()

print("Dados inserido na tbProduto")


sessao.close_all()

