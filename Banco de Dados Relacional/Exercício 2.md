# Modelo Lógico - Estrutura e Restrições

| **Tabela**      | **Atributos**                                         | **Chave Primária (PK)**        | **Chaves Estrangeiras (FK)**                             | **Restrições Adicionais**                        |
|------------------|------------------------------------------------------|--------------------------------|----------------------------------------------------------|-------------------------------------------------|
| **DP**          | `Cod_DP`, `Nome`, `Endereco`                         | `Cod_DP`                       | -                                                        | `Cod_DP` deve ser único e não nulo.             |
| **Responsavel** | `Cod_DP`, `Delegado`                                 | `Cod_DP`                       | Referencia `DP(Cod_DP)`                                  | `Cod_DP` deve ser único (1 para 1 com `DP`).    |
| **Ocorrencias** | `Cod_DP`, `Cod_IBGE`, `Qtde`, `Ano`, `Mes`, `Ocorrencia` | (`Cod_DP`, `Cod_IBGE`, `Ano`, `Mes`) | Referencia `DP(Cod_DP)`, `Municipios(Cod_IBGE)`          | `Qtde` deve ser >= 0. `Ano` e `Mes` devem ser válidos. |
| **Municipios**  | `Cod_IBGE`, `Nome`, `Regiao`                         | `Cod_IBGE`                     | -                                                        | `Cod_IBGE` deve ser único e não nulo.           |

## Restrições e Detalhes:

1. **DP (Delegacia de Polícia)**:
   - `Cod_DP` é a **chave primária** e deve ser único.
   - `Nome` e `Endereco` são atributos descritivos.

2. **Responsável**:
   - `Cod_DP` é **chave primária** e **chave estrangeira** para `DP`.
   - Relacionamento **1 para 1** com `DP`.

3. **Ocorrências**:
   - A **chave primária composta** é formada por: `Cod_DP`, `Cod_IBGE`, `Ano`, e `Mes`.
   - `Cod_DP` é uma **chave estrangeira** que referencia `DP(Cod_DP)`.
   - `Cod_IBGE` é uma **chave estrangeira** que referencia `Municipios(Cod_IBGE)`.
   - Restrições adicionais:
     - `Qtde` (quantidade de ocorrências) deve ser maior ou igual a zero.
     - `Ano` e `Mes` devem representar valores válidos (exemplo: `Mes` entre 1 e 12).

4. **Municípios**:
   - `Cod_IBGE` é a **chave primária** e deve ser único.
   - Atributos descritivos: `Nome` e `Regiao`.

-- Criação da tabela DP 
CREATE TABLE DP (
    Cod_DP      INT           NOT NULL,
    Nome        VARCHAR(100)  NOT NULL,
    Endereco    VARCHAR(255)  NOT NULL,
    CONSTRAINT PK_DP PRIMARY KEY (Cod_DP)
);

-- Criação da tabela Responsavel
CREATE TABLE Responsavel (
    Cod_DP      INT           NOT NULL,
    Delegado    VARCHAR(100)  NOT NULL,
    CONSTRAINT PK_Responsavel PRIMARY KEY (Cod_DP),
    CONSTRAINT FK_Responsavel_DP 
        FOREIGN KEY (Cod_DP) 
        REFERENCES DP (Cod_DP)
);

-- Criação da tabela Municipios
CREATE TABLE Municipios (
    Cod_IBGE    INT           NOT NULL,
    Nome        VARCHAR(100)  NOT NULL,
    Regiao      VARCHAR(100)  NOT NULL,
    CONSTRAINT PK_Municipios PRIMARY KEY (Cod_IBGE)
);

-- Criação da tabela Ocorrencias
CREATE TABLE Ocorrencias (
    Cod_DP      INT           NOT NULL,
    Cod_IBGE    INT           NOT NULL,
    Qtde        INT           NOT NULL 
                              CONSTRAINT CH_Ocorrencias_Qtde 
                              CHECK (Qtde >= 0),
    Ano         INT           NOT NULL 
                              CONSTRAINT CH_Ocorrencias_Ano 
                              CHECK (Ano >= 1900),   -- Ajuste conforme necessidade
    Mes         INT           NOT NULL 
                              CONSTRAINT CH_Ocorrencias_Mes 
                              CHECK (Mes BETWEEN 1 AND 12),
    Ocorrencia  VARCHAR(255),
    CONSTRAINT PK_Ocorrencias 
        PRIMARY KEY (Cod_DP, Cod_IBGE, Ano, Mes),
    CONSTRAINT FK_Ocorrencias_DP 
        FOREIGN KEY (Cod_DP) 
        REFERENCES DP (Cod_DP),
    CONSTRAINT FK_Ocorrencias_Municipios 
        FOREIGN KEY (Cod_IBGE) 
        REFERENCES Municipios (Cod_IBGE)
);
