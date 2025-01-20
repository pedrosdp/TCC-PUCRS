import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

endereco = "C:\\Users"

dp = pd.read_csv(endereco + "DP.csv", sep=",")
responsavelDP = pd.read_excel(endereco + "ResponsavelDP.xlsx")
municipio = pd.read_csv(endereco + "Municipio.csv", sep=",")
ocorrencias = pd.read_excel(endereco + "ocorrencias.xlsx")

tbDP = pd.DataFrame(dp)
tbResponsavelDP = pd.DataFrame(responsavelDP)
tbMunicipio = pd.DataFrame(municipio)
tbOcorrencias = pd.DataFrame(ocorrencias)

engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

conn = engine.connect()
metadata = sa.schema.MetaData(bind=engine)
Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

# DP
DadosDP = tbDP.to_dict(orient="records")
tabela_DP = sa.Table(oc.DP.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_DP.insert(), DadosDP)
    sessao.commit()
except ValueError:
    ValueError()

#ResponsavelDP
DadosRespDP = tbResponsavelDP.to_dict(orient="records")
tabela_respDP = sa.Table(oc.responsavelDp.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_respDP.insert(), DadosRespDP)
    sessao.commit()
except ValueError:
    ValueError()

print("Dados inseridos na tbResponsavelDP")

#Municipio
DadosMunicipio = tbMunicipio.to_dict(orient="records")
tabela_municipio = sa.Table(oc.municipio.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_municipio.insert(), DadosMunicipio)
    sessao.commit()
except ValueError:
    ValueError()

print("Dados inseridos na tbMunicipio")

#ocorrencia
DadosOcorrencia = tbOcorrencias.to_dict(orient="records")
tabela_ocorrencia = sa.Table(oc.ocorrencia.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_ocorrencia.insert(), DadosOcorrencia)
    sessao.commit()
except ValueError:
    ValueError()

print("Dados inseridos na tbOcorrencia")


sessao.close_all()
print("Carga de dados finalizada.")

