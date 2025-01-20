# Modelo de Dados para Delegacias de Polícia

## 1. Visão Geral das Necessidades

### Delegacia de Polícia (DP)
- Possui um **código identificador** (código da DP), **nome** e **endereço**.
- Cada DP deve ser vinculada a um(a) **responsável** (delegado(a) principal).
- **Dado sensível** (dados pessoais do(a) responsável) não deve ficar na mesma tabela que os dados da DP.

### Responsável pela Delegacia
- Devemos guardar o **nome** do(a) responsável separadamente, sem outras informações sensíveis.
- Deve haver **relacionamento** entre a DP e seu(sua) responsável.

### Município
- Para cada município, armazenar:
  - **Nome do município**
  - **Código do IBGE**
  - **Região** (à qual o município pertence).

### Ocorrências
- Precisamos mapear a quantidade de **registros de ocorrências** no Estado do Rio de Janeiro considerando:
  - **Ano**
  - **Mês**
  - **Tipo de ocorrência**
  - A **DP** em que foi registrada (ou à qual se refere).

---

## 2. Entidades Propostas

### MUNICÍPIO
- **codIBGE** (chave primária)
- **nomeMunicipio**
- **regiao**

Cada município do Rio de Janeiro tem um código IBGE único. Um mesmo município pode ter várias delegacias (relação 1 para N).

---

### DELEGACIA
- **codDP** (chave primária)
- **nomeDP**
- **endereco**
- **codIBGE** (chave estrangeira para **MUNICÍPIO**)

Aqui constam apenas informações **não sensíveis** da DP. Cada delegacia se localiza em um município (relação muitos-para-um com **MUNICÍPIO**).

---

### RESPONSÁVEL
- **idResponsavel** (chave primária)
- **nomeResponsavel**
- **codDP** (chave estrangeira para **DELEGACIA**, tipicamente 1:1)

Para cumprir a exigência de **separar informações sensíveis**, criamos a tabela **RESPONSÁVEL**.  
Se cada DP tem exatamente um responsável, a relação é 1:1 (embora, em alguns cenários, poderíamos ter 1:N caso um(a) responsável atenda mais de uma DP).

---

### OCORRÊNCIA
- **idOcorrencia** (chave primária)
- **ano**
- **mes**
- **tipoOcorrencia**
- **quantidade** (número de registros daquela ocorrência)
- **codDP** (chave estrangeira para **DELEGACIA**)

Esta tabela representa o **total de registros** de um determinado tipo de ocorrência, em um mês e ano específicos, vinculados a uma determinada DP.  
Caso fosse necessário detalhar cada ocorrência individual, poderíamos adicionar mais campos, como data/hora exata, descrição, etc.

---

## 3. Como as Entidades se Relacionam

- **MUNICÍPIO — (1 : N) — DELEGACIA**  
  Um município pode ter várias delegacias; cada delegacia pertence a um único município.

- **DELEGACIA — (1 : 1) — RESPONSÁVEL**  
  Cada delegacia possui exatamente um(a) responsável principal.  
  (Ou 1 : N, se uma pessoa puder responder por mais de uma DP, conforme a regra de negócio.)

- **DELEGACIA — (1 : N) — OCORRÊNCIA**  
  Uma delegacia pode registrar várias ocorrências ao longo do tempo; cada ocorrência (agregada em ano, mês, tipo) está vinculada a uma única delegacia.

---

## 4. Exemplo de Diagrama (Entidade‐Relacionamento)

        ┌───────────┐         (1,N)       ┌─────────────┐
        │ MUNICÍPIO │---------------------│ DELEGACIA   │
        │-----------│  FK codIBGE        └─────────────┘
        │ codIBGE PK│                     (1,1)
        │ nomeMun   │---------------------┐
        │ regiao    │   FK codDP         ┌┴──────────────┐
        └───────────┘                   │ RESPONSÁVEL    │
                                        │----------------│
                                        │ idResponsavelPK│
                                        │ nomeResponsavel│
                                        └────────────────┘

       DELEGACIA (1,N) ────────── OCORRÊNCIA
                     FK codDP  ┌───────────────────────┐
                                │ idOcorrencia PK       │
                                │ ano                   │
                                │ mes                   │
                                │ tipoOcorrencia        │
                                │ quantidade            │
                                └───────────────────────┘
MUNICÍPIO (1 : N) DELEGACIA
DELEGACIA (1 : 1 ou 1 : N, conforme a regra) RESPONSÁVEL
DELEGACIA (1 : N) OCORRÊNCIA
