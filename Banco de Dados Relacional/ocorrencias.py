import sqlalchemy as sa
import sqlalchemy.orm as orm
engine = sa.create_engine("sqlite:///BD//ocorrencias.db")

Base = orm.declarative_base()

# Tabela tbDP
class DP(Base):
    __tablename__ = "tbDP"

    codDP = sa.Column(sa.Integer, primary_key=True, index=True)
    nome = sa.Column(sa.String(100), nullable=False)
    endereco = sa.Column(sa.String(255), nullable=False)

# Tabela tbResponsavelISP
class ResponsavelISP(Base):
    __tablename__ = "tbResponsavelISP"

    # codDP também é PK, mas referenciando tbDP
    codDP = sa.Column(
        sa.Integer,
        sa.ForeignKey("tbDP.codDP", ondelete="NO ACTION", onupdate="CASCADE"),
        primary_key=True,
        index=True
    )
    delegado = sa.Column(sa.String(100), nullable=False)

# Tabela tbMunicipio
class Municipio(Base):
    __tablename__ = "tbMunicipio"

    codIBGE = sa.Column(sa.Integer, primary_key=True, index=True)
    municipio = sa.Column(sa.String(100), nullable=False)
    regiao = sa.Column(sa.String(25), nullable=False)

# Tabela tbOcorrencias
class Ocorrencias(Base):
    __tablename__ = "tbOcorrencias"

    idRegistro = sa.Column(sa.Integer, primary_key=True, index=True)
    codDP = sa.Column(
        sa.Integer,
        sa.ForeignKey("tbDP.codDP", ondelete="NO ACTION", onupdate="CASCADE"),
        nullable=False,
        index=True
    )
    codIBGE = sa.Column(
        sa.Integer,
        sa.ForeignKey("tbMunicipio.codIBGE", ondelete="NO ACTION", onupdate="CASCADE"),
        nullable=False,
        index=True
    )
    ano = sa.Column(sa.CHAR(4), nullable=False)
    mes = sa.Column(sa.String(2), nullable=False)
    ocorrencia = sa.Column(sa.String(100), nullable=False)
    qtde = sa.Column(sa.Integer, nullable=False)
