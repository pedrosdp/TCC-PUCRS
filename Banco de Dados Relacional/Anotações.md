# Aula 1 e 2 - Claudio Bonel

## Banco de dados
Representa algum cenário do mundo real (Minimundo). É uma coleção de dados **coerentes**, **correlacionáveis** e que, principalmente, tenham algum significado importante.

### Metadados
- São “dados sobre dados”.
- Exemplo: Título de uma coluna (rotulação).

### Sistema de Gerenciamento de Banco de Dados (SGBDs)
1. Microsoft SQL Server
2. Azure SQL DB
3. Oracle
4. MySQL
5. PostgreSQL

---

## Minimundo e Levantamento de Requisitos

### Tipos de dados
- **INT**
- **DECIMAL**, **FLOAT**, **REAL**
- **CHAR(4)**
- **VARCHAR**
- **DATE**
- **DATETIME**

---

## Modelos de Dados
Devem garantir **correlação**, **coerência** e **abstração**.  
Pelo fato de existirem relacionamentos, este modelo é frequentemente chamado de **modelo de dados relacional**.

### Cardinalidade
É um dos princípios fundamentais sobre o relacionamento em um banco de dados relacional, definindo o grau de relação entre duas entidades ou tabelas.

- **1 para muitos** (1,N)
- (Também existem 1,1 e N,N, mas aqui é enfatizado o 1 para muitos)

---

## Modelo de Dados Conceitual - MER (Modelo Entidade-Relacionamento)

- **Entidades**: Abstrações físicas ou conceituais (tabelas).
  - Exemplo: `CLIENTE`
- **Atributos**: Informações (metadados) a respeito dessas entidades.

---

## Exemplo Prático

### Principais Entidades

#### 1. Cliente
Atributos:
- CPF (chave primária)
- Nome
- Email
- Gênero
- Faixa salarial
- Dia/Mês de aniversário
- Bairro
- Cidade
- UF

#### 2. Venda
Atributos:
- ID da venda (chave primária)
- Data/hora da venda
- Código de barras (ou referência ao produto vendido)
- Valor total
- FK Cliente (para saber quem comprou)
- FK Vendedor (quem realizou a venda)

#### 3. Produto
Atributos:
- Código de barras (chave primária)
- Descrição
- Gênero do produto (ex.: vestuário masculino/feminino/unissex)
- FK Fornecedor (chave estrangeira para identificar de qual Fornecedor vem este produto)

#### 4. Vendedor
Atributos:
- Registro (chave primária)
- CPF
- Nome
- Email
- Gênero

#### 5. Fornecedor
Atributos:
- Registro do fornecedor (chave primária)
- Nome fantasia
- Razão social
- Cidade
- UF

---

## Leitura do Modelo
- **Cliente** faz uma ou várias **Vendas**.  
- **Vendedor** realiza uma ou várias **Vendas**.  
- **Venda** é composta por um ou vários **ItemVenda**, e cada `ItemVenda` referencia um **Produto** específico.  
- Cada **Produto** é fornecido por **exatamente um** Fornecedor (exclusividade do fornecedor em sua linha de produtos).  
- Cada **Fornecedor** pode fornecer vários **Produtos**.

---

## Diagrama Entidade-Relacionamento (Exemplo)



   ┌───────────────────┐
   │     CLIENTE       │
   │───────────────────│
PK │ CPF               │
   │ Nome              │
   │ Email             │
   │ Gênero            │
   │ FaixaSalarial     │
   │ DiaMesAniversario │
   │ Bairro            │
   │ Cidade            │
   │ UF                │
   └───────────────────┘
         (1,N)
          ┌───────────────┐
          │               │
          │               ▼
   ┌───────────────────┐            (N,1)   ┌───────────────────┐
   │       VENDA       │--------------------│     VENDEDOR      │
   │───────────────────│      FK: Registro  │───────────────────│
PK │ idVenda           │                   PK│ Registro          │
   │ DataHora          │                    │ CPF                │
   │ ValorTotal        │                    │ Nome               │
FK │ CPF_Cliente       │                    │ Email              │
FK │ Registro_Vendedor │                    │ Gênero             │
   └───────────────────┘                    └───────────────────┘
         (1,N)
          ┌───────────────┐
          │               │
          │               ▼
    ┌─────────────────────┐
    │     ITEMVENDA       │
    │─────────────────────│
PK1 │ idVenda  (FK → VENDA)   
PK2 │ codBarras (FK → PRODUTO) 
    │ Quantidade          
    │ PrecoUnitario       (opcional, p/ histórico)
    └─────────────────────┘
                (N,1)
                 ┌───────────────┐
                 │               │
                 │               ▼
       ┌─────────────────────┐           (N,1)   ┌─────────────────────┐
       │       PRODUTO       │-------------------│     FORNECEDOR      │
       │─────────────────────│     FK: Registro   │─────────────────────│
    PK │ codBarras           │                  PK│ RegistroFornecedor  │
       │ Descricao           │                    │ NomeFantasia        │
       │ GeneroProduto       │                    │ RazaoSocial         │
FK     │ RegistroFornecedor  │                    │ Cidade              │
       └─────────────────────┘                    │ UF                  │
                                                  └─────────────────────┘


---

## Restrições (Constraints)
Embora sejam opcionais, são **150% recomendadas**:
- **NOT NULL**: não permite valor nulo
- **UNIQUE**: valor exclusivo (sem repetição na coluna)

## Chave Primária
É comum que seu modelo de dados possua **chaves primárias** em **TODAS** as tabelas. Esta é uma boa prática para garantir a integridade dos dados.

## Chave Estrangeira
A **chave estrangeira** serve para fazer a ligação entre as entidades ou entre as tabelas, implementando as referências.

## Index
Os **índices** proporcionam velocidade no acesso às informações, agilizando a recuperação de registros durante as consultas aos dados.

---

## Modelo Lógico
O modelo lógico é uma evolução do modelo conceitual e representa o **desenho de fato** do banco de dados.

---

## Mapeamento de Objeto Relacional (ORM)
- Permite apenas uma forma de manipulação dos dados.
- Exemplo: Uso de ORM no **Python**.

---

## Consultando Dados no Banco de Dados
- **Querying DATA**: Refere-se à ação de realizar consultas no banco de dados.

# Aula 3 - Azriel Majdenbaum

## Características do SQL
- **Case insensitive**: O SQL não faz distinção entre maiúsculas e minúsculas.
- **Formatos flexíveis**: Pode ser escrito em uma única linha ou quebrado em várias.

---

## Principais Comandos SQL

### Criar Tabelas
```sql
CREATE TABLE nome_da_tabela (
    coluna1 tipo_de_dado,
    coluna2 tipo_de_dado
);


INSERT INTO nome_da_tabela (coluna1, coluna2)
VALUES (valor1, valor2);


consultar
SELECT *
FROM nome_da_tabela
WHERE condição;

Exemplo de comando para selecionar a placa, o ano e o modelo de veículos anteriores ao ano 2022

SELECT placa, ano, modelo
FROM VEICULOS
WHERE ano < 2022;


Atualizar
UPDATE nome_da_tabela
SET coluna = novo_valor
WHERE condição;


Exemplo: Experimente escrever o campo UPDATE para somar 100km a todos os veículos cjos anos estão entre 2015 e 2021 (inclusive)

UPDATE VEICULOS 
SET km = km + 100
WHERE (ano >= 2015) and (ano <=2021);

Excluir
DELETE FROM nome_da_tabela
WHERE condição;

Ordenar
SELECT *
FROM nome_da_tabela
ORDER BY coluna [ASC | DESC];


Contar quantos registros tem
SELECT COUNT (*)
FROM ...

Exercício: Quantos veículos da marca FORD estão cadastrados no banco de dados?

SELECT COUNT(*)
FROM VEICULOS
WHERE marca = 'FORD';


Mostar uma unidade
SELECT DISTINCT marca

Valores Nulo
      NOT NULL
      NULL

% substitui qualquer quantidade de caracteres

WHERE NOME LIKE '%CARLOS%'

_ substitui exatamente um caracter

IN valor numa lista

Removendo e adicionando novas colunas em tabelas

Alter Table
drop column

alter table 
add

DATAS
   datanasc

"pode fazer aritmética com datas" Exemplo:

SYSDATE + 30

# INTEGRIDADE DE ENTIDADE

- **CHAVE PRIMÁRIA (pk):** Atributo que não vai se repetir nunca.
- **UNIQUE (AKs):** Garante que os valores de uma coluna sejam únicos.

# INTEGRIDADE DE DOMÍNIO

- **Restringir os valores:** Define os valores permitidos em uma coluna.

# RESTRIÇÃO DE INTEGRIDADE REFERENCIAL

- **Vincular dados de uma tabela a outra:** Garante a consistência entre as tabelas relacionadas.

# JUNÇÕES E ENTRELAÇAMENTO

- **JOIN:**
  - `INNER JOIN`
  - `OUTER JOIN`

FUNÇÕES
   Sobre Linhas.
   Sobre Conjuntos de linhas.

Group by; Agrupamento de resultados
Having (condições)

Subconsultas; 2 consultas em 1 só;

Indexação
   Select nome, uf FROM CIDADES;
   Ordenação de dados.
   Pesquisa Binária

Índice - Tabela a parte (rowid)


