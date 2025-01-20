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

Chave primária = é comum que seu modelo de dados possua chaves primárias em TODAS as tabelas. É uma boa prática, para garantir integridade de dados.

Chave estrangeira = serve para fazer a ligação entre as entidades ou entre as tabelas, elas implementam as referências.

Index - Velocidade no acesso às informações. Agilizar a recuperação de registros durante as consultas a dados.

Modelo Lógico
    evolução do conceitual
    desenho de fato

Mapeamento de objeto relacional - ORM
Apenas 1 forma de manipular
ORM no Python

