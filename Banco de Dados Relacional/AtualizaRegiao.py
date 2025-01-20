import sqlalchemy as sa
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

metadado = sa.MetaData(bind=engine)
sa.MetaData.reflect(metadado)

tbMunicipio = metadado.tables[oc.municipio.__tablename__]

atualiza_regiao = sa.update(tbMunicipio).values({"regiao": "Rio de Janeiro"}) \
    .where(tbMunicipio.c.municipio == "Rio de Janeiro")

try:
    engine.execute(atualiza_regiao)
    print("Dados atualizados")
except ValueError:
    ValueError()
